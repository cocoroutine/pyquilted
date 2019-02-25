from pyquilted.mapper.heading_details import HeadingDetailsMapper
from pyquilted.quilted.heading_simple import HeadingSimple


class HeadingMapper:
    """Heading data mapper object"""
    def __init__(self, odict):
        self.heading = HeadingDetailsMapper(odict).deserialize()
        self.section = None

    def deserialize(self):
        if self.heading.objective or len(self.heading.details) > 2:
            self._build_heading_complex()
        else:
            self._build_heading_simple()
        return self.section

    def _build_heading_complex(self):
        pass

    def _build_heading_simple(self):
        if len(self.heading.details) == 2:
            self.section = HeadingSimple(name=self.heading.name,
                                         adjacent=self.heading.details[0],
                                         primary=self.heading.details[1])
        elif len(self.heading.details) == 1:
            self.section = HeadingSimple(name=self.heading.name,
                                         primary=self.heading.details[0])
        else:
            self.section = HeadingSimple(name=self.heading.name)
