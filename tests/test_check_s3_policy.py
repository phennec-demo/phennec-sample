import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from check_s3_policy import check  # noqa: E402

EXAMPLE = pathlib.Path(__file__).resolve().parents[1] / "examples" / "aws" / "s3-readonly-policy.json"


def policy(*statements):
    return {"Version": "2012-10-17", "Statement": list(statements)}


class CheckS3PolicyTest(unittest.TestCase):
    def test_example_policy_is_ok(self):
        self.assertEqual(check(json.loads(EXAMPLE.read_text()), "YOUR-BUCKET-NAME"), [])

    def test_write_action_is_reported(self):
        p = policy({"Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::b/*"})
        self.assertEqual(len(check(p, "b")), 1)

    def test_wildcard_action_is_reported(self):
        p = policy({"Effect": "Allow", "Action": "s3:*", "Resource": "*"})
        self.assertEqual(len(check(p, "b")), 1)

    def test_other_bucket_is_reported(self):
        p = policy({"Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::other/*"})
        self.assertEqual(len(check(p, "b")), 1)

    def test_deny_statements_are_ignored(self):
        p = policy({"Effect": "Deny", "Action": "s3:*", "Resource": "*"})
        self.assertEqual(check(p, "b"), [])


if __name__ == "__main__":
    unittest.main()
