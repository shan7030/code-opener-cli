# CONTRIBUTING 

## References / Pre-requisites
- Code opener CLI uses [Typer](https://typer.tiangolo.com/), which is package used to build great CLI's 
- Code opener CLI package is build using [Poetry](https://python-poetry.org/), which makes Python packaging and dependency management easy

## Development setup

1. In order to start, Fork the project (You can also star it if you liked it 🌟)
2. Install poetry from [here](https://python-poetry.org/docs/#installation) or simply using `pip install poetry` 
3. Clone the Forked repo and go inside the project using `cd code-opener-cli`
4. Install all dependencies using `poetry install`(This will also create Virtual env)
5. Check whether the virtual env is created using `poetry env info`
6. Change the virtual env using `poetry env use /path`. You will get `/path` using the `poetry env info --path` or `poetry env info`. In case if this dosen't work you can change the interpreter path with above path.
7. Now, you can start the development, also don't forget to create an Issue [here](https://github.com/shan7030/code-opener-cli/issues) before starting work on anything

## Verifying the Developmental Changes

1. Use `poetry install` to install the package locally inside your Virtual Environment
2. Test locally whether your package works correctly.
3. Create wheel package using `poetry build`
4. Test the wheel using `pip install --user /path/to/wheel/file/inside/dist`
5. Make sure you have written tests for the new code added
6. Also correct the previously broken test case if any . I have used pytest so you can use `pytest` to run tests
7. Now you can create a PR 😅

Thank you for your contributions 😊

## Coding Standards

1. Currently the project dosen't use any linter, which will be added soon, but till then make sure you add comments to each file, function, class or any where it is required
2. Make sure to write appropriate commit message 
3. Also link the PR to Issue using Keyword. For more information you can refer [this](https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) 

## HAPPY CODING 💻