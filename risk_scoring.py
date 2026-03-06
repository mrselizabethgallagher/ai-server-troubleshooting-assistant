def calculate_risk(cpu, memory, disk, failed_logins):

    score = 0
    alerts = []

    if cpu > 90:
        score += 3
        alerts.append("CPU usage above 90%")

    if memory > 90:
        score += 2
        alerts.append("Memory usage above 90%")

    if disk > 90:
        score += 3
        alerts.append("Disk usage above 90%")

    if failed_logins > 20:
        score += 2
        alerts.append("High number of failed SSH login attempts")

    return score, alerts
