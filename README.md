# phennec-sample

Sample repository for [Phennec](https://phennec.ai/en/), the context platform for AI-driven development by Aitria.

It holds short guides and example files based on the public Phennec usage guide, and shows how an AI agent can explore a GitHub repository through Phennec: files, branches, commits, tags, issues and pull requests.

## Contents

| Path | What it is |
|---|---|
| [docs/getting-started.md](docs/getting-started.md) | Account, setup wizard, first data source, AI agent connection |
| [docs/data-sources.md](docs/data-sources.md) | What each data source needs |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Common problems and fixes |
| [examples/aws/s3-readonly-policy.json](examples/aws/s3-readonly-policy.json) | Least-privilege IAM policy for an S3 data source |
| [examples/agents/AGENTS.md](examples/agents/AGENTS.md) | Agent rules that make Phennec usage reliable |
| [tools/check_s3_policy.py](tools/check_s3_policy.py) | Checks that an S3 policy is read-only |

## Check an S3 policy

```bash
python tools/check_s3_policy.py examples/aws/s3-readonly-policy.json YOUR-BUCKET-NAME
```

Run the tests:

```bash
python -m unittest discover tests
```

## Links

- [Phennec](https://phennec.ai/en/)
- [Usage guide](https://phennec.ai/en/setup)
- [FAQ](https://phennec.ai/en/faq)
- [Release notes](https://phennec.ai/en/release-notes)
