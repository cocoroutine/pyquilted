import unittest
from pyquilted.builder.section_factory import SectionOptions


class TestSectionOptions(unittest.TestCase):
    def setUp(self):
        self.options_default = SectionOptions()
        self.options = SectionOptions(heading='compact', skills_table=True)

    def test_section_options_default(self):
        self.assertTrue(hasattr(self.options_default, 'heading'))
        self.assertTrue(hasattr(self.options_default, 'skills_table'))

        self.assertEqual(self.options_default.heading, 'auto')
        self.assertEqual(self.options_default.skills_table, False)

    def test_section_options(self):
        self.assertEqual(self.options.heading, 'compact')
        self.assertTrue(self.options.skills_table)


if __name__ == '__main__':
    unittest.main()
