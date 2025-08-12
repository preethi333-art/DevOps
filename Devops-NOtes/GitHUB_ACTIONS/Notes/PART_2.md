Here are the **detailed notes** for the next parts of the GitHub Actions tutorial, covering **workflow triggering behavior, disabling workflows, and scheduled workflows** using `cron`.

---

## 📘 **GitHub Actions: Intermediate Concepts**

---

### 🔹 **Recap of Previous Workflows**

| Workflow     | Trigger Type            | File               |
| ------------ | ----------------------- | ------------------ |
| `demo.yml`   | `push` to `main` branch | Auto-triggered     |
| `manual.yml` | `workflow_dispatch`     | Manually triggered |

#### 🔁 Unintended Trigger Issue:

* Every time `manual.yml` was modified, `demo.yml` also ran because it listens to **push events on `main`**.
* Even small changes (e.g., adding a space) cause a new run.

---

### 🚫 **Disabling a Workflow Temporarily**

> Avoids unnecessary execution without deleting the `.yml` file.

#### 📌 Steps to Disable a Workflow:

1. Go to the **Actions** tab.
2. Click the workflow (e.g., `demo.yml`) from the sidebar.
3. Click the **three dots (•••)** menu (top-right).
4. Click **"Disable workflow"**.

* You’ll now see a banner: `This workflow was disabled manually`.
* A label also appears: `"Workflow disabled"` under that workflow.

#### 🔁 To Enable Again:

* Click the same banner and click **"Enable workflow"**.

---

## ⏰ **Scheduled Workflows (Using `cron`)**

### 🔸 What is a Cron Expression?

* A cron (CRON = **Command Run ON Notice**) defines a **repeating time-based schedule**.
* GitHub Actions uses cron to run workflows **automatically at set intervals**.

---

### ⏱️ **Cron Syntax Format**

A cron expression has **5 fields**:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday = 0)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

---

### 📋 Examples:

| Expression                | Description                              |
| ------------------------- | ---------------------------------------- |
| `* * * * *`               | Every minute (❌ Not allowed in GitHub)   |
| `*/5 * * * *`             | ✅ Every 5 minutes                        |
| `0 0 * * *`               | Every day at **12 AM (UTC)**             |
| `5 * * * *`               | 5th minute of every hour                 |
| `35 5 * * 1,3`            | 5:35 AM UTC every **Monday & Wednesday** |
| `35 5 * * 2,4`            | 5:35 AM UTC every **Tuesday & Thursday** |
| Multiple cron expressions | Workflow runs on **all matched times**   |

---

### ✅ GitHub’s Scheduling Limit:

> 🔺 GitHub does **not support schedules below 5 minutes** interval.

---

### 📝 **Example: `scheduled.yml`**

```yaml
name: Schedule Workflow

on:
  workflow_dispatch:  # Manual trigger (optional but recommended for first run)
  schedule:
    - cron: '*/10 * * * *'  # Every 10 minutes

jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - name: Log time
        run: date
```

---

### 🧪 **Testing Scheduled Workflows**

* After pushing the file, GitHub **may not trigger it immediately**.
* ✅ To fix this:

  * Add `workflow_dispatch` temporarily
  * Manually trigger the workflow once
  * Then remove `workflow_dispatch` if not needed

---

### ⚠️ Known Issues with Schedule:

* **First run may be delayed** or skipped until a manual trigger is done.
* **Inconsistencies observed**: Some runs may be missed or delayed due to GitHub runner limitations or backlog.

---

### 🧠 Best Practices

* Use `workflow_dispatch` along with `schedule` initially to validate the job.
* Use a **single workflow for multiple schedules** if they share similar logic.
* Comment your `cron` expressions or use hover tooltips in GitHub editor.

---

## ✅ **Summary**

| Topic               | Key Takeaways                                             |
| ------------------- | --------------------------------------------------------- |
| Disable Workflow    | Prevents workflow from running without deleting it        |
| Enable Workflow     | Reactivate disabled workflows anytime                     |
| Scheduled Workflows | Use `cron` expressions under `on.schedule`                |
| Cron Format         | `minute hour day month weekday`                           |
| Schedule Limits     | Min interval is **5 minutes** in GitHub                   |
| Trigger Issues      | Run once manually using `workflow_dispatch` to fix delay  |
| Multiple Events     | A workflow can have multiple triggers: push, manual, cron |

---

Let me know if you'd like this converted to:

* PDF summary
* Markdown file for your GitHub repo
* Slide deck (e.g., for teaching/demo)

Ready to generate it in any format you prefer!
