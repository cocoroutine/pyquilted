from pyquilted.quilted.skills import Skills
from pyquilted.quilted.skills_table import SkillsTable


class SkillsBuilder:
    """Skills data mapper object"""
    def __init__(self, skills_odict, table=False):
        self.odict = list(skills_odict)
        self.table = table

    def deserialize(self):
        if self.table:
            skills = SkillsTable(self.odict)
        else:
            skills = Skills(self.odict)
        return skills
