from pyquilted.builder.contacts import ContactsMapper
from pyquilted.builder.education import EducationMapper
from pyquilted.builder.heading import HeadingMapper
from pyquilted.builder.projects import ProjectsMapper
from pyquilted.builder.skills import SkillsMapper
from pyquilted.builder.work import WorkMapper


class SectionMapper:
    """A data mapper object for all sections"""
    def __init__(self, key, section_odict, options=None):
        self.key = key
        self.section_odict = section_odict
        self.options = options or SectionOptions()
        self.mapper = None
        self.section = None

    def create_section(self):
        self._create_mapper()
        self.section = self.mapper.deserialize()
        return self.section

    def _create_mapper(self):
        if self.key in 'contacts':
            self.mapper = ContactsMapper(self.section_odict)
        elif self.key in 'education':
            self.mapper = EducationMapper(self.section_odict)
        elif self.key in 'heading':
            self.mapper = HeadingMapper(self.section_odict)
        elif self.key in 'projects':
            self.mapper = ProjectsMapper(self.section_odict)
        elif self.key in 'skills':
            self.mapper = SkillsMapper(self.section_odict)
        elif self.key in 'work':
            self.mapper = WorkMapper(self.section_odict)


class SectionOptions:
    """section builder options for the formatting of the sections"""
    def __init__(self, heading=None, **kwargs):
        self.heading = heading or "auto"
