
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
from risk_scoring import calculate_risk


def main():
    print("=== SYSTEM INFO ===")
    print(get_system_info())

    print("\n=== CPU INFO ===")
    cpu_info = get_cpu_info()
    print(cpu_info)

    print("\n=== MEMORY INFO ===")
    memory_info = get_memory_info()
    print(memory_info)

    print("\n=== DISK INFO ===")
    disk_info = get_disk_info()
    print(disk_info)

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

    print("\n=== SYSTEM RISK SCORE ===")
    score, alerts = calculate_risk(
        cpu_info["cpu_percent"],
        memory_info["memory_percent"],
        disk_info["disk_percent"],
        ssh_results["failed_count"],
    )

    print(f"Risk Score: {score}/10")

    if alerts:
        print("Alerts:")
        for alert in alerts:
            print(f"- {alert}")
    else:
        print("No critical issues detected.")


if __name__ == "__main__":
    main()
