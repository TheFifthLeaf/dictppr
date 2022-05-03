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

    def test_pprint_nested_hard(self, capfd):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3",
                "key_4": {
                    "key_5": "val_5",
                    "key_6": "val_6",
                    "key_7": ["val_7.1", "val_7.2", "val_7.3", "val_7.4"]
                }
            },
            "key_8": ["val_8", "val_9"],
            "key_10": ["val_10"]
        }
        dictppr.pprint(dictionary)
        printed, _ = capfd.readouterr()
        expected = "key_1  => val_1\n" \
                   "key_2  => key_3:val_3, key_4:[key_5:val_5, key_6:val_6, key_\n" \
                   "          7:[val_7.1, val_7.2, val_7.3, val_7.4]]\n" \
                   "key_8  => val_8, val_9\n" \
                   "key_10 => val_10\n"
        assert printed == expected
