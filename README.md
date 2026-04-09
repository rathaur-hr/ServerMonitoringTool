# 🚀 Server Monitoring Tool (AWS + Python)

## 📌 Overview

A lightweight, agentless server monitoring tool built using Python and deployed on **Amazon Web Services (AWS)**.

This project monitors key Linux system metrics such as CPU usage, memory utilization, uptime, and service health. It automatically sends email alerts using AWS SES when predefined thresholds are exceeded.

Designed to simulate real-world **DevOps monitoring and alerting systems**.

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
Email Alerts (AWS SES)
   ↓
Cron Job (Every 5 Minutes)
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
git clone https://github.com/your-username/ServerMonitoringToo.git
cd linux-monitoring-tool
```

### 4️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## ⚙️ Configuration

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 75

SERVICES = ["nginx", "ssh"]

EMAIL_SENDER = "your-email@example.com"
EMAIL_RECEIVER = "receiver@example.com"
```

---

## ⏰ Automation (Cron Job)

Set up a cron job to run every 5 minutes:

```bash
crontab -e
```

Add:

```bash
*/5 * * * * /usr/bin/python3 /path/to/healthcheck.py
```

---

## 📧 Email Alerts

The system sends:

* 🚨 **Alert Emails** → When thresholds are exceeded
* 📊 **Status Reports** → Periodically (optional)

### Example Triggers

* CPU usage > 80%
* Memory usage > 75%
* Service failure

---

## 📸 Sample Alert

```
🚨 ALERT: High CPU Usage

Server: ip-172-31-xx
CPU Usage: 87%
Threshold: 80%
Time: 2026-04-09 12:30:00
```

---

## 🔥 Future Enhancements

* 📊 Web dashboard using Flask or FastAPI
* 📈 Graph-based monitoring (CPU/Memory trends)
* 🌐 Multi-server monitoring via SSH
* 🗄️ Store metrics in database (SQLite/DynamoDB)
* 🔔 Slack/Telegram integration for alerts

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

## ⭐ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 💡 Acknowledgements

Inspired by real-world DevOps monitoring tools and SRE practices.
