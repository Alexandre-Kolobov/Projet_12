This is a CRM (Customer Relationship Management) application.
It works with PostgreSQL database and SQLAlchemy ORM.
To ensure security this application uses:
    - JWT token
    - SQLAlchemy ORM
    - Password hashing
    - Config file

Before running app:

- PostreSQL (the database):
    1)Please install the appropriate version of PostreSQL from https://www.postgresql.org/download/

    2)You have to create 2 databases, one for CRM and one for tests.


- Sentry (logging system):
    1)Create your account on https://sentry.io

    2)Create your project


- Python and virtual environment:
    1)To set up the virtual environment, please make sure that you have a python version higher that 3.3 (in prompt: python --version) because you need to have the pip installer.

    2)You have to create a folder ( /YOUR_FOLDER) and go in with the command line. In command line plese make "python -m venv venv" to create the virtual envrinment named "venv".

    3)To activate venv, via command line:
        For Windows: venv/Scripts/Activate.ps1 (with powershell) or use commande "source Scripts/activate" (if you use bash)
        For Linux: venv/bin/activate

    4)Place your command line in /YOUR_FOLDER and then "git clone https://github.com/Alexandre-Kolobov/Projet_12.git"

    5)In the folder make "pip install -r requirements.txt" to set up the right configuration

    6)In root directory please create a config.ini file and add this information with your own data from PostreSQL and Sentry:
        [postgresql]
        host = your_host
        user_epic = your_user
        password_epic = your_password
        db_name = your_database_name
        db_name_test = your_test_database_name


        [jwt]
        secret = your_secret_for_jwt

        [sentry]
        key = your_key_from_sentry

    7)Now you are ready to launch the web app. On the command line go to /YOUR_FOLDER and make "python main.py".

- How it works:
    On first application launch all tables will be created and you will be asked to create a first gestion user.
    Now you can use this user to create all others users and navigate to CRM app

- Additional information:
    1)For start linter please use "flake8 --format=html --htmldir=flake-report" and you can consult html rapport in the flake-report directory

    2)For start tests please use "pytest"

    3)For check test coverage  "pytest --cov=. --cov-report html" and you can check html rapport in the htmlcov directory
