# reysic.com

[![Build Status](https://dev.azure.com/reysic/reysic.com/_apis/build/status/jeremy-hicks.reysic.com?branchName=master)](https://dev.azure.com/reysic/reysic.com/_build/latest?definitionId=1&branchName=master)

Personal website deployed to Azure App Service

## Local Development

* To activate venv in VS Code, use Terminal: Create New Integrated Terminal from the Command Palette (`Ctrl+Shift+P`).
* To install dependencies, `pip install -r requirements-to-freeze.txt --upgrade`, followed by `pip freeze > requirements.txt` (see [Kenneth Reitz workflow](https://www.kennethreitz.org/essays/a-better-pip-workflow)).
* To run [Black](https://pypi.org/project/black/) on a file, `black application.py`, on a directory, `black directory/`.
* To run locally, `py -m flask run` (looks for `app.py` by default), navigate to `http://127.0.0.1:5000/`, stop using `Ctrl+C` (see [VS Code Flask Tutorial](https://code.visualstudio.com/docs/python/tutorial-flask)).
