from os.path import exists

from dbbot import CommandLineOptions


class WriterOptions(CommandLineOptions):

    @property
    def output_file_path(self):
        return self._options.output_file_path

    def _add_parser_options(self):
        super(WriterOptions, self)._add_parser_options()
        self._parser.add_option('-o', '--output',
            dest='output_file_path',
            help='test summary html file',
        )

    def _get_validated_options(self):
        options = super(WriterOptions, self)._get_validated_options()
        if not options.output_file_path:
            self._parser.error('output html filename required')
        if not exists(options.db_file_path):
            self._parser.error('database %s not exists' % options.db_file_path)
        return options
