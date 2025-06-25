In **Terraform**, `list`, `set`, and `map` are commonly used **input variable types** that help manage structured and reusable configurations.

Here's a breakdown of each with their **differences**:

---

### ✅ 1. `list`

* An **ordered** collection of values.
* Can contain duplicate values.
* Accessed by **index** (e.g., `list[0]`).

**Example:**

```hcl
variable "names" {
  type = list(string)
  default = ["alice", "bob", "alice"]
}
```

**Use case:** When the order matters (e.g., availability zones).

---

### ✅ 2. `set`

* An **unordered** collection of **unique** values.
* Cannot contain duplicates.
* Cannot be indexed like a list.

**Example:**

```hcl
variable "unique_names" {
  type = set(string)
  default = ["alice", "bob"]
}
```

**Use case:** When you want to ensure uniqueness and don't care about order.

---

### ✅ 3. `map`

* A **key-value** pair structure (like a dictionary).
* Keys must be strings; values can be any type.
* Accessed by **key** (e.g., `map["key"]`).

**Example:**

```hcl
variable "region_map" {
  type = map(string)
  default = {
    "us-east-1" = "Virginia"
    "us-west-1" = "California"
  }
}
```

**Use case:** When you want to look up a value by a known key (e.g., environment -> AMI ID).

---

### 🔍 Differences Summary

| Feature       | List               | Set               | Map                |
| ------------- | ------------------ | ----------------- | ------------------ |
| Ordered       | ✅ Yes              | ❌ No              | ❌ No               |
| Duplicates    | ✅ Allowed          | ❌ Not Allowed     | 🔸 Keys unique     |
| Access Method | By index (`[0]`)   | By iteration only | By key (`["key"]`) |
| Use Case      | Sequence of values | Unique collection | Key-based lookup   |

---

Let me know if you want a table comparing usage examples too.
