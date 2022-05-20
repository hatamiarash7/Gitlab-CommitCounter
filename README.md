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

---

## Support

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz)](https://en.cryptobadges.io/donate/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz) [![Donate with Ethereum](https://en.cryptobadges.io/badge/micro/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)](https://en.cryptobadges.io/donate/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D1WGU9)

<div><a href="https://payping.ir/@hatamiarash7"><img src="https://cdn.payping.ir/statics/Payping-logo/Trust/blue.svg" height="128" width="128"></a></div>

## Contributing

Don't be shy and reach out to us if you want to contribute 😉

1. Fork it !
2. Create your feature branch : `git checkout -b my-new-feature`
3. Commit your changes : `git commit -am 'Add some feature'`
4. Push to the branch : `git push origin my-new-feature`
5. Submit a pull request

## Issues

Each project may have many problems. Contributing to the better development of this project by reporting them. 👍
