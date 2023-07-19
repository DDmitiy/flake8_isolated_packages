import pytest


@pytest.fixture()
def import_from_common_module() -> str:
    return 'from common import function'


@pytest.fixture()
def import_from_nested_common_module() -> str:
    return 'from common.utils import function'


@pytest.fixture()
def import_from_service_module() -> str:
    return 'from service import function'


@pytest.fixture()
def import_from_nested_service_module() -> str:
    return 'from service.utils import function'


@pytest.fixture()
def local_import():
    return 'from .utils import function'


@pytest.fixture()
def import_from_dot():
    return 'from . import function'
