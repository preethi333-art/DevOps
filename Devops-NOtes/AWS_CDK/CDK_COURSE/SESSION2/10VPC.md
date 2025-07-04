https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html

Here’s a **concise summary** of the lecture on AWS CDK L1 Constructs and how to use them, particularly focusing on creating a **VPC using L1 constructs** in Python:

---

### 🔹 What Are CDK Constructs?

* **Constructs** are the **basic building blocks** of CDK apps.
* Even the **App** and **Stack** are constructs (special types).
* Constructs can represent **individual AWS resources** or a group (solution).

---
thewe are 3 levels of constructs L1, L2, and L3. 
### 🔹 Construct Levels

1. **L1 (Low-level):**

   * Map **1:1 with CloudFormation** resources.
   * Names start with **`Cfn`** (e.g., `CfnVPC`).
   * Require **detailed knowledge** of each AWS resource.
   * Ideal for users familiar with CloudFormation.
   * you can switch to CDK using only L1 constructs to replace JSON or YAML templates with code in your favorite

programming language, such as Python.

2. **L2 (Higher-level):**

   * Provide sensible defaults and best practices.
   * Easier to use; abstract many details.

3. **L3 (Patterns):**

   * Composed of multiple L2 constructs as **pre-configured solutions**.

---

### 🔹 Example Architecture (using L1 constructs)

* Create a **VPC** with:

  * **2 Availability Zones**
  * Each zone has:

    * **1 Public subnet**
    * **1 Private (isolated) subnet**
  * Attach an **Internet Gateway** to the VPC
  * Define routes to make public subnets accessible
  * **No NAT Gateway** (to stay within Free Tier)

---

### 🔹 Writing the CDK Code

* CDK code typically goes into the **`__init__`** method of your stack class.

* To define a VPC using an L1 construct:

  * Use the **`aws_cdk.aws_ec2`** module.
  * Import with:

    ```python
    import aws_cdk.aws_ec2 as ec2
    ```

* L1 Construct for VPC is:

  ```python
  ec2.CfnVPC
  ```

---

### 🔹 Using the CDK Construct Library Reference

* Access the reference from the lecture resources.
* Navigate via:

  * **Service (e.g., EC2)**
  * Scroll to **CloudFormation Resources** section
  * Look for constructs that start with **`Cfn`**

---

### 🔹 Construct Syntax Overview

To instantiate an L1 construct like `CfnVPC`, use:

```python
from aws_cdk import aws_ec2 as ec2
from aws_cdk import core  # or aws_cdk as cdk in newer versions

vpc = ec2.CfnVPC(
    self,
    "MyVpc",
    cidr_block="10.0.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True,
    tags=[core.CfnTag(key="Name", value="MyVpc")]  # Correct tag format
)

internet_gateway = ec2.CfnInternetGateway(self, "InternetGateway")

ec2.CfnVPCGatewayAttachment(
    self,
    "IGWAttachment",
    vpc_id=vpc.attr_vpc_id,
    internet_gateway_id=internet_gateway.attr_internet_gateway_id
)

```

* You must **know the properties** of the resource (same as CloudFormation).
* For full property list, use the **CloudFormation reference link** provided in the construct’s CDK reference.

---

### 🔹 Summary Takeaways

* **L1 constructs** give **full control** but require **deep resource knowledge**.
* Use **construct library reference** to identify and configure resources.
* CDK lets you write **infrastructure as code** in your preferred language, like Python.
* Learning to use **L1 constructs** prepares you to understand and eventually use **L2 and L3** more effectively.

---

Certainly! Here's a natural continuation of the lecture summary, picking up from where the previous section ended:

---

🧠 1. CDK L1 Constructs Mirror CloudFormation
You are guided to scroll to the "Syntax" section of the AWS CDK reference documentation.

It is explained that:

CDK L1 constructs directly map to CloudFormation resources.

Properties like CidrBlock become cidr_block (i.e., PascalCase → snake_case), which is the Pythonic convention.

🧱 2. Creating the VPC (L1 Construct)
The construct ec2.CfnVPC is used to define a VPC manually.

Arguments passed:

self: Represents the current stack object (analogous to this in JavaScript).

Logical ID: 'MyVpc' (follows CloudFormation PascalCase naming).

Keyword arguments:

cidr_block='10.0.0.0/16'

enable_dns_hostnames=True

enable_dns_support=True

Python indentation is emphasized: it must be at the same indentation level as the super() call inside __init__.

🌐 3. Internet Gateway Creation
Created using ec2.CfnInternetGateway.

Passed:

self

Logical ID: 'InternetGateway'

This construct does not require any properties.

🔗 4. Attach Internet Gateway to VPC
Done via ec2.CfnVPCGatewayAttachment.

Passed:

self

Logical ID: 'IgwAttachment'

Properties:

vpc_id=my_vpc.attr_vpc_id

internet_gateway_id=internet_gateway.attr_internet_gateway_id

🔄 5. Understanding attr_ Attributes
CDK L1 constructs provide instance attributes for CloudFormation return values.

For example:

attr_vpc_id maps to Fn::GetAtt → VpcId in CloudFormation.

These attr_* attributes are auto-generated for most returned values.

If a particular attribute is not available, you can use:

python
Copy code
my_vpc.get_att("VpcId")
Equivalent to Fn::GetAtt.

🧩 6. Synthesizing and Deploying
Run:

cdk synth – Generates the CloudFormation template.

cdk deploy – Deploys it to AWS.

CDK automatically creates a cdk.out folder and CloudFormation JSON template.

Verified deployment using:

CDK Explorer in VS Code (from AWS Toolkit extension).

CloudFormation Console.

📉 7. Observations Post Deployment
The deployment is successful: the stack includes:

The VPC

The Internet Gateway

The Gateway Attachment

But: No subnets yet!

This is highlighted visually using the Resource Map in the AWS Console.

Sets up the next lecture: defining subnets, routing, and associations.

✅ Summary of New Concepts Introduced
Concept	Details
Pythonified CDK Syntax	Snake_case for properties, unlike PascalCase in raw CloudFormation
L1 Construct Usage	CfnVPC, CfnInternetGateway, CfnVPCGatewayAttachment
Using attr_* Attributes	Access return values from resources like attr_vpc_id, attr_internet_gateway_id
get_att() Fallback	Used when attr_* attributes are missing
Stack Deployment Steps	cdk synth → verify JSON → cdk deploy → validate via console
CDK Explorer Tool	Visualizes stacks and resources in VS Code
Next Steps Teased	Will add subnets, route tables, and internet routing later

