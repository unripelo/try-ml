import sys
import threading
import time

SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
SPINNER_INTERVAL = 0.08


def _spinner_worker(stop_event: threading.Event, message: str) -> None:
    """Run spinner animation until stop_event is set."""
    idx = 0
    while not stop_event.is_set():
        frame = SPINNER_FRAMES[idx % len(SPINNER_FRAMES)]
        sys.stdout.write(f"\r  {frame}  {message}")
        sys.stdout.flush()
        idx += 1
        stop_event.wait(SPINNER_INTERVAL)
    sys.stdout.write("\r" + " " * (len(message) + 8) + "\r")
    sys.stdout.flush()

