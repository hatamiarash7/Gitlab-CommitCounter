# Count commits for Gitlab repository

[![GitHub license](https://img.shields.io/github/license/hatamiarash7/Gitlab-CommitCounter)](https://github.com/hatamiarash7/Gitlab-CommitCounter/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/hatamiarash7/Gitlab-CommitCounter) ![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/hatamiarash7/gitlab-commit-counter) ![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/hatamiarash7/gitlab-commit-counter?sort=date)

It's a small Docker image to count commits for a Gitlab repository. There is an [API endpoint](https://docs.gitlab.com/ee/api/commits.html) to do that :

```
https://gitlab.com/api/v4/projects/<ID>/repository/commits
```

### Install

```bash
docker pull hatamiarash7/gitlab-commit-counter
```

### Environment variables

- **PROJECT_ID** : Project id for specific repository. You can find it under title or `Settings > General`
- **ACCESS_TOKEN** : Personal access token for your account. You can create a token in `User Settings > Access Tokens`
- **BRANCH** : Branch name

### Usage

```bash
docker run --rm -e "PROJECT_ID=13960749" -e "ACCESS_TOKEN=erplmkbnoihsdFgfalsdk" -e "BRANCH=master" hatamiarash7/gitlab-commit-counter
```
