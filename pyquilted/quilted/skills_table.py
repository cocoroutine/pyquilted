from pyquilted.quilted.table import Table
from pyquilted.quilted.section import Section


class SkillsTable(Section):
    """The skills section in a quilted resume

       The skills object is a compact section that is a comma separated
       list of strings describing your skills. As a section it mixes in
       the sectionable functionality.
    """
    def __init__(self, skills, icon=None, cols=4, default=""):
        self.label = 'Skills'
        self.icon = icon or "fa-wrench"
        self.rows = Table(cols=cols, default=default).build(skills)
        self.compact = False
