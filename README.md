# AI Server Troubleshooting Assistant

🚧 **Project Status:** Work in Progress — currently building core diagnostics and AI analysis modules.

AI-powered Linux server diagnostics tool with automated risk scoring and troubleshooting recommendations.

---

# Overview

The **AI Server Troubleshooting Assistant** is a Python-based system administration tool designed to automate Linux server diagnostics and troubleshooting.

The tool collects system health information such as:

* CPU usage
* Memory usage
* Disk utilization
* Running processes
* Listening network ports
* Authentication logs

It then generates a structured **server health report** and uses AI to analyze the data and provide troubleshooting guidance for system administrators.

The goal is to automate common diagnostic tasks and help administrators quickly identify potential issues.

---

# Features

## Core Features

* Automated Linux server health checks
* CPU, memory, and disk utilization monitoring
* Top process identification
* Listening port detection
* Authentication log parsing for failed SSH attempts
* Service status checks
* AI-powered troubleshooting recommendations

---

## Advanced Features

* Automated **system risk scoring**
* Alert detection for abnormal system conditions
* AI-generated troubleshooting guidance
* Designed for **continuous monitoring mode**

---

# Technologies Used

* Python
* `psutil`
* OpenAI API
* Linux system logs
* Regular Expressions (Regex)

---

# Project Goals

This project was created to combine **AI with real-world system administration tasks**, including:

* system monitoring
* log analysis
* infrastructure troubleshooting
* automation

Rather than building a generic chatbot, this project focuses on creating a **practical tool that reflects the daily responsibilities of a system administrator.**

It is also designed to integrate with a **homelab environment for testing and future improvements.**

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOURUSERNAME/ai-server-troubleshooting-assistant.git
cd ai-server-troubleshooting-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create an environment file:

```bash
cp .env.example .env
```

Add your OpenAI API key to `.env`.

---

# Usage

Run the tool:

```bash
python app.py
```

Future monitoring mode:

```bash
python app.py --monitor
```

Monitoring mode will repeatedly check system metrics and generate alerts when abnormal conditions are detected.

---

# Project Architecture

```
ai-server-troubleshooting-assistant
│
├── app.py               # Main application entry point
├── collector.py         # Collects system metrics
├── log_parser.py        # Parses Linux authentication logs
├── formatter.py         # Formats system health reports
├── risk_scoring.py      # Calculates system risk score
├── ai_analyzer.py       # Sends reports to OpenAI for analysis
├── monitor.py           # Future continuous monitoring module
├── requirements.txt
├── README.md
```

---

# Future Improvements

Planned improvements include:

* Windows event log support
* Web dashboard using Flask
* Automated alert notifications
* Scheduled monitoring
* Firewall integration
* Additional log analysis (Apache, nginx, firewall logs)

---

# Author

**Elizabeth Gallagher**

Cybersecurity and IT student focused on:

* Systems Administration
* Python automation
* Homelab infrastructure
* Security tooling

Example usage:
 
bash
python app.py --monitor
