# Jenkins Push URL Generator

Generates [Push Notification URLs](https://wiki.jenkins.io/display/JENKINS/Git+Plugin) to be used by Git repositories to trigger [Jenkins](https://jenkins.io/) builds.


#### Usage

```sh
python generate-url.py -j https://example.jenkins.org:9090 -r git@example.com:abc/git-repo.git
`````

Use `python generate-url.py --help` for more information.

