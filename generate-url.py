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
    required.add_argument('--repo', '-r', type=str, required=True,
                          help='Git Repository URL (ssh://<url> or https://<url>)')
    parser.add_argument('--version', action='version', version="%(prog)s 0.0.1",
                        help='Shows the program version')

    return parser.parse_args()


def load_from_file(env_name):
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    host = cfg['instances'][env_name]

    return "https://{}".format(host)


def generate_url(repo, jenkins):
    return "{}/git/notifyCommit?url={}".format(jenkins, repo)


def main():
    args = parse_args()

    if args.jenkins:
        repo_url = args.jenkins
    elif args.environment:
        repo_url = load_from_file(args.environment)
    else:
        repo_url = "<URL>:<PORT>"

    notification_url = generate_url(args.repo, repo_url)
    print("Push Notification URL:\n\n{}\n".format(notification_url))


if __name__ == '__main__':
    main()
