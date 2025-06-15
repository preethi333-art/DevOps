# CDK Stacks and Templates

## One Stack = One Template
```ascii
[CDK App]
│
├── Stack 1 (my-first-cdk-app)
│   └── Produces → template1.json
│
├── Stack 2 (if added)
│   └── Produces → template2.json
│
└── Stack 3 (if added)
    └── Produces → template3.json
```

## Example: Single Stack App
```ascii
app.py
└── MyFirstCdkAppStack
    ├── SQS Queue
    └── SNS Topic
    │
    └── Produces → my-first-cdk-app.template.json
```

## Example: Multi-Stack App
```ascii
app.py
├── DatabaseStack
│   └── DynamoDB Table
│       └── Produces → database-stack.template.json
│
├── NetworkStack
│   └── VPC Resources
│       └── Produces → network-stack.template.json
│
└── ComputeStack
    └── Lambda Functions
        └── Produces → compute-stack.template.json
```

## Key Points
1. Each stack in your CDK app gets its own CloudFormation template
2. Template name matches stack name
3. Templates are generated during synthesis
4. Each template is deployed as a separate CloudFormation stack 
