# Jenkins Push URL Generator
#
# Copyright (C) 2019  offa
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
    required.add_argument('--jenkins', '-j', type=str,
                          help='Jenkins URL (https://<url>[:<port>])')
    required.add_argument('--environment', '-e', type=str,
                          help='Jenkins Environment (jenkins.conf)')
    required.add_argument('--all', '-a', action='store_true',
                          help='All Jenkins Environments (jenkins.conf)')
    required.add_argument('--repo', '-r', type=str, required=True,
                          help='Git Repository URL (ssh://<url> or https://<url>)')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Prints URL only')
    parser.add_argument('--version', '-v', action='version', version="%(prog)s 0.0.1",
                        help='Shows the program version')

    return parser.parse_args()


def load_from_file(env_name):
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    host = cfg['instances'][env_name]

    return "https://{}".format(host)


def generate_url(repo, jenkins):
    return "{}/git/notifyCommit?url={}".format(jenkins, repo)


def print_url(url, quiet):
    if quiet:
        print("{}".format(url))
    else:
        print("Push Notification URL:\n\n{}\n".format(url))


def main():
    args = parse_args()

    if args.jenkins:
        instances = [args.jenkins]
    elif args.all:
        raise NotImplementedError
    elif args.environment:
        instances = [load_from_file(args.environment)]
    else:
        instances = ["<URL>:<PORT>"]

    for instance in instances:
        notification_url = generate_url(args.repo, instance)
        print_url(notification_url, args.quiet)


if __name__ == '__main__':
    main()
