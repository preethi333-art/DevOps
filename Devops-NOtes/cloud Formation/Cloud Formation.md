Infrastructure as a Code
=======================
- Manual work is tough to reproduce from scratch.
It will be difficult to produce changes in:
- Another region

Another account

Same account if unwanted deletion of resources occur
It would be great if we could recreate the whole infrastructure using Code.
Code would deploy and do all the changes by creating, updating and
deleting our infrastructure.

What is AWS CloudFormation?
-============================
AWS CloudFormation is a service that helps you model and set up your AWS
resources so that you can spend less time managing those resources and
more time focusing on your applications that run in AWS.
You can create a template that describes all the AWS resources that you
want.

For example, Amazon EC2 instances or Amazon RDS DB instances

Provisions and configures the resources for you.


Benefits of CloudFormation
==========================
Simplify infrastructure
Quickly replicate your infrastructure
Easily control and track changes to your infrastructure
Each resource within the stack is tagged with an identifier so you can easily
interpret the costs
Hence, you can estimate costs using the CloudFormation

AWS CloudFormation concepts
============================
When you use AWS CloudFormation, you work with templates and stacks.
You create templates to describe your AWS resources and their properties.
Templates:
============
JSON or YAML formatted
Blueprints for building your AWS resources
Stacks:
=========
manage related resources as a single unit called a stack.
You create, update, and delete a collection of resources by creating, updating,
and deleting stacks.
- Change sets
============

In AWS CloudFormation, **Templates**, **Stacks**, and **Change Sets** are core components used for infrastructure as code (IaC). Here’s a breakdown of each and how they relate:

---

## 🧾 1. **Templates**

* A **template** is a JSON or YAML file that defines **AWS resources** (like EC2 instances, S3 buckets, etc.).
* It describes *what* to create and configure, including:

  * Parameters
  * Resources
  * Outputs
  * Mappings and conditions

**Example:**

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
```

---

## 📦 2. **Stacks**

* A **stack** is a running instance of a CloudFormation template.
* When you **create a stack**, CloudFormation reads the template and provisions the resources defined.
* You can:

  * Create a stack
  * Update a stack (by submitting a modified template)
  * Delete a stack

**Analogy:**
Think of a template as a blueprint and a stack as the actual constructed building.

---

## ♻️ 3. **Change Sets**

* A **Change Set** shows **what will change** in your stack before you actually apply the update.
* Useful for **safe deployment** and **review before changes** are made.
* Especially important in production environments.

**Workflow:**

1. Modify the template or parameters.
2. Create a change set.
3. CloudFormation shows a diff of the current stack vs. proposed changes.
4. You review and **execute the change set** to apply the update.

---

## 🔁 Relationship Summary

| Component      | Purpose                                    | Used When                        |
| -------------- | ------------------------------------------ | -------------------------------- |
| **Template**   | Blueprint for your infrastructure          | When defining what to deploy     |
| **Stack**      | Actual deployed resources from a template  | When deploying or managing infra |
| **Change Set** | Preview of changes before updating a stack | When updating stacks safely      |
=======================================================================================================================

How CloudFormation Works
========================
Templates are uploaded in S3 and then referenced in CloudFormation
To update the template we can't reuse the previous ones
Each time we have to upload a new version of template
Deleting a stack deletes every single artifact created using CloudFormation

