# Code Opener CLI ⌨️

The command line interface to add any project as favorite and open it from anywhere using just one command. Use `copen add` to add and `copen open <project_name>` to open and . See commands to get idea on more things supported by Code Opener CLI 

# Commands

## See Lists of Projects Added 

```
copen see
``` 

## Add a Project

- <b> Method 1 : </b> 
    1. Adding Project just requires you to go to project using `cd` for the first time and type command <br>
    `copen add` 

    ```
    cd path/to/your/project
    copen add
    ```
    2. This will ask for project name, give any nick name to project which is handy to you and press Enter.
    <br>
    Done :smile:, now you can open this project from anywhere . 

- <b> Method 2 : </b> 
        You can also directly add using one of the following single command :
    1. Using short name `-pn` :
        ```
        copen add -pn <project_name>
        ```
    2. Using defualt Option name :
        ```
        copen add --project-name <project_name>
        ```


## Open a Project

After a project is added , you can easily open it from anywhere using this command . Remember that project_name is the name/nick name that you gave to your project .

```
 copen open <project_name>
```


## Remove a Project

- <b> Method 1 :</b>
    1. Removing Project is very easy using 
    ```
    copen remove
    ```
    2. This will ask you for the project name and confirmation.

- <b> Method 2 :</b>
    You can also directly remove using one of the following single command :
    1. Using short name `-pn` :
        ```
        copen remove -pn <project_name>
        ```
    2. Using defualt Option name :
        ```
        copen remove --project-name <project_name>
        ```

## Other handy commands 

- `copen` : Will display welcome message
- `copen --help` : Provides list of commands
- `copen <add/remove/see/open> --help` : Provides you help for particular command
- `copen --version` : Provides you the version of code-opener-cli

## Contributing to Project

Let's take this project to next level together 🎉 You can find the guidelines to contribute to this project [here](https://github.com/shan7030/code-opener-cli/blob/master/CONTRIBUTING.md).

## Changelogs

All notable changes to this projects can be found in [CHANGELOG.md](https://github.com/shan7030/code-opener-cli/blob/master/CHANGELOG.md) .
Currently, this CLI supports on VSCode, but support for other code editors/IDE's will be added soon :smile: .