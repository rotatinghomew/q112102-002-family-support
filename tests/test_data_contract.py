import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'messages': ['item', 'origin', 'source', 'text', 'at', 'replaces'], 'history': ['item', 'old_destination', 'accepted_at'], 'labels': ['item', 'review', 'actual', 'confirmed_on'], 'audit_strata': ['month', 'source', 'probability'], 'loss': ['actual', 'destination', 'cost'], 'maturity': ['minimum_label_days', 'max_review_minutes'], 'policy': ['max_risk', 'minimum_random_per_source'], 'intake': ['item', 'source', 'text', 'priority', 'arrive', 'deadline'], 'review_slots': ['slot', 'staff', 'categories', 'start', 'end', 'urgent_only'], 'commitments': ['id', 'item', 'status', 'assignment', 'at'], 'new_facts': ['id', 'kind', 'target', 'value', 'at']}


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
