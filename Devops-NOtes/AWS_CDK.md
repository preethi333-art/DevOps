## Install AWS CDK in Windows (npm is pre-requisites)
1. npm install -g aws-cdk
2. aws configure (AWS CLI)
2. cdk bootstrap aws://<AccountNumber>/<Region>

## Commands AWS CDK ( Run venv)
1. mkdir <project-name>
2. cd <project-name>
3. cdk init app --language python
4. cd .venv\Scripts
5. .\Activate.ps1
6. cd ..
7. pip install -r requirements.txt

## ## Commands AWS CDK ( Run without venv - provided you laptop has installed python "aws-cdk-lib" module )
1. mkdir <project-name>
2. cd <project-name>
3. cdk init app --language python
4. pip install -r requirements.txt

## Deploy The Project.
1. cdk synth - Generates a CloudFormation template from your CDK code.  # See what your code turns into
2. cdk diff  - Shows the difference between: Your current CDK code, and What’s already deployed in your AWS account. # Check what will change in AWS
3. cdk deploy - Deploys the synthesized CloudFormation template to AWS. # Deploy the changes to AWS

## Delete all resource
1. cdk destroy



1. cdk synth (short for synthesize)
Purpose:
Generates a CloudFormation template from your CDK code.

What it does:

Takes your CDK (Python, TypeScript, etc.) code.

Converts it into a pure CloudFormation JSON/YAML template.

Outputs it either on the terminal or saves to a file.

2. cdk diff
Purpose:
Shows the difference between: Your current CDK code, and What’s already deployed in your AWS account.

What it does:

Compares synthesized CloudFormation (from cdk synth) with the live stack in AWS.

Shows what will change: resources to be created, updated, or deleted.

Why use it:

To review changes before deploying.

Helps avoid surprises like unintended resource replacement.
