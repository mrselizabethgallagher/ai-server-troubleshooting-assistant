# AI Server Troubleshooting Assistant

A Python-based system administration tool that automates Linux server health checks, parses authentication logs, checks service status, and uses AI to generate troubleshooting recommendations.

## Overview

This project collects server health information such as CPU usage, memory usage, disk utilization, running processes, and authentication logs. It then generates a structured report and uses AI to analyze the data and provide troubleshooting guidance for system administrators.

The goal is to automate common diagnostic tasks and help administrators quickly identify potential issues.

## Features

## Core Features

- Automated Linux server health checks
- CPU, memory, and disk utilization monitoring
- Top process identification
- Listening port detection
- Authentication log parsing for failed SSH attempts
- Service status checks
- AI-powered troubleshooting recommendations

## Advanced Features

- Automated **system risk scoring**
- Alert detection for abnormal system conditions
- AI-generated troubleshooting guidance
- Designed for **continuous monitoring mode**

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

 ## Planned Monitoring Mode

Future versions will allow the assistant to run continuously like a lightweight monitoring tool.

Example usage:
 
