Here are the **detailed and structured notes** for the next sections of the GitHub Actions tutorial, covering:

1. **Building Angular apps using workflows**
2. **Job dependencies using `needs`**
3. **Conditional job execution using `if: always()`**

---

## 📘 GitHub Actions: Angular CI/CD & Job Dependencies

---

## 🚀 Building Angular Application Using GitHub Workflows

### 📁 Workflow File: `.github/workflows/build-angular.yml`

### 🔧 Workflow Steps

```yaml
name: Build Angular App

on:
  push:
    branches:
      - main

jobs:
  build-angular:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Install Dependencies
        run: npm install

      - name: Build Angular App
        run: npm run build
```

### 📝 Explanation:

* **`checkout`**: Pulls repo code to the runner.
* **`setup-node`**: Installs Node.js version 18.
* **`npm install`**: Installs Angular dependencies.
* **`npm run build`**: Builds Angular project.

---

## 🔁 Job Dependencies with `needs`

### 🧩 Scenario

You want to **deploy** your Angular app only **after it has been built successfully**.

### 🔧 Updated Workflow with Dependency

```yaml
jobs:
  build-angular:
    runs-on: ubuntu-latest
    steps:
      - name: Build Step
        run: npm run build

  deploy-angular:
    runs-on: ubuntu-latest
    needs: build-angular
    steps:
      - name: Deploy Step
        run: echo "Deploying..."
```

### ✅ Result:

* `deploy-angular` will **only run if `build-angular` completes successfully**.
* If `build-angular` fails, `deploy-angular` will be **skipped**.

---

## 🧪 Introducing Multiple Dependencies

```yaml
jobs:
  build-angular:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building..."

  job-two:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Job Two Running"

  deploy-angular:
    runs-on: ubuntu-latest
    needs:
      - build-angular
      - job-two
    steps:
      - run: echo "Deploying App..."
```

* `deploy-angular` runs **only after both `build-angular` and `job-two` complete successfully**.

---

## ⚠️ Conditional Job Execution with `always()`

### 🔧 Example

Run `deploy-angular` **even if dependencies fail**:

```yaml
deploy-angular:
  runs-on: ubuntu-latest
  needs:
    - build-angular
    - job-two
  if: always()
  steps:
    - run: echo "Deploy triggered regardless of previous job status"
```

### ✅ Behavior:

* `deploy-angular` runs **even if one or more `needs` jobs fail**.
* Useful for:

  * Sending failure notifications
  * Cleaning up environments
  * Running post-build analysis

---

## 🚫 Common Error Example

### ❌ Invalid Action

```yaml
uses: actions/upload-artifact-123@v2  # Wrong action name
```

### 🧾 Error Message

> `Unable to resolve action 'actions/upload-artifact-123', repository not found.`

🛠️ Fix: Always verify action names on [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)

---

## ✅ Summary Table

| Feature                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| `checkout@v4`              | Pulls repo code to runner                   |
| `setup-node@v4`            | Installs Node.js in runner                  |
| `needs:`                   | Declares job dependencies                   |
| `if: always()`             | Runs job regardless of dependencies' status |
| Multiple `needs`           | Run job after multiple jobs succeed         |
| Invalid action error       | Happens if action name/version is wrong     |
| Use array or dash notation | Both styles are valid for `needs:`          |

---

Let me know if you'd like:

* A single combined **Angular CI/CD workflow**
* **Artifact upload + deploy** example
* Export to **PDF / Markdown / Slide deck** format

Ready to assist!
