import time
import os
import platform
import winsound

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def format_time(seconds):
    minutes = seconds // 60
    second_remainder = seconds % 60
    return f"{minutes:02d}:{second_remainder:02d}"

def countdown(seconds,label):
    for remaining in range(seconds,0,-1):
        clear_screen()
        print(f"\n{label}")
        print(f"\n Time remaining: {format_time(remaining)}")

        if label == "Work Session":
            print("\n Focus on work!")
        elif "break" in label:
            print("\n take a break...")
        time.sleep(1)

    clear_screen()
    print(f"\n {label} Completed")
    if platform.system() == "Windows":
         winsound.Beep(1000,500)
    else:
         print("🔔")
              

def pomodoro_timer():
    try:
        clear_screen()
        print("\n==== Pomodoro Timer ====")

        # default settings
        work_minutes = 25
        short_break_minutes = 5
        long_break_minutes = 15
        cycles = 4

        customize = input(
                "\nUse default settings (25min work, 5min short break, 15min long break?) (yes/no):").lower()
        if customize.startswith("n"):
            try:
                    work_minutes = int(
                        input("\nEnter work session length (minutes): "))
                    short_break_minutes = int(
                        input("Enter short break length (minutes): "))
                    long_break_minutes = int(
                        input("Enter long break length (minutes): "))
                    cycles = int(
                        input("Enter number of cycles befre a long break: "))
            except ValueError:
                    print("\nInvalid input! Using default settings")
                    time.sleep(2)

        clear_screen()
        print(f"\n Starting Pomodoro Timer with:")
        print(f"• {work_minutes} minute work sessions")
        print(f"• {short_break_minutes} minute short breaks")
        print(f"• {long_break_minutes} minute long break after {cycles} cycles")
        print(f"• Press Ctrl+C at any time to exit")
        input("\nPress Enter to begin...")

        # covert minutes to seconds
        work_seconds = work_minutes * 60
        short_break_seconds = short_break_minutes * 60
        long_break_seconds = long_break_minutes * 60

        completed_cycles = 0
        
        while True:
                countdown(work_seconds, "Work Session")
                completed_cycles += 1

                if completed_cycles % cycles == 0:
                    input("\nTime for a long break! Press Enter to start your break...")
                    countdown(long_break_seconds, "Long Break")
                    input(
                        "\nLong break complete! Press Enter to start the next work session...")
                else:
                    input("\nTime for a short break! Press Enter to start your break...")
                    countdown(short_break_seconds, "Short Break")
                    input(
                        "\nShort break complete! Press Enter to start the next work session...")
                    
    except KeyboardInterrupt:
         clear_screen()
         print("GOODBYE!")


 

pomodoro_timer()