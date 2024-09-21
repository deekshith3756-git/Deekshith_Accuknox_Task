import psutil
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging to store logs in the logs directory
logging.basicConfig(filename='logs/system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # 80% CPU usage
MEMORY_THRESHOLD = 80  # 80% Memory usage
DISK_THRESHOLD = 80  # 80% Disk usage

def monitor_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def monitor_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def monitor_disk():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
    return disk_usage

def monitor_processes():
    process_count = len(psutil.pids())
    logging.info(f"Total running processes: {process_count}")
    return process_count

def monitor_system():
    logging.info("Starting system health check...")
    cpu = monitor_cpu()
    memory = monitor_memory()
    disk = monitor_disk()
    processes = monitor_processes()

    logging.info(f"CPU Usage: {cpu}%")
    logging.info(f"Memory Usage: {memory}%")
    logging.info(f"Disk Usage: {disk}%")
    logging.info(f"Running Processes: {processes}")

if __name__ == '__main__':
    monitor_system()
