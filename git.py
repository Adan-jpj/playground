import random
import time
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

TEMPERATURE_THRESHOLD = 80
VIBRATION_THRESHOLD = 5.0

LOG_MESSAGES = [
    "System check complete. All systems normal.",
    "Temperature stable.",
    "Error: Overheat detected!",
    "Vibration levels critical!",
    "Routine check passed.",
    "Warning: Vibration out of range.",
    "Machine running smoothly."
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def read_sensor_data():
    """Simulate sensor data for temperature and vibration"""
    temperature = random.uniform(50, 100)
    vibration = random.uniform(1.0, 7.0)
    return temperature, vibration

def check_for_errors(temp, vib, log):
    """Check if any readings or logs indicate an error"""
    errors = []

    if temp > TEMPERATURE_THRESHOLD:
        errors.append(f"Temperature too high: {temp:.2f} degrees Celsius")

    if vib > VIBRATION_THRESHOLD:
        errors.append(f"Vibration level too high: {vib:.2f} millimeters per second")

    if "error" in log.lower() or "warning" in log.lower():
        errors.append(f"Log alert: {log}")

    return errors

print("Monitoring machine... (press Ctrl+C to stop)")
speak("Monitoring machine started")

try:
    while True:
        temp, vib = read_sensor_data()
        log = random.choice(LOG_MESSAGES)
        errors = check_for_errors(temp, vib, log)

        print(f"\nTemperature: {temp:.2f}°C | Vibration: {vib:.2f} mm/s | Log: {log}")
        speak(f"Temperature {temp:.2f} degrees. Vibration {vib:.2f} millimeters per second.")

        if errors:
            print("[!] ERRORS DETECTED:")
            for error in errors:
                print("   -", error)
                speak(error)
        else:
            print("System normal.")
            speak("System normal.")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
    speak("Monitoring stopped.")

finally:
    engine.stop()
