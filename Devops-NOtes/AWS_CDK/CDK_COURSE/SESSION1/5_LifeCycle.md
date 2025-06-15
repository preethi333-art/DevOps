# CDK Lifecycle & Synthesis Process

## CDK Application Lifecycle

imagine building a house:

    App is the entire housing plan

    Stack is a floor

    Constructs are rooms, windows, or furniture

    The __init__ method is the blueprint for how each part is built
    

When you "run the blueprint" (cdk synth), it walks through the hierarchy and builds everything accordingly.

App (cdk.App)

│
└─── MyStack (cdk.Stack)

     │
     ├─── Bucket (aws_s3.Bucket)
     │
     ├─── LambdaFunction (aws_lambda.Function)
     │
     └─── DynamoDBTable (aws_dynamodb.Table)

App: The root of the construct tree (cdk.App) — it doesn't represent an AWS resource but holds all stacks.

MyStack: A CDK Stack that represents a single CloudFormation stack — it is a construct that contains other constructs.

Bucket, Lambda, Table: These are all child constructs — actual AWS resources defined inside the stack.


```ascii
[CDK Source Code] → [Lifecycle Phases] → [Deployment Artifacts] → [CloudFormation]


 Construction Phase -> The construction chain (init() methods) all constructs including app, stack, and their child constructs are instantiated
 --> Most of the CDK code executed at this stage
1. Construction Phase ->
   ├── Instantiate constructs
   └── Execute init methods

2. Preparation Phase
   ├── Execute prepare() methods
   └── Run CDK aspects

3. Validation Phase
   └── Execute validate() methods

4. Synthesis Phase--->   which creates the deployment artifacts by executing the synthesize() methods of all constructs.In your 'app.py' file, the main of your CDK app,the 'app.synth()' method call at the bottom
riggers this synthesis process.
--> these deployment artifacts may include CloudFormation templates, Lambda function bundles, files, Docker image assets, etc. depending on the construct type.
   └── Generate deployment artifacts

finally, all these deployment artifacts are deployed by creating CloudFormation stacks
5. Deployment Phase
   └── Create CloudFormation stacks
```

## Synthesis Process

```ascii
[CDK App] → [cdk synth] → [cdk.out/]
                    │
                    ├── template.json    (CloudFormation template)
                    ├── assets.json      (Asset information)
                    ├── manifest.json    (Deployment instructions)
                    ├── tree.json        (Construct hierarchy)
                    └── cdk.out.json     (Version information)
```


Assets.json
==========
automatically generated during cdk synth and contains all the necessary information about asset sources, destinations,
as a file asset and the S3 bucket name and object key as the deployment destination.
## Construct Tree Example
```ascii
App
└── my-first-cdk-app (Stack)
    ├── MyFirstCdkAppQueue (SQS)
    │   ├── Queue Policy
    │   └── SNS Subscription
    ├── MyFirstCdkAppTopic (SNS)
    ├── CDKMetadata
    ├── BootstrapVersion
    └── CheckBootstrapVersion
```

## Key Points
1. **Local Development**
   - Write CDK code
   - Define constructs and stacks
   - Use `cdk synth` to generate templates

2. **Synthesis Output**
   - CloudFormation templates (JSON/YAML)
   - Asset information
   - Deployment instructions
   - Construct hierarchy

3. **Deployment Artifacts**
   - Located in `cdk.out/` directory
   - Templates ready for CloudFormation
   - Asset information for S3 uploads

4. **Visualization**
   - Use AWS Toolkit in VS Code
   - View construct tree
   - Monitor deployment status

## Common Commands
```bash
# Synthesize CloudFormation template
cdk synth

# Synthesize specific stack
cdk synth my-first-cdk-app

# Synthesize multiple stacks
cdk synth stack1 stack2
``` 
