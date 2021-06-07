# Jenkins Push URL Generator

Generates [Push Notification URLs](https://wiki.jenkins.io/display/JENKINS/Git+Plugin) to be used by Git repositories to trigger [Jenkins](https://jenkins.io/) builds.


#### Usage

```sh
# URL for host passed by parameter
python generate_url.py -j https://example.jenkins.org:9090 git@example.com:abc/git-repo.git

# URL for 'prod' host predefined in 'jenkins.conf'
python generate_url.py -e prod git@example.com:abc/git-repo.git

# URL for all hosts predefined in 'jenkins.conf'
python generate_url.py -a git@example.com:abc/git-repo.git
```

Use `python generate-url.py --help` for more information.


##### Predefined environments

The `--environment` / `-e` options load the host and port by name from the `jenkins.conf` file.
Each entry consists of a *name* and the *host* (with a optional port). `https://` is added if neither `https://` nor `http://` is present. Use `-a` / `--all` to generate URLs for all entries.

```ini
[instances]
prod = jenkins-prod-1
staging = jenkins-staging:8081
test = jenkins-test:8082
```
