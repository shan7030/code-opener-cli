"""
Main file for the package
"""

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
def add(project_name:str =  typer.Option(...,prompt=True), path: str = typer.Option(...,prompt=True)):
    """
    Add the project to the list of projects
    """
    JsonDataOperations.create()