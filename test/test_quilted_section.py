import unittest
from pyquilted.quilted.section import Section


class MockCompound(Section):
    def __init__(self):
        self.one = 1


class Mock(Section):
    def __init__(self):
        self.one = 1


class TestSection(unittest.TestCase):
    def test_kebab(self):
        mock = Mock()
        self.assertEqual(mock._kebab_name(), 'mock')

    def test_kebab_compound(self):
        mock = MockCompound()
        self.assertEqual(mock._kebab_name(), 'mock-compound')

    def test_serialize(self):
        mock = MockCompound()
        self.assertTrue(isinstance(mock.serialize(), dict))

if __name__ == '__main__':
    unittest.main()
