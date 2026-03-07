import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def analyze_system(cpu, memory, disk, failed_logins):
	prompt = f"""
You are a Linux system administrator.

Analyze the following system metrics and provide a short health summary.

CPU Usage: {cpu}%
Memory Usage: {memory}%
Disk Usage {disk}%
Failed SSH Logins: {failed_logins}

Explain whether the system looks healthy and if any action should be taken.
"""

	response = client.responses.create(
		model="gpt-4.1-mini",
		input=prompt,
	)

	return response.output_text


