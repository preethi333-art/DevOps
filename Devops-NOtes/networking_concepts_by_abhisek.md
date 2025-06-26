Here are **concise notes** from the networking fundamentals video you provided:

---

## 📝 Networking Fundamentals: Key Concepts

### 1. **IP Address**
- **Definition:** A unique number assigned to each device on a network.
- **Purpose:** Identifies devices for communication, tracking, and access control.
- **Analogy:** Like a house number for each device.
- **Format:**  
  - **IPv4:** Four numbers (0-255) separated by dots (e.g., 192.168.1.1).
  - Each number = 1 byte (8 bits), so IPv4 = 32 bits total.
  - Each byte can be 0–255 because 8 bits = 2^8 = 256 values.
- **Example:**  
  - 192.168.0.1  
  - 10.0.0.5

---

### 2. **Subnet**
- **Definition:** A smaller network within a larger network (sub-network).
- **Purpose:**  
  - **Security:** Isolate sensitive devices (e.g., finance vs. free Wi-Fi).
  - **Privacy:** Limit access between groups.
  - **Isolation:** Prevents a breach in one subnet from affecting others.
- **Types:**
  - **Private Subnet:** No internet access.
  - **Public Subnet:** Has internet access.
- **How to create:**  
  - Split a large network (e.g., office) into smaller subnets for different purposes.

---

### 3. **CIDR (Classless Inter-Domain Routing)**
- **Definition:** A way to specify IP address ranges and subnet sizes.
- **Format:** `IP_address/Prefix_Length` (e.g., 192.168.1.0/24)
- **Calculation:**  
  - `/24` means 32-24=8 bits for hosts → 2^8 = 256 IPs.
  - `/31` → 2 IPs, `/30` → 4 IPs, `/29` → 8 IPs, etc.
- **Usage:**  
  - Assigns the number of IPs in a subnet.
  - Example: 172.16.3.0/24 gives 256 IPs (for a finance subnet).

---

### 4. **Private vs Public IP Ranges**
- **Private IPs:**  
  - 10.0.0.0 – 10.255.255.255  
  - 172.16.0.0 – 172.31.255.255  
  - 192.168.0.0 – 192.168.255.255  
  - Used for internal networks, not routable on the internet.
- **Public IPs:**  
  - Any IP not in the above ranges, routable on the internet (e.g., 8.8.8.8 for Google DNS).

---

### 5. **Ports**
- **Definition:** A number that identifies a specific process or service on a device.
- **Purpose:** Allows multiple applications to use the same IP address.
- **Format:** `IP:Port` (e.g., 192.168.1.10:8080)
- **Common Ports:**  
  - 80 (HTTP), 443 (HTTPS), 3306 (MySQL), 8080 (Jenkins)
- **Range:** 0–65535 (some reserved, some for custom use)

---

### 6. **Summary Table**

| Concept   | What it is / Why it matters                |
|-----------|--------------------------------------------|
| IP Address| Unique device identifier on a network      |
| Subnet    | Subdivision of a network for isolation     |
| CIDR      | Notation for IP range/subnet size          |
| Private IP| Internal use, not internet-routable        |
| Public IP | Internet-routable address                  |
| Port      | Identifies application/service on a device |

---

### 7. **Assignments/Practice**
- Convert an IP address (e.g., 172.32.16.1) to binary (octet) format.
- Calculate number of IPs in a CIDR (e.g., 172.68.3.0/30).
- Identify if an IP is private or public.

---

**Next Video:** OSI Model (Layers 1–7, HTTP, TCP, etc.)

---

**Tip:**  
Use online CIDR calculators to practice subnetting and IP range calculations!

---

Let me know if you want a visual diagram, more examples, or a quiz for practice!
