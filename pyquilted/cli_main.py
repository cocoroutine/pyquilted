import argparse
from pyquilted import __version__
from pyquilted.app_factory import AppFactory


class CliMain:
    """Command Line Inteface for pyquilted"""
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                prog='pyquilted',
                description="pyquilted --pdf input.yml output.pdf")
        self._args_pyquilted()
        self._args_section()
        self._args_style()

    def _args_pyquilted(self):
        self.parser.add_argument('-v', '--version', action='version',
                                 version='%(prog)s ' + __version__)
        self.parser.add_argument('-p', '--pdf', metavar=('yml', 'pdf'),
                                 nargs=2, dest='pdf',
                                 help="print resume to pdf")
        self.parser.add_argument('-H', '--html', metavar=('yml', 'html'),
                                 nargs=2, dest='html',
                                 help="print resume to html")
        self.parser.add_argument('-s', '--sample', metavar='yml',
                                 dest='sample',
                                 help="generate sample resume in yaml")

    def _args_section(self):
        section_group = self.parser.add_argument_group('section formatting')
        section_group.add_argument(
                '--heading-compact', dest='heading_compact',
                default=False, action='store_true',
                help="use a compact heading format defaults to auto")

        section_group.add_argument(
                '--heading-expanded', dest='heading_expanded',
                default=False, action='store_true',
                help="use an expanded heading format defaults to auto")

        section_group.add_argument('--skills-table', dest='skills_table',
                                   default=False, action='store_true',
                                   help="use a skills table to show "
                                        "many skills")

        section_group.add_argument('--no-sorting', dest='sorting',
                                   default=True, action='store_false',
                                   help="disable sorting skills "
                                   "alphabetically")

        section_group.add_argument('--no-grouping', dest='grouping',
                                   default=True, action='store_false',
                                   help="disable grouping of compact sections")

    def _args_style(self):
        style_group = self.parser.add_argument_group(
                'style', 'css styles to apply to resume content')
        style_group.add_argument('--color', metavar='"color|#rgb"',
                                 dest='name_color',
                                 help="css color code for your name")
        style_group.add_argument('--font', metavar='"font"', dest='font_main',
                                 help="css font for resume content")
        style_group.add_argument('--font-other', metavar='"font"',
                                 dest='font_other',
                                 help="css font override for heading/contacts")
        style_group.add_argument('--font-size', metavar='"size"',
                                 dest='font_size',
                                 help="css font size for resume content")

    def run(self):
        app = self._create_app()
        if app:
            app.run()
        else:
            self.parser.print_help()

    def _create_app(self):
        args = self.parser.parse_args()
        return AppFactory(args).create()
