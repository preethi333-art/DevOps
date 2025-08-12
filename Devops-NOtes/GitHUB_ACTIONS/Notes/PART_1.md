Here are the **detailed notes** based on the GitHub Actions tutorial covered in the video transcripts:

---

## 📘 **GitHub Actions Workflow - Notes**

---

### 🔹 **Part 1: Introduction & First Workflow**

#### ✅ What is a GitHub Workflow?

* A **workflow** is an automation process defined in a `.yml` file.
* It can run on events such as `push`, `pull_request`, or even **manually**.
* Workflows are stored under the `.github/workflows/` directory in your repo.

#### ✅ Directory Structure

```
repository/
└── .github/
    └── workflows/
        └── demo.yml
```

---

### 📝 **Sample: Basic Workflow Structure**

```yaml
name: Hello World

on:
  push:
    branches:
      - main

jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - name: Greetings
        run: echo "Hello World"
```

#### 🔹 Key Concepts:

* **`on:`** - Specifies the event (e.g., push to main branch) that triggers the workflow.
* **`jobs:`** - A job is a set of steps that execute on the same runner.
* **`runs-on:`** - Specifies the environment (e.g., Ubuntu).
* **`steps:`** - Each job has one or more steps; each step is an action or command.

---

### 🔹 **Workflow Execution**

* Committing the `.yml` file to the `main` branch **automatically triggers** the workflow if `on: push` is defined.
* Go to the **"Actions"** tab in GitHub to view status & logs.

---

### 📂 **Workflow Logs Overview**

* GitHub shows:

  * Runner details (OS, version)
  * Job steps and outputs
  * Raw logs and console outputs

---

## 🔹 **Part 2: Manual Trigger using `workflow_dispatch`**

#### 🛠️ Update `on:` to allow manual triggering:

```yaml
on:
  workflow_dispatch:
```

#### 📌 Result:

* Adds a **"Run Workflow"** button in the Actions tab.

---

## 🧩 **Adding Inputs to Manual Workflow**

### 🔹 Types of Inputs:

1. **string**
2. **number**
3. **boolean**
4. **choice**
5. **(Advanced)** `environment` – covered in later videos

### 📝 **Syntax Example**

```yaml
on:
  workflow_dispatch:
    inputs:
      name:
        description: 'Name'
        type: string
        default: 'test'
```

---

### 💡 **Accessing Input Values**

Use `${{ inputs.input_name }}` in your steps:

```yaml
- name: Greet by Name
  run: echo "Hello ${{ inputs.name }}"
```

---

### 📌 **Boolean Input Example**

```yaml
      married:
        description: 'Is Married?'
        type: boolean
```

* Shown as a **checkbox** in the manual trigger form
* Default is `false` unless checked by the user

---

### 📌 **Choice Input Example**

```yaml
      gender:
        description: 'Gender'
        type: choice
        options:
          - male
          - female
```

* Shown as a **dropdown** to the user

---

### 🧪 **Testing Inputs in Steps**

Each input can be used in different steps for clarity:

```yaml
- name: Age
  run: echo "Age: ${{ inputs.age }}"

- name: Gender
  run: echo "Gender: ${{ inputs.gender }}"

- name: Married
  run: echo "Married: ${{ inputs.married }}"
```

---

## 🔁 **Important Notes**

* Manual trigger via `workflow_dispatch` **only works on default branch**.
* To change default branch:

  1. Go to **Settings > Branches**
  2. Set desired branch as default
* Without being on the default branch, **manual trigger option will not appear**.

---

## ✅ **Summary**

| Feature                 | Description                                   |
| ----------------------- | --------------------------------------------- |
| `on: push`              | Automatically triggers workflow on code push  |
| `on: workflow_dispatch` | Enables **manual run** via Actions tab        |
| `inputs:`               | Allows form-style inputs for manual workflows |
| `jobs:`                 | Defines one or more jobs to run               |
| `steps:`                | Each job includes a set of actions/commands   |
| `runs-on:`              | Specifies the OS/environment (e.g. Ubuntu)    |

---

## 🧠 **Next Steps**

* Try combining triggers (e.g., push + manual)
* Add `if:` conditions to steps
* Use reusable workflows
* Learn `matrix` strategy for parallel jobs
* Explore GitHub Actions Marketplace

---

Let me know if you'd like this exported to **PDF**, **DOCX**, or as a **GitHub repo-ready README.md**.
