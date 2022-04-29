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
