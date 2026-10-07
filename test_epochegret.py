import datetime as d,unittest
import epochegret as e
class EpochTests(unittest.TestCase):
    def test_zero(self):self.assertEqual(e.report(e.from_epoch('0'))['utc_iso'],'1970-01-01T00:00:00.000000Z')
    def test_seconds(self):self.assertEqual(e.report(e.from_epoch('86400'))['epoch_seconds'],86400)
    def test_ms(self):self.assertEqual(e.report(e.from_epoch('1234','ms'))['epoch_milliseconds'],1234)
    def test_negative(self):self.assertEqual(e.report(e.from_epoch('-1','ms'))['utc_iso'],'1969-12-31T23:59:59.999000Z')
    def test_unrepresentable(self):self.assertIsNone(e.report(e.from_epoch('1','ms'))['epoch_seconds'])
    def test_micro(self):r=e.report(e.parse_iso('1970-01-01T00:00:00.000001Z'));self.assertEqual(r['epoch_microseconds'],1);self.assertIsNone(r['epoch_milliseconds'])
    def test_offset(self):self.assertEqual(e.report(e.parse_iso('1970-01-01T01:00:00+01:00'))['epoch_seconds'],0)
    def test_leap(self):self.assertEqual(e.parse_iso('2024-02-29T00:00:00Z').day,29)
    def test_bad_date(self):
        with self.assertRaises(ValueError):e.parse_iso('2025-02-29T00:00:00Z')
    def test_naive(self):
        with self.assertRaises(ValueError):e.parse_iso('1970-01-01T00:00:00')
    def test_bad_offset(self):
        with self.assertRaises(ValueError):e.parse_iso('1970-01-01T00:00:00+00:99')
    def test_leap_second(self):
        with self.assertRaises(ValueError):e.parse_iso('1970-01-01T00:00:60Z')
    def test_numeric_only(self):
        for x in ('1.2','1e5','x','١'):
            with self.assertRaises(ValueError):e.from_epoch(x)
    def test_overflow(self):
        with self.assertRaises(OverflowError):e.from_epoch('999999999999999999')
    def test_precision_limit(self):
        with self.assertRaises(ValueError):e.parse_iso('1970-01-01T00:00:00.1234567Z')
    def test_unit(self):
        with self.assertRaises(ValueError):e.from_epoch('1','m')
    def test_naive_report(self):
        with self.assertRaises(ValueError):e.report(d.datetime(1970,1,1))
if __name__=='__main__':unittest.main()
