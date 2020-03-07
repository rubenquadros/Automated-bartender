# Automated-bartender

This is a simple python module with flask which can be deployed on the Raspberry Pi to make automated drinks.

## Steps to run the application on Raspberry Pi

1. Clone or download the project

2. Install the dependencies by executing the following command on the command line: "pip install -r requirements.txt"

3. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need. For this execute the following command: "python3 -m venv env" or "python -m venv env"

4. Activate the virtual environment using: "source env/bin/activate"\
If you are using windows run the following command: "env/Scripts/activate"\
Now, you should see (env) beside the folder name on your command line.

5. Finally run the application using: "flask run"\
This will run the application on "http://localhost:5000" \
You can also run the application using: "flask run --host=0.0.0.0"\
This will make your application publicly available
