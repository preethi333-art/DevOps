### 🔀 **Conditions in AWS CloudFormation**

**Conditions** in CloudFormation let you control **whether certain resources, outputs, or properties are created or assigned**, based on **parameter values** or **environmental factors** like region, environment type, etc.

---

## ✅ Use Cases

| Use Case                                | Example                                       |
| --------------------------------------- | --------------------------------------------- |
| Deploy resource only in certain regions | Only create an S3 bucket in `us-east-1`       |
| Environment-based behavior              | Use a different AMI for `dev` vs `prod`       |
| Optional resources                      | Only create resources if a feature is enabled |
| Conditional outputs                     | Output a value only in specific conditions    |

---

## 🧩 **How Conditions Work**

### 1. **Define the Condition**

In the `Conditions` section, you define logical rules using `Fn::Equals`, `Fn::If`, `Fn::And`, `Fn::Or`, and `Fn::Not`.

```yaml
Conditions:
  IsProd:
    Fn::Equals: [ !Ref EnvType, "prod" ]
```

---

### 2. **Use the Condition**

You then apply the condition to resources, outputs, or properties using the `Condition` key.

```yaml
Resources:
  ProdOnlyBucket:
    Type: AWS::S3::Bucket
    Condition: IsProd
```

```yaml
Outputs:
  ProdBucketName:
    Condition: IsProd
    Value: !Ref ProdOnlyBucket
```

---

## 🧠 Logical Functions You Can Use

| Function     | Description                                 |
| ------------ | ------------------------------------------- |
| `Fn::Equals` | Compare two values                          |
| `Fn::If`     | Return one of two values based on condition |
| `Fn::And`    | True if **all** conditions are true         |
| `Fn::Or`     | True if **any** condition is true           |
| `Fn::Not`    | Logical NOT on a condition                  |

---

## 🛠 Full Example

```yaml
Parameters:
  EnvType:
    Type: String
    Default: dev
    AllowedValues:
      - dev
      - prod

Conditions:
  IsProd: !Equals [ !Ref EnvType, "prod" ]

Resources:
  ProdOnlyBucket:
    Type: AWS::S3::Bucket
    Condition: IsProd

Outputs:
  MaybeBucket:
    Condition: IsProd
    Value: !Ref ProdOnlyBucket
```

If `EnvType` is `dev`, the S3 bucket and output will **not** be created.

---

## 🧾 Summary

| Section      | Purpose                                             |
| ------------ | --------------------------------------------------- |
| `Conditions` | Define boolean rules to drive logic in the template |
| `Condition:` | Apply the condition to a resource/output/section    |
| `Fn::If`     | Use inline conditional values                       |

---

Let me know if you'd like:

* Examples with nested logical functions
* Multi-condition setups (e.g., region + env)
* How to test conditions via the AWS Console or CLI
