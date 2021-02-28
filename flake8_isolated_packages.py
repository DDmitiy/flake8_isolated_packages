import ast
import sys
from typing import Any, Generator, List, Optional, Tuple, Type

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


MESSAGE = 'FIP100: You try to import from isolated package'


class Visitor(ast.NodeVisitor):
    def __init__(self, filename: str, isolated_packages: List[str], test_folders: List['str']) -> None:
        self.package_name = self._get_package_name(filename)
        self.errors: List[Tuple[int, int]] = []
        self.isolated_packages = isolated_packages
        self.test_folders = test_folders

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if self.package_name in self.test_folders:
            self.generic_visit(node)
            return

        root_import_package_name = node.module.split('.')[0]
        if (root_import_package_name in self.isolated_packages
                and root_import_package_name != self.package_name):
            self.errors.append((node.lineno, node.col_offset))

        self.generic_visit(node)

    @staticmethod
    def _get_package_name(filename) -> Optional[str]:
        split_filepath = filename.split('/')
        if len(split_filepath) < 2:
            return None
        package_name = split_filepath[1]
        if package_name.endswith('.py'):
            return None
        return package_name


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    isolated_packages_option_name = 'isolated_packages'
    test_folders_option_name = 'test_folders'

    @classmethod
    def add_options(cls, parser):
        """Required by flake8
        add the possible options, called first
        Args:
            parser (OptionsManager):
        """
        kwargs = {'action': 'store', 'parse_from_config': True,
                  'comma_separated_list': True}
        parser.add_option(
            f'-{cls.isolated_packages_option_name}',
            f'--{cls.isolated_packages_option_name}',
            default='',
            **kwargs
        )
        parser.add_option(
            f'-{cls.test_folders_option_name}',
            f'--{cls.test_folders_option_name}',
            default='tests',
            **kwargs
        )

    @classmethod
    def parse_options(cls, options):
        """Required by flake8
        parse the options, called after add_options
        Args:
            options (dict): options to be parsed
        """
        cls._isolated_packages = getattr(options, cls.isolated_packages_option_name)
        cls._test_folders = getattr(options, cls.test_folders_option_name)

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self._filename = filename
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Any module from specified package could not be import in another package
        """
        visitor = Visitor(self._filename, self._isolated_packages, self._test_folders)
        visitor.visit(self._tree)
        for line, col in visitor.errors:
            yield line, col, MESSAGE, type(self)
