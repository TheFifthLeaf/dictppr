import pytest
import dictppr


class TestConvertFunction:

    def test_convert_empty(self):
        dictionary = {}
        converted = dictppr.convert(dictionary)
        expected = dictionary
        assert converted == expected
        assert isinstance(converted, dict)

    def test_convert_flat(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": "val_2"
        }
        converted = dictppr.convert(dictionary)
        expected = dictionary
        assert converted == expected
        assert isinstance(converted, dict)

    def test_convert_nested_once(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3"
            }
        }
        converted = dictppr.convert(dictionary)
        expected = {"key_1": "val_1", "key_2": "val_3"}
        assert converted == expected
        assert isinstance(converted, dict)

    def test_convert_nested_multiple(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3",
                "key_4": "val_4"
            }
        }
        converted = dictppr.convert(dictionary)
        expected = {"key_1": "val_1", "key_2": "key_3:val_3, key_4:val_4"}
        assert converted == expected
        assert isinstance(converted, dict)

    def test_convert_nested_hard(self):
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
        converted = dictppr.convert(dictionary)
        expected = {
            "key_1": "val_1",
            "key_2": "key_3:val_3, key_4:[key_5:val_5, key_6:val_6, "
                     "key_7:[val_7.1, val_7.2, val_7.3, val_7.4]]",
            "key_8": "val_8, val_9",
            "key_10": "val_10"
        }
        assert converted == expected
        assert isinstance(converted, dict)
