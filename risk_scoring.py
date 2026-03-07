



def calculate_risk(cpu_percent, memory_percent, disk_percent, failed_logins):

    score = 0
    alerts = []

    if cpu_percent > 90:
        score += 3
        alerts.append("High CPU usage")

    if memory_percent > 90:
        score += 2
        alerts.append("High memory usage")

    if disk_percent > 90:
        score += 3
        alerts.append("Disk usage above 90%")

    if failed_logins > 10:
        score += 2
        alerts.append("Multiple failed SSH login attempts detected")

    return score, alerts
