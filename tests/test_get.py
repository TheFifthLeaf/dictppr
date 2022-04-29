import pytest
import dictppr


class TestGetFunction:

    def test_get_empty(self):
        dictionary = {}
        converted = dictppr.get(dictionary)
        expected = ""
        assert converted == expected
        assert isinstance(converted, str)

    def test_get_flat(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": "val_2"
        }
        converted = dictppr.get(dictionary)
        expected = "key_1:val_1, key_2:val_2"
        assert converted == expected
        assert isinstance(converted, str)

    def test_get_nested_once(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3"
            }
        }
        converted = dictppr.get(dictionary)
        expected = "key_1:val_1, key_2:val_3"
        assert converted == expected
        assert isinstance(converted, str)

    def test_get_nested_multiple(self):
        dictionary = {
            "key_1": "val_1",
            "key_2": {
                "key_3": "val_3",
                "key_4": "val_4"
            }
        }
        converted = dictppr.get(dictionary)
        expected = "key_1:val_1, key_2:key_3:val_3, key_4:val_4"
        assert converted == expected
        assert isinstance(converted, str)
