import pytest
import dictppr


class TestPPrintFunction:

    def test_pprint_empty(self, capfd):
        dictionary = {}
        dictppr.pprint(dictionary)
        printed, _ = capfd.readouterr()
        expected = "\n"
        assert printed == expected

    def test_pprint_flat(self, capfd):
        dictionary = {
            "key_1": "val_1",
            "key_2": "val_2"
        }
        dictppr.pprint(dictionary)
        printed, _ = capfd.readouterr()
        expected = "key_1 => val_1\n" \
                   "key_2 => val_2\n"
        assert printed == expected

    def test_pprint_nested_once(self, capfd):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3"
            }
        }
        dictppr.pprint(dictionary)
        printed, _ = capfd.readouterr()
        expected = "key_1 => val_1\n" \
                   "key_2 => val_3\n"
        assert printed == expected

    def test_pprint_nested_multiple(self, capfd):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3",
                "key_4": "val_4"
            }
        }
        dictppr.pprint(dictionary)
        printed, _ = capfd.readouterr()
        expected = "key_1 => val_1\n" \
                   "key_2 => key_3:val_3, key_4:val_4\n"
        assert printed == expected
