In **AWS CloudFormation**, **Parameters** allow you to **customize your templates** when creating or updating a stack — making your templates reusable and flexible.

---

## 🧾 What Are Parameters?

Parameters are **input values** passed to a CloudFormation template at runtime. Think of them as **variables**.

### ✅ Use Cases:

* Specify different VPC IDs or AMI IDs across environments
* Customize instance types or availability zones
* Toggle optional features (like enabling logging)

---

## 🧩 Basic Example of Parameters

```yaml
Parameters:
  InstanceTypeParameter:
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t2.small
      - t3.micro
    Description: EC2 instance type

Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceTypeParameter
      ImageId: ami-0abcdef1234567890
```

Here:

* `InstanceTypeParameter` is defined with allowed values.
* The `!Ref` function is used to reference the parameter in the resource.

---

## 🔑 Common Parameter Types

| Type                                 | Description                     |
| ------------------------------------ | ------------------------------- |
| `String`                             | A single line of text           |
| `Number`                             | An integer or float             |
| `List<String>`                       | Comma-delimited list of strings |
| `AWS::EC2::KeyPair::KeyName`         | A valid EC2 key pair            |
| `AWS::SSM::Parameter::Value<String>` | SSM parameter value             |

---

## 🛑 Optional Validations

You can apply constraints to ensure valid input:

```yaml
  DBName:
    Type: String
    MinLength: 1
    MaxLength: 64
    AllowedPattern: "[a-zA-Z][a-zA-Z0-9]*"
    ConstraintDescription: "Must start with a letter and contain only alphanumeric characters."
```

---

## 📥 Passing Parameters (CLI Example)

```bash
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://template.yaml \
  --parameters ParameterKey=InstanceTypeParameter,ParameterValue=t2.small
```

---

## 📌 Summary

| Feature        | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Parameters** | Custom inputs at stack creation                              |
| **Used With**  | `!Ref` or `!Sub` in Resources section                        |
| **Benefits**   | Reusability, flexibility, environment-specific customization |

---
In AWS CloudFormation, when defining **Parameters**, you must specify a **Type**. This controls what kind of input is allowed when creating or updating a stack.

Here’s a complete list of **all supported parameter types**, grouped by category:

---

## 🔹 1. **Primitive Types**

| Type                 | Description                     | Example      |
| -------------------- | ------------------------------- | ------------ |
| `String`             | Any text value                  | `"myVpc"`    |
| `Number`             | Integer or float                | `42`, `3.14` |
| `List<Number>`       | Comma-separated list of numbers | `"1,2,3"`    |
| `CommaDelimitedList` | Comma-separated list of strings | `"a,b,c"`    |

---

## 🔹 2. **AWS-Specific Parameter Types**

These types provide **built-in validation** for AWS resource names/IDs.

| Type                                             | Description                              |
| ------------------------------------------------ | ---------------------------------------- |
| `AWS::EC2::AvailabilityZone::Name`               | A valid AZ name (e.g., `us-east-1a`)     |
| `AWS::EC2::Image::Id`                            | A valid AMI ID (e.g., `ami-0abcd1234`)   |
| `AWS::EC2::Instance::Id`                         | EC2 instance ID                          |
| `AWS::EC2::KeyPair::KeyName`                     | Name of an existing EC2 key pair         |
| `AWS::EC2::SecurityGroup::GroupName`             | EC2 security group name                  |
| `AWS::EC2::SecurityGroup::Id`                    | EC2 security group ID                    |
| `AWS::EC2::Subnet::Id`                           | Subnet ID                                |
| `AWS::EC2::Volume::Id`                           | EBS volume ID                            |
| `AWS::EC2::VPC::Id`                              | VPC ID                                   |
| `AWS::Route53::HostedZone::Id`                   | Route 53 hosted zone ID                  |
| `AWS::SNS::Topic::Arn`                           | ARN of an SNS topic                      |
| `AWS::SSM::Parameter::Name`                      | Name of an SSM parameter                 |
| `AWS::SSM::Parameter::Value<String>`             | Value of an SSM parameter (plain string) |
| `AWS::SSM::Parameter::Value<List<String>>`       | List from SSM parameter                  |
| `AWS::SSM::Parameter::Value<CommaDelimitedList>` | List from SSM param as comma list        |

---

## 🔹 3. **List Versions of AWS Types**

For many of the AWS types above, you can also specify a **list of them**:

| Type                                     | Description                |
| ---------------------------------------- | -------------------------- |
| `List<AWS::EC2::Subnet::Id>`             | List of subnet IDs         |
| `List<AWS::EC2::AvailabilityZone::Name>` | List of AZ names           |
| `List<AWS::EC2::SecurityGroup::Id>`      | List of security group IDs |

---

## 🔸 Constraints You Can Add (Optional)

You can apply constraints to parameter values to control their validity.

| Constraint              | Purpose                              |
| ----------------------- | ------------------------------------ |
| `Default`               | Set a default value                  |
| `AllowedValues`         | Only allow specific values           |
| `AllowedPattern`        | Regex pattern for validation         |
| `MinLength/MaxLength`   | Control string length                |
| `MinValue/MaxValue`     | Control number range                 |
| `ConstraintDescription` | Error message when validation fails  |
| `NoEcho: true`          | Hide sensitive data (like passwords) |

---

## ✅ Example

```yaml
Parameters:
  DBPassword:
    Type: String
    NoEcho: true
    MinLength: 8
    MaxLength: 32
    AllowedPattern: "[a-zA-Z0-9]*"
    ConstraintDescription: "Password must be alphanumeric and 8–32 characters."
```


