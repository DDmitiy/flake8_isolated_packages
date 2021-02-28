import pytest


@pytest.fixture
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
def root_module_filename() -> str:
    return


@pytest.fixture()
def common_module_filename() -> str:
    return


@pytest.fixture()
def service_module_filename() -> str:
    return
