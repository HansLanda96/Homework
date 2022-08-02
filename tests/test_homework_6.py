from unittest import TestCase, main
from homework_6.task_1 import key_value_connect


class TestKeyValueConnect(TestCase):
    def test_key_value_connects(self):
        self.assertEqual(key_value_connect(
            ('key1', 'key2', 'key3'), ('val1', 'val2', 'val3')),
            {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
        )

    def test_key_value_connects_tuple(self):
        with self.assertRaises(TypeError) as e:
            key_value_connect('key1', 'val1')
        self.assertEqual("Key and value must be tuples", e.exception.args[0])

    def test_key_value_connects_with_different_length_keys(self):
        with self.assertRaises(ValueError) as e:
            key_value_connect(('key1', 'key2'), ('val1', 'val2', 'val3'))
        self.assertEqual("Key and value must be the same length", e.exception.args[0])

    def test_key_value_connects_with_different_length_values(self):
        with self.assertRaises(ValueError) as e:
            key_value_connect(('key1', 'key2', 'key3'), ('val1', 'val2'))
        self.assertEqual("Key and value must be the same length", e.exception.args[0])


if __name__ == '__main__':
    main()
