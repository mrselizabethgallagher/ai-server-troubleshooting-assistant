
import platform
import socket
import subprocess
from datetime import datetime

import psutil


def get_system_info():
    """Return basic host and OS information."""
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_cpu_info():
    """Return CPU usage and core count."""
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count(),
    }


def get_memory_info():
    """Return memory usage details in GB and percent."""
    memory = psutil.virtual_memory()
    return {
        "total_memory_gb": round(memory.total / (1024 ** 3), 2),
        "used_memory_gb": round(memory.used / (1024 ** 3), 2),
        "memory_percent": memory.percent,
    }


def get_disk_info():
    """Return root disk usage details in GB and percent."""
    disk = psutil.disk_usage("/")
    return {
        "total_disk_gb": round(disk.total / (1024 ** 3), 2),
        "used_disk_gb": round(disk.used / (1024 ** 3), 2),
        "disk_percent": disk.percent,
    }


def get_top_processes(limit=5):
    """
    Return the top processes by memory usage.
    CPU percent may be 0.0 on first read for some processes, which is normal.
    """
    processes = []

    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = proc.info
            processes.append({
                "pid": info.get("pid"),
                "name": info.get("name"),
                "cpu_percent": info.get("cpu_percent", 0.0),
                "memory_percent": round(info.get("memory_percent", 0.0), 2),
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes.sort(key=lambda p: p["memory_percent"], reverse=True)
    return processes[:limit]


def get_listening_ports():
    """Return a list of listening TCP/UDP ports."""
    listening_ports = []

    try:
        for conn in psutil.net_connections(kind="inet"):
            if conn.status == "LISTEN" and conn.laddr:
                listening_ports.append({
                    "ip": conn.laddr.ip,
                    "port": conn.laddr.port,
                })
    except (psutil.AccessDenied, Exception) as exc:
        return [{"error": str(exc)}]

    unique_ports = []
    seen = set()

    for item in listening_ports:
        key = (item["ip"], item["port"])
        if key not in seen:
            seen.add(key)
            unique_ports.append(item)

    return unique_ports


def get_service_status(service_name):
    """
    Check whether a service is active using systemctl.
    Returns 'active', 'inactive', 'failed', or an error string.
    """
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True,
            check=False,
        )
        status = result.stdout.strip()

        if status:
            return status
        return result.stderr.strip() or "unknown"
    except FileNotFoundError:
        return "systemctl not found"
    except Exception as exc:
        return f"error: {exc}"
