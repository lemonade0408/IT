import unittest
from unittest.mock import patch
from timer import measure_time


class TestMeasureTime(unittest.TestCase):

    def test_result_and_time(self):
        @measure_time
        def add(a, b):
            return a + b

        with patch("timer.time.perf_counter", side_effect=[1.0, 1.5]):
            with patch("builtins.print") as printed:
                result = add(2, 3)

        self.assertEqual(result, 5)
        printed.assert_called_once()
        self.assertIn("0.5", str(printed.call_args))

    def test_error(self):
        @measure_time
        def broken():
            raise ValueError("Test error")

        with patch("timer.time.perf_counter", side_effect=[1.0, 1.5]):
            with patch("builtins.print") as printed:
                with self.assertRaises(ValueError):
                    broken()

        printed.assert_called_once()


if __name__ == "__main__":
    unittest.main()