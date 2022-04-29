# kryon-fhir
***Please read all steps before start***

step1 : Install python:

--Download python(version above 3.9 or latest version) from https://www.python.org/downloads/

--Start install the python

--During installation select "Add Python to PATH" checkbox. It's create environment path automatically. Otherwise, python not recognized by your machine.

--Complete your python installation


********************************All commands must run in python-services directory*******************************

step2: Setup the project

--Open directory kryon-fhir 

--Open cmd in kryon-fhir directory

--Run the command(for install virtual environment) :  pip install virtualenv

--Run the command(for create virtual env)          :  py -3 -m venv venv

--Run the command(for activate virtual env)        :  venv\Scripts\activate

--Run the command(for install required package)    :  pip install -r requirements.txt

step3: Run the project

--Run the command(for set flask app)        : set FLASK_APP=application.py

--Run the command(for set config profile)   : set FLASK_ENV=development

--Run the command(for run the project)      : flask run

step4: open swagger

--in browser search the url: http://127.0.0.1:5000/  (for open the swagger)
