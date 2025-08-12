Here are the **structured notes** for the GitHub Actions tutorial on **step outputs** — covering how to **set outputs**, **access them in other steps**, and differences based on **shell types (bash vs PowerShell)**.

---

## 📘 GitHub Actions: Step Outputs

---

### ✅ What Are Step Outputs?

* Step outputs allow you to **pass data between steps or jobs** in the same workflow.
* Outputs are defined using `GITHUB_OUTPUT` and accessed via `${{ steps.<step_id>.outputs.<output_name> }}`.

---

## 📝 Step Output Syntax (Bash Shell)

### 📂 Workflow File: `.github/workflows/step-output.yml`

```yaml
name: Step Output

on:
  push:
    branches:
      - main

jobs:
  job-one:
    runs-on: ubuntu-latest
    steps:
      - name: Set Output
        id: set-output
        run: |
          echo "H=23" >> $GITHUB_ENV
          echo "name=interview Pro" >> $GITHUB_ENV
          echo "H=23" >> $GITHUB_OUTPUT
          echo "name=interview Pro" >> $GITHUB_OUTPUT

      - name: Access Output
        run: |
          echo "Output H: ${{ steps.set-output.outputs.H }}"
          echo "Output Name: ${{ steps.set-output.outputs.name }}"
```

> ✅ `GITHUB_OUTPUT` is an **environment variable** provided by GitHub for passing values between steps.

---

### 🔁 Setting Multiple Outputs

Use a `pipe (|)` in `run:` to execute multiple shell lines:

```yaml
run: |
  echo "H=23" >> $GITHUB_OUTPUT
  echo "name=interview Pro" >> $GITHUB_OUTPUT
```

---

### 🧪 Accessing Outputs from Other Steps

You can reference outputs using:

```yaml
${{ steps.<step_id>.outputs.<output_name> }}
```

Example:

```yaml
echo "Age is ${{ steps.set-output.outputs.H }}"
```

---

## 🧩 Using Outputs Across Multiple Steps

You can access the same output variable in **multiple steps**:

```yaml
- name: Access Output Again
  run: echo "User: ${{ steps.set-output.outputs.name }}"
```

---

## 🔁 Multiple Output Steps

```yaml
- name: Set Output 2
  id: set-output-2
  run: echo "salary=10000" >> $GITHUB_OUTPUT

- name: Access All Outputs
  run: |
    echo "Age: ${{ steps.set-output.outputs.H }}"
    echo "Name: ${{ steps.set-output.outputs.name }}"
    echo "Salary: ${{ steps.set-output-2.outputs.salary }}"
```

---

## 💡 Output Access in PowerShell

When using PowerShell (`pwsh`) instead of bash:

### 🖥️ Use:

```powershell
$env:GITHUB_OUTPUT
```

OR

```powershell
"key=value" | Out-File -Append -FilePath $env:GITHUB_OUTPUT
```

> 🧠 In PowerShell, environment variables are accessed using:

```powershell
$env:<variable_name>
```

---

## 🔄 Shell Differences Summary

| Shell      | Output Syntax                        |                                                    |
| ---------- | ------------------------------------ | -------------------------------------------------- |
| Bash       | `echo "key=value" >> $GITHUB_OUTPUT` |                                                    |
| PowerShell | \`"key=value"                        | Out-File -Append -FilePath \$env\:GITHUB\_OUTPUT\` |

---

## ✅ Summary

| Feature                         | Description                                            |                                              |
| ------------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| `GITHUB_OUTPUT`                 | Special file used to store output variables from steps |                                              |
| `id:`                           | Required to reference outputs from a specific step     |                                              |
| `steps.<step_id>.outputs.<key>` | Syntax to access outputs                               |                                              |
| Reusable Outputs                | Accessible across multiple steps                       |                                              |
| Multi-Shell Support             | Bash (default) and PowerShell (`pwsh`) supported       |                                              |
| Use \`pipe (                    | )\`                                                    | For multiline shell commands in `run:` block |

---

Let me know if you’d like:

* A complete **YAML workflow file** with comments
* A **demo repo structure**
* Export to **PDF/Markdown** for your reference

Happy to help!
