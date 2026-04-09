import psutil
import subprocess
import boto3
from datetime import datetime

REGION = "ap-south-1"
SENDER = "harshit.rathaur3@gmail.com"
RECIPIENT = "harshit.rataur@zohomail.com"

def check_cpu():
    cpu = psutil.cpu_percent(interval=2)
    if cpu > 80:
        return f"CPU usage critical: {cpu}%"
    return None

def check_memory():
    mem = psutil.virtual_memory()
    if mem.available < (0.15 * mem.total):
        return f"Low memory available: {mem.available // (1024*1024)} MB"
    return None

def check_disk():
    alerts = []
    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)
        if usage.percent > 85:
            alerts.append(
                f"Disk usage high on {part.mountpoint}: {usage.percent}%"
            )
    return alerts

def check_service(service):
    status = subprocess.getoutput(f"systemctl is-active {service}")
    if status != "active":
        return f"Service down: {service}"
    return None

def send_email(subject, body):
    ses = boto3.client("ses", region_name=REGION)
    ses.send_email(
        Source=SENDER,
        Destination={"ToAddresses": [RECIPIENT]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}}
        }
    )

def main():
    alerts = []

    cpu_alert = check_cpu()
    if cpu_alert:
        alerts.append(cpu_alert)

    mem_alert = check_memory()
    if mem_alert:
        alerts.append(mem_alert)

    disk_alerts = check_disk()
    if disk_alerts:
        alerts.extend(disk_alerts)

    service_alert = check_service("nginx")
    if service_alert:
        alerts.append(service_alert)

    if alerts:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Time: {timestamp}\n\n" + "\n".join(alerts)
        send_email("CRITICAL: Server Health Alert", message)

if __name__ == "__main__":
    main()