# Count commits for Gitlab repository

It's a small Docker image to count commits for a Gitlab repository. There is an API endpoint to do that :

```
https://gitlab.com/api/v4/projects/<ID>/repository/commits
```

### Install

```bash
docker pull hatamiarash7/gitlab-commit-counter
```

### Environment variables

- **PROJECT_ID** : Project id for specific repository. You can find it under title or `Settings > General`
- ACCESS_TOKEN : Personal access token for your account. You can create a token in `User Settings > Access Tokens`
- BRANCH : Branch name

### Usage

```bash
docker run --rm -e "PROJECT_ID=13960749" -e "ACCESS_TOKEN=erplmkbnoihsdFgfalsdk" -e "BRANCH=master" hatamiarash7/gitlab-commit-counter
```
