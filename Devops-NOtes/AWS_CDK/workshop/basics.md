**cdk init
**
The cdk init command creates a structure of files and folders within an empty directory to help organize the source code for your CDK app. This structure of files and folders is called your CDK project

cdk init sample-app --language python

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

A virtualenv (short for virtual environment) in Python is a self-contained directory that contains a Python interpreter and its own independent set of installed packages. It allows you to isolate dependencies for a specific project, so they don’t interfere with packages installed globally or with other projects.

🔍 Why Use a Virtualenv?
Dependency isolation – Different projects can use different versions of packages.

Avoid polluting the global Python installation.

Reproducibility – You can lock package versions (via requirements.txt) so the environment behaves consistently across machines or deployments.


After the init process completes and the virtualenv is created, you can use the steps to activate your virtualenv.

$ source .venv/bin/activate

Once the virtualenv is activated, you can install the required dependencies.

$ pip install -r requirements.txt

Project structure

.venv - The python virtual environment information discussed in the previous section.
cdk_workshop — A Python module directory.
cdk_workshop_stack.py — A custom CDK stack construct for use in your CDK application.
tests — Contains all tests.
unit — Contains unit tests.
test_cdk_workshop.py — A trivial test of the custom CDK stack created in the cdk_workshop package. This is mainly to demonstrate how tests can be hooked up to the project.
app.py — The “main” for this sample application.
cdk.json — A configuration file for CDK that defines what executable CDK should run to generate the CDK construct tree.
README.md — The introductory README for this project.
requirements.txt — This file is used by pip to install all of the dependencies for your application.
Your app's entry point


app.py- This code loads and instantiates an instance of the CdkWorkshopStack class from cdk_workshop/cdk_workshop_stack.py file. We won't be modifying this file during the workshop so you can safely close it.
