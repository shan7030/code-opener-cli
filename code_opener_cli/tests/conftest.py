import pytest

@pytest.fixture(scope="package")
def config_with_project():
    return {"default_editor": "code .", "projects": [{'project_name':'abc','path':'/abc/def/test'}]}

@pytest.fixture(scope="package")
def config_with_no_project():
    return {"default_editor": "code .", "projects": []}
