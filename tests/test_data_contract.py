import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'regions': ['period', 'area', 'eligible_upper'], 'overlap': ['period', 'area', 'abc', 'people', 'verified', 'reported_on'], 'dependence': ['period', 'area', 'sources', 'basis'], 'address_frame': ['period', 'area', 'frame', 'dwelling', 'independent'], 'sample_plan': ['period', 'area', 'dwelling', 'probability', 'frozen_on'], 'observations': ['id', 'dwelling', 'state', 'observed_on', 'reported_on'], 'access_windows': ['dwelling', 'start', 'end'], 'staff_slots': ['slot', 'start', 'end', 'areas'], 'commitments': ['id', 'slot', 'dwelling', 'notified_on'], 'changes': ['id', 'kind', 'target', 'at'], 'policy': ['area', 'minimum_independent_interviews', 'minimum_missing_share'], 'adjustments': ['id', 'area', 'effective_period', 'extra_slots', 'confirmed_on', 'evidence_cutoff']}


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
