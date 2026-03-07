
from collector import (
    get_system_info,
    get_cpu_info,
    get_memory_info,
    get_disk_info,
    get_top_processes,
    get_listening_ports,
    get_service_status,
)


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
    for port in get_listening_ports()[:10]:
        print(port)

    print("\n=== SERVICE STATUS ===")
    services = ["ssh", "cron", "nginx"]
    for service in services:
        print(f"{service}: {get_service_status(service)}")


if __name__ == "__main__":
    main()
