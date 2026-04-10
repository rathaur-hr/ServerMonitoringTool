# 🚀 Server Monitoring Tool (AWS + Python)

## 📌 Overview

A lightweight, agentless server monitoring tool built using Python and deployed on **Amazon Web Services (AWS)**.

This project monitors key Linux system metrics such as CPU usage, memory utilization, uptime, and service health. It automatically sends email alerts using AWS SES in Every One hour.

Designed to simulate real-world **Monitoring and Alerting systems**.

---

## 🧠 Key Features

* ✅ Real-time monitoring of:

  * CPU usage
  * Memory usage
  * System uptime
  * Service status (systemctl-based)
* 📧 Automated email alerts using AWS SES
* ⚙️ Configurable threshold-based alert system
* ⏱️ Scheduled execution using cron jobs
* 🪶 Lightweight and agentless design

---

## 🏗️ Architecture

```
EC2 (Linux Server)
   ↓
Python Script (healthcheck.py)
   ↓
Metrics Collection (psutil, subprocess)
   ↓
Threshold Evaluation
   ↓
Cron Job (Every 1 hour)
   ↓
Email Alerts (AWS SES)
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * psutil
  * boto3
  * smtplib
  * subprocess
  * datetime
* **Cloud Platform:** AWS (EC2, SES)
* **Operating System:** Linux
* **Scheduler:** Cron

---

## 📂 Project Structure

```
linux-monitoring-tool/
│
├── healthcheck.py      # Main monitoring script
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Launch EC2 Instance

* Create a Linux instance on AWS EC2
* Allow SSH (port 22) access

### 2️⃣ Connect to EC2

```bash
ssh ec2-user@your-public-ip
```

### 3️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ServerMonitoringTool.git
cd ServerMonitoringTool
```

### 4️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## ⚙️ Configuration

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
Disk Threshold = 85
SERVICES = ["nginx"]

EMAIL_SENDER = "your-email@example.com"
EMAIL_RECEIVER = "receiver@example.com"
```

---

## ⏰ Automation (Cron Job)

Set up a cron job to run every one hour:

```bash
crontab -e
```

Add:

```bash
0 * * * * /usr/bin/python3 /path/to/healthcheck.py
```

---

## 📧 Email Alerts

The system sends:

* 🚨 **Alert Emails & Health Reports**

```
CRITICAL: Server Health Alert
Today, 12:40 pm •
Time: 2026-04-09 12:40:02

Issues Detected:
CPU usage high: 96.0%

Full Server Status:
CPU Usage: 96.0%
Memory Usage: 369MB / 961MB (38.5%)
Disk Usage:
/: 22.4% used
/boot/efi: 12.9% used
Service (nginx): active
Last Reboot Time: 2026-04-09 12:36:05
---

## 🧠 Learning Outcomes

* Real-world server monitoring concepts
* AWS EC2 deployment and management
* Cron job automation
* Python system-level scripting
* Alerting and notification systems

---

## 👨‍💻 Author

**Harshit Rathaur**

---

## 💡 Acknowledgements

Inspired by real-world DevOps monitoring tools and SRE practices.
