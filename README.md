# AI Server Troubleshooting Assistant

A Python-based system administration tool that automates Linux server health checks, parses authentication logs, checks service status, and uses AI to generate troubleshooting recommendations.

## Overview

This project collects server health information such as CPU usage, memory usage, disk utilization, running processes, and authentication logs. It then generates a structured report and uses AI to analyze the data and provide troubleshooting guidance for system administrators.

The goal is to automate common diagnostic tasks and help administrators quickly identify potential issues.

## Features

- Collects CPU, memory, and disk metrics
- Displays top running processes
- Identifies listening network ports
- Parses authentication logs for failed SSH login attempts
- Checks service status
- Generates a formatted server health report
- Uses AI to analyze system conditions and recommend actions

## Technologies Used

- Python
- psutil
- OpenAI API
- Linux system logs
- Regex parsing

## Project Goals

This project was created to combine AI with real-world system administration tasks such as monitoring, log analysis, troubleshooting, and automation.

It is designed to be useful for both learning and practical homelab environments.

## Future Improvements

- Windows support
- Flask dashboard
- automated alerts
- scheduled monitoring
- firewall integration
- additional log analysis
