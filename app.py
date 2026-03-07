
from collector import (
    get_system_info,
    get_cpu_info,
    get_memory_info,
    get_disk_info,
    get_top_processes,
    get_listening_ports,
    get_service_status,
)

from log_parser import parse_failed_ssh_attempts


def main():

    print("=== SYSTEM INFO ===")
    print(get_system_info())

    print("\n=== CPU INFO ===")
    print(get_cpu_info())

    print("\n=== MEMORY INFO ===")
    print(get_memory_info())

    print("\n=== DISK INFO ===")
    print(get_disk_info())

    print("\n=== TOP PROCESSES ===")
    for proc in get_top_processes():
        print(proc)

    print("\n=== LISTENING PORTS ===")
    for port in get_listening_ports():
        print(port)

    print("\n=== SERVICE STATUS ===")
    services = ["ssh", "cron", "nginx"]
    for service in services:
        print(f"{service}: {get_service_status(service)}")

    print("\n=== SSH LOG ANALYSIS ===")

    ssh_results = parse_failed_ssh_attempts()

    if ssh_results["error"]:
        print(f"Error: {ssh_results['error']}")
    else:
        print(f"Log file: {ssh_results['log_path']}")
        print(f"Failed SSH logins: {ssh_results['failed_count']}")

        print("Top source IPs:")
        if ssh_results["top_ips"]:
            for ip, count in ssh_results["top_ips"].items():
                print(f"{ip}: {count}")
        else:
            print("None detected.")


if __name__ == "__main__":
    main()
