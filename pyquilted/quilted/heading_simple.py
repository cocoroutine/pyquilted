class HeadingSimple:
    """The heading section located at the top of a quilted resume

       A simple heading format that is centered and contains at most 3
       items. It supports title, location and flair. Objectives cannot
       be used in a simple heading.
    """
    def __init__(self, name=None, adjacent=None, primary=None):
        self.name = name
        self.adjacent = adjacent
        self.primary = primary

    def serialize(self):
        section = dict()
        section['heading-simple'] = vars(self)
        return section
