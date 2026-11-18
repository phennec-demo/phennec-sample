"""Check that an IAM policy for a Phennec S3 data source is read-only.

The policy may allow only s3:ListBucket on the bucket and s3:GetObject on its objects.
With a prefix, s3:GetObject may also be limited to objects under that prefix.

Usage: python tools/check_s3_policy.py POLICY.json BUCKET [PREFIX]
"""
import json
import sys

ALLOWED = {"s3:ListBucket", "s3:GetObject"}


def as_list(value):
    return value if isinstance(value, list) else [value]


def check(policy, bucket, prefix=None):
    """Return a list of problems; an empty list means the policy is fine."""
    expected = {
        "s3:ListBucket": {f"arn:aws:s3:::{bucket}"},
        "s3:GetObject": {f"arn:aws:s3:::{bucket}/*"},
    }
    if prefix:
        expected["s3:GetObject"].add(f"arn:aws:s3:::{bucket}/{prefix.strip('/')}/*")
    problems = []
    for i, statement in enumerate(as_list(policy.get("Statement", []))):
        if statement.get("Effect") != "Allow":
            continue
        for action in as_list(statement.get("Action", [])):
            if action not in ALLOWED:
                problems.append(f"statement {i}: action {action} is not allowed")
                continue
            for resource in as_list(statement.get("Resource", [])):
                if resource not in expected[action]:
                    allowed = " or ".join(sorted(expected[action]))
                    problems.append(f"statement {i}: {action} on {resource}, expected {allowed}")
    return problems


def main(argv):
    if len(argv) not in (3, 4):
        print(__doc__.strip().splitlines()[-1])
        return 2
    with open(argv[1], encoding="utf-8") as f:
        problems = check(json.load(f), argv[2], argv[3] if len(argv) == 4 else None)
    for p in problems:
        print(p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
