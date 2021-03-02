import ast
from typing import List

import pytest

from flake8_isolated_packages import Plugin

ERROR_CODE = 'FIP100'
ROOT_MODULE_FILENAME = './utils.py'
COMMON_MODULE_FILENAME = './common/utils.py'
SERVICE_MODULE_FILENAME = './service/utils.py'
TEST_MODULE_FILENAME = './tests/conftest.py'


def _result(loc: str, filename: str) -> List[str]:
    tree = ast.parse(loc)
    plugin = Plugin(tree, filename)
    plugin._isolated_packages = ['service']
    plugin._test_folders = ['tests']
    return [f'{line}:{col} {message}' for line, col, message, _ in plugin.run()]


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, False),
        (COMMON_MODULE_FILENAME, False),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_import_from_common_module(import_from_common_module, filename, has_error):
    check_res = _result(import_from_common_module, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, False),
        (COMMON_MODULE_FILENAME, False),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_import_from_nested_common_module(import_from_nested_common_module, filename, has_error):
    check_res = _result(import_from_nested_common_module, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, True),
        (COMMON_MODULE_FILENAME, True),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_import_from_service_module(import_from_service_module, filename, has_error):
    check_res = _result(import_from_service_module, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, True),
        (COMMON_MODULE_FILENAME, True),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_import_from_nested_service_module(import_from_nested_service_module, filename, has_error):
    check_res = _result(import_from_nested_service_module, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, False),
        (COMMON_MODULE_FILENAME, False),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_local_import(local_import, filename, has_error):
    check_res = _result(local_import, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res


@pytest.mark.parametrize(
    'filename, has_error', [
        (ROOT_MODULE_FILENAME, False),
        (COMMON_MODULE_FILENAME, False),
        (SERVICE_MODULE_FILENAME, False),
        (TEST_MODULE_FILENAME, False),
    ]
)
def test_import_from_dot(import_from_dot, filename, has_error):
    check_res = _result(import_from_dot, filename)
    if has_error:
        assert len(check_res) == 1
        assert ERROR_CODE in check_res[0]
    else:
        assert not check_res
