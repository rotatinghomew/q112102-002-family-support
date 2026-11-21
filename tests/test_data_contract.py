import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'risk_facts': ['app', 'person', 'purpose', 'started', 'deadline', 'population'], 'sessions': ['session', 'app', 'channel', 'opened'], 'continuations': ['from_session', 'to_session', 'state', 'recognized_on'], 'visibility': ['channel', 'step', 'start', 'end', 'observable'], 'actions': ['session', 'step', 'state', 'at'], 'received': ['proof', 'app', 'kind', 'issuer', 'valid_until', 'signed_on', 'void_on'], 'permitted': ['edition', 'from_date', 'population', 'purpose', 'kind', 'issuer'], 'proposals': ['proposal', 'action', 'step', 'alternate', 'population'], 'adoptions': ['proposal', 'confirmed_on', 'effective_on', 'population']}


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
