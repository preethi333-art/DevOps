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

Let me know if you want an example with **nested stacks**, **SSM parameters**, or **parameter overrides using CI/CD pipelines**!
