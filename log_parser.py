
import re
from collections import Counter
from pathlib import Path


AUTH_LOG_PATHS = [
    "/var/log/auth.log",   # Ubuntu/Debian
    "/var/log/secure",     # RHEL/CentOS
]


def find_auth_log():
    """Return the first auth log path that exists, or None."""
    for path in AUTH_LOG_PATHS:
        if Path(path).exists():
            return path
    return None


def parse_failed_ssh_attempts():
    """
    Parse Linux auth logs for failed SSH logins.
    Returns total failed count, top offending IPs, and log path used.
    """
    log_path = find_auth_log()

    if not log_path:
        return {
            "log_found": False,
            "log_path": None,
            "failed_count": 0,
            "top_ips": {},
            "error": "No authentication log file found."
        }

    # Covers common SSH failure formats on Ubuntu/Debian
    failed_patterns = [
        re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"),
        re.compile(r"Invalid user .* from (\d+\.\d+\.\d+\.\d+)"),
    ]

    failed_count = 0
    ip_counter = Counter()

    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                for pattern in failed_patterns:
                    match = pattern.search(line)
                    if match:
                        failed_count += 1
                        ip_counter[match.group(1)] += 1
                        break

        return {
            "log_found": True,
            "log_path": log_path,
            "failed_count": failed_count,
            "top_ips": dict(ip_counter.most_common(5)),
            "error": None
        }

    except PermissionError:
        return {
            "log_found": True,
            "log_path": log_path,
            "failed_count": 0,
            "top_ips": {},
            "error": f"Permission denied reading {log_path}. Try running with sudo."
        }

    except Exception as exc:
        return {
            "log_found": True,
            "log_path": log_path,
            "failed_count": 0,
            "top_ips": {},
            "error": str(exc)
        }
