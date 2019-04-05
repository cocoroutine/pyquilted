import unittest
from pyquilted.builder.section_factory import SectionOptions


class TestSectionOptions(unittest.TestCase):
    def setUp(self):
        self.options = SectionOptions()
        self.options_compact = SectionOptions(heading_compact=True)
        self.options_expanded = SectionOptions(heading_expanded=True)
        self.options_both = SectionOptions(heading_compact=True, 
                                           heading_expanded=True)
        self.options_table = SectionOptions(skills_table=True)

    def test_section_options_default(self):
        self.assertTrue(hasattr(self.options, 'heading'))
        self.assertTrue(hasattr(self.options, 'skills_table'))

        self.assertEqual(self.options.heading, 'auto')
        self.assertFalse(self.options.skills_table)

    def test_section_options_compact(self):
        self.assertEqual(self.options_compact.heading, 'compact')

    def test_section_options_expanded(self):
        self.assertEqual(self.options_expanded.heading, 'complex')

    def test_section_options_both(self):
        self.assertEqual(self.options_both.heading, 'complex')

    def test_section_options_skills_table(self):
        self.assertTrue(self.options_table.skills_table)


if __name__ == '__main__':
    unittest.main()
