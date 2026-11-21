import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'plans': ['need', 'resident', 'kind', 'unit', 'required', 'start', 'end'], 'authorizations': ['id', 'need', 'agency', 'start', 'end', 'proxy'], 'referrals': ['id', 'need', 'agency', 'state', 'at'], 'segments': ['id', 'worker', 'agency', 'start', 'end'], 'shares': ['id', 'segment', 'need', 'fraction', 'amount', 'proof', 'primary'], 'funds': ['fund', 'scope', 'start', 'end', 'month_limit_minutes', 'backfill_for'], 'changes': ['id', 'action', 'subject', 'replacement', 'at'], 'payments': ['id', 'share', 'fund', 'kind', 'minutes', 'prior', 'at']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
