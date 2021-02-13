"""
Main file for the package
"""
import os
import typer
import json
from code_opener_cli.utils.helpers import JsonDataOperations
from code_opener_cli import __version__
from typing import Optional

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo(f"Code Opener CLI Version: {__version__}")
        raise typer.Exit()

def list_projects(incomplete: str):
    current_config = JsonDataOperations.read()
    project_name_list = []
    for project_item in current_config['projects']:
        if project_item['project_name'].startswith(incomplete):
            project_name_list.append(project_item['project_name'])
    return project_name_list

@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context,version: Optional[bool] = typer.Option(None, "--version", callback=version_callback)):
    """
    CLI to handle your projects and Editors smartly
    """
    if ctx.invoked_subcommand is None:
        typer.echo("Hi, Welcome to Code Opener CLI 😀")
        command = typer.style("copen --help", bg=typer.colors.BRIGHT_WHITE,fg=typer.colors.BLACK)
        typer.echo('Use ' +command + ' to get help with commands')
    
@app.command()
def add(project_name:str =  typer.Option(...,"--project-name","-pn",prompt=True,metavar="Name by which you like to call this project 🥺")):
    """
    Add a project with PROJECT_NAME
    """
    path = os.getcwd()
    current_config = JsonDataOperations.read()
    
    for project_item in current_config['projects']:
        if project_item['project_name']==project_name:
            echo_text = typer.style("Project with this name already present!",
             bg=typer.colors.RED,fg=typer.colors.WHITE)
            typer.echo(echo_text, err=True)
            raise typer.Exit(code=1)
            
    current_config['projects'].append({'project_name':project_name, 'path':path})
    JsonDataOperations.update(current_config)
    typer.secho("Project added successfully!!", fg=typer.colors.BRIGHT_GREEN)

@app.command()
def see():
    """
    See list of all projects that are added
    """
    current_config = JsonDataOperations.read()
    if len(current_config['projects'])==0:
        typer.echo('Seems like you have not added any project yet!!!')
        command = typer.style("copen add", bg=typer.colors.BRIGHT_WHITE,fg=typer.colors.BLACK)
        typer.echo('Use ' +command + ' to add new project')
        raise typer.Exit()

    col = typer.style("Project Name",fg=typer.colors.CYAN, bold=True)
    typer.echo(col)
    typer.echo("=======================")
    for project_item in current_config['projects']:
        typer.echo(project_item['project_name'])
    typer.echo("=======================")

@app.command()
def open(project_name:str =  typer.Argument(...,autocompletion=list_projects,metavar="Project Name which you used while adding 🥺")):
    """
    Opens a Project with PROJECT_NAME
    """
    current_config = JsonDataOperations.read()
    found = False
    for project_item in current_config['projects']:
        if project_item['project_name']==project_name:
            found = typer.style("Project Found!", fg=typer.colors.GREEN, bold=True)
            typer.echo(found)
            os.chdir(project_item['path'])
            os.system(current_config['default_editor'])
            found = True
            break

    if found == False:
        echo_text = project_name + ": Project Not Found!"
        not_found = typer.style(echo_text, fg=typer.colors.RED, bold=True)
        typer.echo(not_found,  err=True)
        command = typer.style("copen add", bg=typer.colors.BRIGHT_WHITE,fg=typer.colors.BLACK)
        typer.echo('Use ' +command + ' to add new project')
        raise typer.Exit()

@app.command()
def remove(project_name:str = typer.Option(...,"--project-name","-pn",autocompletion=list_projects,prompt=True,confirmation_prompt=True,metavar="Project Name which you used while adding 🥺")):
    """
    Removes a project with specified PROJECT_NAME
    """
    current_config = JsonDataOperations.read()
    index = -1
    found = False
    for project_item in current_config['projects']:
        index += 1
        if project_item['project_name']==project_name:
            current_config['projects'].pop(index)
            found = True
            JsonDataOperations.update(current_config)
            break

    if found==False:
        echo_text = typer.style("Project with this name is not present!",
             bg=typer.colors.RED,fg=typer.colors.WHITE)
        typer.echo(echo_text, err=True)
    else:
        typer.secho('Removed Successfully!',fg= typer.colors.BRIGHT_GREEN)