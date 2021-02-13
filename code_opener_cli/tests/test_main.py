import os
from typer.testing import CliRunner

from code_opener_cli.main import app
from code_opener_cli.utils.helpers import JsonDataOperations

runner = CliRunner()

def test_see_with_no_projects(monkeypatch, config_with_no_project):
    """
    Test reading the lists of projects, when there is not project Added
    """
    def mock_read():
        return config_with_no_project

    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    result = runner.invoke(app, ["see"])
    assert result.exit_code == 0
    assert "Seems like you have not added any project yet!!!" in result.stdout 


def test_see_with_projects(monkeypatch, config_with_project):
    """
    Test reading the lists of projects, when there is atleast one project
    """
    def mock_read():
        return config_with_project

    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    result = runner.invoke(app, ["see"])
    assert result.exit_code == 0
    assert "Project Name" in result.stdout
    assert "abc" in result.stdout 
    assert "Seems like you have not added any project yet!!!" not in result.stdout 

def test_add_new_project(monkeypatch, config_with_project):
    """
    Test adding new project when the project name is not already present
    """
    def mock_read():
        return config_with_project

    def mock_update(config_data):
        return None

    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    monkeypatch.setattr(JsonDataOperations, 'update', mock_update)

    result = runner.invoke(app, ["add"],input="test-name")
    assert result.exit_code == 0
    assert "Project added successfully!!" in result.stdout

def test_add_present_project(monkeypatch, config_with_project):
    """
    Test adding new project when the project name is already present
    """
    def mock_read():
        return config_with_project

    def mock_update(config_file):
        return None

    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    monkeypatch.setattr(JsonDataOperations, 'update', mock_update)

    result = runner.invoke(app, ["add"],input="abc")
    assert result.exit_code == 1
    assert "Project with this name already present!" in result.stdout

def test_open_project_not_present(monkeypatch, config_with_project):
    """
    Test opening the project when the project name is not present
    """
    def mock_read():
        return config_with_project
    
    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    result = runner.invoke(app, ["open", "test_project"])
    assert result.exit_code == 0
    assert "Project Not Found!" in result.stdout

def test_open_project_present(monkeypatch, config_with_project):
    """
    Test opening the project when the project name is present
    """
    def mock_read():
        return config_with_project
    
    def mock_os_sytem(command):
        return None
    
    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    monkeypatch.setattr(os, 'system', mock_os_sytem)

    result = runner.invoke(app, ["open", "abc"])
    assert result.exit_code == 0
    assert "Project Not Found!" not in result.stdout
    assert "Project Found!" in result.stdout

def test_remove_not_present_project(monkeypatch, config_with_project):
    """
    Test removing the project when the project is not already added
    """
    def mock_read():
        return config_with_project
    
    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)

    result = runner.invoke(app, ["remove"], input="test_project\ntest_project\n")
    assert result.exit_code == 0
    assert "Project with this name is not present!" in result.stdout

def test_remove_project_present(monkeypatch, config_with_project):
    """
    Test removing the project when the project is present
    """
    def mock_read():
        return config_with_project
    
    def mock_update(config_data):
        return None
    
    monkeypatch.setattr(JsonDataOperations, 'read', mock_read)
    monkeypatch.setattr(JsonDataOperations, 'update', mock_update)

    result = runner.invoke(app, ["remove"], input="abc\nabc\n")
    assert result.exit_code == 0
    assert "Removed Successfully!" in result.stdout

