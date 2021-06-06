# Jenkins Push URL Generator
#
# Copyright (C) 2019-2021  offa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import configparser

CONFIG_FILE = 'jenkins.conf'


def parse_args():
    parser = argparse.ArgumentParser(prog="generate-url",
                                     description='Generate Git Push Notification URLs for Jenkins.')
    required = parser.add_argument_group('arguments')
    required.add_argument('--jenkins', '-j', type=str, help='Jenkins URL (https://<url>[:<port>])')
    required.add_argument('--environment',
                          '-e',
                          type=str,
                          help='Jenkins Environment (jenkins.conf)')
    required.add_argument('--all',
                          '-a',
                          action='store_true',
                          help='All Jenkins Environments (jenkins.conf)')
    required.add_argument('--repo',
                          '-r',
                          type=str,
                          required=True,
                          help='Git Repository URL (ssh://<url> or https://<url>)')
    parser.add_argument('--quiet', '-q', action='store_true', help='Prints URL only')
    parser.add_argument('--version',
                        '-v',
                        action='version',
                        version="%(prog)s 0.0.1",
                        help='Shows the program version')

    return parser.parse_args()


def load_config():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    return cfg['instances']


def generate_url(repo, jenkins):
    url_prefix = "" if jenkins.startswith('https://') or jenkins.startswith(
        "http://") else "https://"
    return "{}{}/git/notifyCommit?url={}".format(url_prefix, jenkins, repo)


def print_url(url, name, quiet):
    if quiet:
        print("{}".format(url))
    else:
        prefix = " * {}:\t ".format(name) if name else 'Push Notification URL:\n\n'
        print("{}{}".format(prefix, url))


def main():
    args = parse_args()

    if args.jenkins:
        instances = [(None, args.jenkins)]
    elif args.all:
        instances = load_config().items()
    elif args.environment:
        instances = [(args.environment, load_config()[args.environment])]
    else:
        instances = [(None, "<URL>:<PORT>")]

    for (name, url) in instances:
        notification_url = generate_url(args.repo, url)
        print_url(notification_url, name, args.quiet)


if __name__ == '__main__':
    main()
