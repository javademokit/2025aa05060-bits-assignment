# speech_speed_estimator.py
# Live speaking speed (WPM) estimator using microphone
# Requirements: pip install speechrecognition pyaudio
#               (on Windows you may need: pip install pipwin && pipwin install pyaudio)

import speech_recognition as sr
import time
import sys
from datetime import datetime

def clear_line():
    """Clear current terminal line"""
    sys.stdout.write('\r' + ' ' * 100 + '\r')
    sys.stdout.flush()

def main():
    print("┌────────────────────────────────────────────────────┐")
    print("│       Real-time Speaking Speed Estimator (WPM)     │")
    print("│                                                    │")
    print("│  Requirements: microphone + internet connection    │")
    print("│  Press Ctrl+C to stop                              │")
    print("└────────────────────────────────────────────────────┘\n")

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Calibrating ambient noise... (be quiet for 3 seconds)")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=3)
    print("Calibration done. Start speaking normally!\n")

    total_words = 0
    start_time = time.time()
    last_speech_time = start_time

    print("Current speaking speed: ... WPM")
    print("─" * 50)

    try:
        while True:
            try:
                with mic as source:
                    audio = recognizer.listen(source, timeout=8, phrase_time_limit=12)

                text = recognizer.recognize_google(audio).strip()

                if text:
                    words = len(text.split())
                    total_words += words

                    now = time.time()
                    elapsed_minutes = (now - start_time) / 60

                    if elapsed_minutes > 0:
                        current_wpm = total_words / elapsed_minutes

                        clear_line()
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        status = (f"[{timestamp}]  Speed: {current_wpm:5.1f} WPM  "
                                 f"│ Words: {total_words:4d}  │ Last: \"{text[:50]}{'...' if len(text)>50 else ''}\"")
                        print(status)

                    last_speech_time = now

            except sr.WaitTimeoutError:
                # No speech for a while → show current average
                now = time.time()
                elapsed = (now - start_time) / 60
                if elapsed > 0:
                    avg_wpm = total_words / elapsed
                    clear_line()
                    print(f"Current average speed: {avg_wpm:5.1f} WPM   (silent...)")
                time.sleep(1)

            except sr.UnknownValueError:
                # Couldn't understand → skip
                pass

            except sr.RequestError as e:
                print(f"\nGoogle API error: {e}")
                break

    except KeyboardInterrupt:
        print("\n" + "═" * 50)
        total_time_sec = time.time() - start_time
        total_minutes = total_time_sec / 60

        if total_minutes > 0:
            final_wpm = total_words / total_minutes
            print(f"Final statistics:")
            print(f"  Total words spoken : {total_words:,}")
            print(f"  Total time         : {total_time_sec:.1f} seconds ({total_minutes:.2f} min)")
            print(f"  Average speed      : {final_wpm:.1f} words per minute")
        else:
            print("No speech detected during session.")

        print("Goodbye! 👋")

if __name__ == "__main__":
    main()