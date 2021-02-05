"""
Main file for the package
"""
import os
import typer
import json
from code_opener_cli.utils.helpers import JsonDataOperations

app = typer.Typer()

@app.callback()
def callback():
    """
    CLI to handle your projects and Editors smartly
    """
    
    
@app.command()
def add(project_name:str =  typer.Option(...,prompt=True)):
    """
    Add the project to the list of projects
    """
    path = os.getcwd()
    if JsonDataOperations.present():
        current_config = JsonDataOperations.read()
        current_config['projects'].append({'project_name':project_name, 'path':path})
        JsonDataOperations.update(current_config)
    else:
        JsonDataOperations.create()


@app.command()
def read():
    """
    Add the project to the list of projects
    """
    if JsonDataOperations.present():
        print(JsonDataOperations.read())
    else:
        JsonDataOperations.create()
