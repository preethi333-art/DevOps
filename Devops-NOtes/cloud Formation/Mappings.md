 **Mappings in AWS CloudFormation** — a very useful feature for managing region-specific or environment-specific configuration values inside a template.

---

## 📍 **What Are Mappings in CloudFormation?**

**Mappings** are key-value lookups used in CloudFormation templates to define **static configuration data** that does **not change at runtime**. They are ideal when you want to reference predefined values based on specific conditions like **AWS Region**, **environment**, or **instance type**.

---

## 🧩 Example: Basic Mapping

```yaml
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0abcdef1234567890
    us-west-1:
      AMI: ami-0fedcba9876543210
```

This map links AWS regions to AMI IDs.

---

## 🛠 Using Mappings with `Fn::FindInMap`

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", AMI]
      InstanceType: t2.micro
```

### Explanation:

* `!FindInMap` is used to **look up values** in the mapping.
* `!Ref "AWS::Region"` dynamically fetches the current region.
* This selects the correct AMI for that region.

---

## ✅ Use Cases for Mappings

| Use Case                    | Example                                      |
| --------------------------- | -------------------------------------------- |
| Region-based configurations | Different AMIs per region                    |
| Environment-specific values | Use different VPC or subnet IDs for dev/prod |
| Instance pricing info       | Assign cost metadata for budgeting           |

---

## 🔐 Key Properties

| Feature         | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| **Static**      | Values are fixed — cannot be modified at runtime (unlike parameters) |
| **Structured**  | Nested as `TopLevelKey -> SecondLevelKey -> Value`                   |
| **Lookup-only** | You must use `Fn::FindInMap` or `!FindInMap` to access values        |

---

## 🧠 Mapping vs. Parameters

| Feature  | Mappings                         | Parameters                           |
| -------- | -------------------------------- | ------------------------------------ |
| Editable | No (static in template)          | Yes (user-defined at stack creation) |
| Dynamic  | No                               | Yes                                  |
| Use Case | Region/environment-based lookups | Runtime user customization           |

---

## 🧾 Summary

* Mappings store static lookup tables inside your CloudFormation template.
* Use them with `Fn::FindInMap` to reference the data.
* Ideal for regional AMIs, environment settings, or static pricing data.
* Do **not** require user input like parameters.

---

Let me know if you’d like:

* A real-world example (e.g., prod/dev configs)
* How to combine mappings with conditions
* Mapping vs SSM Parameter Store comparison
