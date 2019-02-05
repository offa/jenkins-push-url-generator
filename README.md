# Jenkins Push URL Generator

Generates [Push Notification URLs](https://wiki.jenkins.io/display/JENKINS/Git+Plugin) to be used by Git repositories to trigger [Jenkins](https://jenkins.io/) builds.


#### Usage

```sh
# Pass host by parameter
python generate-url.py -j https://example.jenkins.org:9090 -r git@example.com:abc/git-repo.git

# Load host from list predefined in 'jenkins.conf'
python generate-url.py -e prod -r git@example.com:abc/git-repo.git
```

Use `python generate-url.py --help` for more information.


##### Predefined environments

The `--environment` / `-e` options load the host and port by name from the `jenkins.conf` file.
Each entry consists of a *name* and the *host* (with port) – `https://` is added by default.

```init
[instances]
prod = jenkins-prod-1:8080
staging = jenkins-staging:8081
test = jenkins-test:8082
```
