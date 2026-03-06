import time

def start_monitoring(interval=60):
    """
    Continuously monitor the system every X seconds.
    """

    print("Monitoring mode started. Press Ctrl+C to stop.")

    try:
        while True:
            print("Running system health check...")
            # future: call main diagnostic function here
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
