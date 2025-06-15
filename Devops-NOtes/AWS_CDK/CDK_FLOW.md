

---

## 🔧 What is AWS CDK?

The **AWS Cloud Development Kit (CDK)** is an open-source software development framework that lets you define your **cloud infrastructure using programming languages** like:

* TypeScript / JavaScript
* Python
* Java
* C#

Instead of writing long CloudFormation YAML or JSON files, you can use CDK to define infrastructure using **code** (Infrastructure as Code – IaC).

---

## 🚀 Key Concepts in AWS CDK

### 1. **App**

An **App** is the root of your CDK project. It can contain one or more **Stacks**.

```python
app = App()
```

---

### 2. **Stack**

A **Stack** is a unit of deployment in AWS CDK. It maps directly to a **CloudFormation Stack**.

You define all your infrastructure (resources like Lambda, S3, EC2) inside a stack.

```python
class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        # Define resources here
```

---

### 3. **Construct**

A **Construct** is the basic building block of CDK. It represents a piece of infrastructure.

* Examples:

  * `s3.Bucket` (S3 Bucket)
  * `lambda.Function` (Lambda Function)
  * `ec2.Instance` (EC2 Instance)

CDK provides **L1, L2, and L3 constructs**:

* **L1**: Low-level, direct CloudFormation equivalent.
* **L2**: Easier abstraction (e.g., `s3.Bucket`).
* **L3**: Patterns (higher-level building blocks).

---

### 4. **Resources**

Actual AWS services you define using constructs.

Example:

```python
bucket = s3.Bucket(self, "MyBucket")
```

---

### 5. **Context & Environment**

* **Context**: CDK config values passed during deployment (e.g., `cdk.json`)
* **Environment**: Specifies AWS account and region.

```python
env=cdk.Environment(account="123456789012", region="us-west-2")
```

---

### 6. **cdk synth**

Generates the **CloudFormation template** from your code.

```bash
cdk synth
```

---

### 7. **cdk deploy**

Deploys the generated CloudFormation template to AWS.

```bash
cdk deploy
```

---

### 8. **cdk diff**

Shows the difference between your code and the deployed stack.

```bash
cdk diff
```

---

### 9. **cdk destroy**

Destroys the deployed stack from AWS.

```bash
cdk destroy
```

---

## ✅ Why Use AWS CDK?

* **Faster development** with familiar programming languages
* **Modular & reusable** code (classes, functions, etc.)
* **Type safety & IDE support**
* **Easier CI/CD integration**

---

Would you like a working example of a simple CDK app (like creating an S3 bucket or Lambda function)?
