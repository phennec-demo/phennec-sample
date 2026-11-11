# Data sources

What each data source needs. Full instructions: [Phennec usage guide](https://phennec.ai/en/setup).

| Type | What you need |
|---|---|
| GitLab | Repository URL + access token with `read_repository` and `read_api` |
| GitHub | Repository URL + personal access token |
| Google Drive | Folder URL, shared with `syncer@phennec.iam.gserviceaccount.com` as Editor |
| Backlog | Project URL + API key |
| Notion | Page URL + connection access token |
| DocBase | Group URL + access token with Read scope |
| Slack | Channel link + the Phennec app added to the channel |
| Confluence | Space URL + Atlassian account email + API token |
| Jira | Project URL + Atlassian account email + API token |
| File upload | Nothing — up to 100 MB per file, 10 files per upload |
| Amazon S3 | Bucket name, region, access key ID and secret access key |
| Filesystem | Directory path |

## GitHub

1. In GitHub, open **Settings → Developer settings → Personal access tokens**.
2. Create a **Personal access token (classic)** with the `repo` scope and copy it.
3. In Phennec, add a data source of type **GitHub** and enter the repository URL and the token.

## Amazon S3

Use a dedicated IAM user with least privilege. The policy in
[examples/aws/s3-readonly-policy.json](../examples/aws/s3-readonly-policy.json) allows only listing the bucket and reading its objects.
