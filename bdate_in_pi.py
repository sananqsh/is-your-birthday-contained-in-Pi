# Idea of this program originated from Python Crash Course Book
import sys
if len(sys.argv) == 1:
    file_path = 'Pi1MDP.txt'
    accuracy = 1000000
else:
    if (sys.argv[1] == '10'):
        file_path = 'Pi10DP.txt'
        accuracy = 10
    elif (sys.argv[1] == '100'):
        file_path = 'Pi100DP.txt'
        accuracy = 100
    elif (sys.argv[1] == '1000'):
        file_path = 'Pi1KDP.txt'
        accuracy = 1000
    elif (sys.argv[1] == '10000'):
        file_path = 'Pi10KDP.txt'
        accuracy = 10000
    elif (sys.argv[1] == '100000'):
        file_path = 'Pi100KDP.txt'
        accuracy = 100000
    elif (sys.argv[1] == '1000000'):
        file_path = 'Pi1MDP.txt'
        accuracy = 1000000
    elif (sys.argv[1] == '1250000'):
        file_path = 'Pi125MDP.txt'
        accuracy = 1250000
    else:
        print("Invalid Input!")
        exit()

try:
    with open(file_path) as pi:
        lines = pi.readlines()
except FileNotFoundError:
    print(f"file '{file_path}' does not exist!")

bdate = input("Enter your birthday(mmddyy): ")
if (not bdate.isdigit() or len(bdate) != 8):
    print("Most probably not a date, but whatever...")

pi_str = "3"
for line in lines:
    pi_str += line[:-1]

found_dig = pi_str.find(bdate)
if bdate in pi_str:
        print(f"Your birthday appears in the digit:{found_dig} in Pi number!")
else:
    print(f"Nah! Your birthday does not apear in first {accuracy} digits of Pi")
