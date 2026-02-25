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

def run_with_loading(duration: float, message: str) -> None:
    """Execute a timed operation with a loading spinner."""
    stop_event = threading.Event()
    spinner = threading.Thread(
        target=_spinner_worker,
        args=(stop_event, message),
        daemon=True,
    )
    spinner.start()
    time.sleep(duration)
    stop_event.set()
    spinner.join(timeout=0.5)


def _agent_header(title: str) -> None:
    """Print a styled agent task header."""
    width = 52
    print(f"\n┌{'─' * (width - 2)}┐")
    print(f"│  ●  {title:<{width - 8}}│")
    print(f"└{'─' * (width - 2)}┘")

def _agent_line(label: str, value: str) -> None:
    """Print a formatted agent info line."""
    print(f"   →  {label}: {value}")


def _agent_success(message: str) -> None:
    """Print a success completion message."""
    print(f"   ✓  {message}\n")


def handle_prompt(prompt: str) -> None:
    """Process and analyze the user prompt."""
    _agent_header("PROMPT ANALYSIS")
    _agent_line("Input", prompt)
    print()
    run_with_loading(5, "Analyzing intent and planning workflow...")
    _agent_success("Prompt understood. Workflow initialized.")
