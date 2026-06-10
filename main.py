import os
import time

def clear_screen():
    # wipe console, works for both windows and unix handles
    os.system('cls' if os.name == 'nt' else 'clear')

# main entry point
clear_screen()
print('==================================================')
print('  Welcome to the Python Syntax & Logic Quiz!     ')
print('==================================================')
print('Test your knowledge of basic programming concepts.\n')

input("Press ENTER to start the quiz...")
clear_screen()

# score tracker
score = 0

try:
    print("Select a level to practice:")
    print("1) Level 1: Variable Syntax")
    print("2) Level 2: Loop Structures")
    print("3) Level 3: Data Types (Advanced)")
    
    cha_lvl = int(input("\n Choose level (1, 2, or 3): "))
    clear_screen()

    # =====================================================================
    # LVL 1: VARS
    # =====================================================================
    if cha_lvl == 1:
        print('Loading Level 1...')
        time.sleep(1.0)
        clear_screen()
        
        print("=== LEVEL 1: VARIABLE SYNTAX ===")
        print("Which variable declaration is valid in Python?\n")
        print("1) 1st_number = 10")
        print("2) my-number = 10")
        print("3) my_number = 10")
        
        answer = int(input("\nYour answer (1, 2 or 3): "))
        
        if answer == 3:
            print("\nCORRECT! Excellent start.")
            score += 1
        else:
            print("\nWRONG ANSWER.")
            print("Explanation: Var names cant start with numbers or use hyphens. Basic stuff.")

    # =====================================================================
    # LVL 2: LOOPS
    # =====================================================================
    elif cha_lvl == 2:
        print('Loading Level 2...')
        time.sleep(1.0)
        clear_screen()
        
        print("=== LEVEL 2: THE WHILE LOOP TRAP ===")
        print("Look at these loop structures. Which one runs exactly 5 times?\n")
        print("1) i = 0\n   while i < 5:\n       print(i)\n       i += 1")
        print("2) i = 1\n   while i <= 5:\n       print(i)")
        print("3) while False:\n       print('Hello')")
        
        answer = int(input("\nYour answer (1, 2 or 3): "))
        
        if answer == 1:
            print("\nCORRECT! You understand loop counters and increments.")
            score += 1
        else:
            print("\nWRONG ANSWER.")
            print("Explanation: Option 2 is a rip, it triggers an infinite loop because 'i' never increments.")

    # =====================================================================
    # LVL 3: TYPES
    # =====================================================================
    elif cha_lvl == 3:
        print('Loading Level 3...')
        time.sleep(1.0)
        clear_screen()
        
        print("=== LEVEL 3: THE ULTIMATE DATA TYPE TEST ===")
        print("What is the result of executing this code in Python?\n")
        print("print('5' + 5)\n")
        print("1) 10")
        print("2) 55")
        print("3) TypeError (Crash)")
        
        answer = int(input("\nYour answer (1, 2 or 3): "))
        
        if answer == 3:
            print("\nEXCELLENT! You beat the system.")
            score += 1
        else:
            print("\nWRONG ANSWER.")
            print("Explanation: Python doesnt do implicit type coercion here, it just throws a TypeError.")
            
    else:
        print('Invalid choice. Please restart and choose 1, 2, or 3.')

except ValueError:
    # foolproofing if user types strings instead of ints
    print('\nError: Invalid input format. Please enter numbers only!')

# wrap up
print('\n==================================================')
print(f"Quiz finished! Your final score: {score}/1")
print('==================================================')

# keep window alive, prevent instant termination
input("\nPress ENTER to exit the program...")