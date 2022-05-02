# Idea of this program originated from Python Crash Course Book
import sys

if (sys.argv[1] == '10'):
    file_path = 'Pi10DP.txt'
elif (sys.argv[1] == '100'):
    file_path = 'Pi100DP.txt'
elif (sys.argv[1] == '1000'):
    file_path = 'Pi1KDP.txt'
elif (sys.argv[1] == '10000'):
    file_path = 'Pi10KDP.txt'
elif (sys.argv[1] == '100000'):
    file_path = 'Pi100KDP.txt'
elif (sys.argv[1] == '1000000'):
    file_path = 'Pi1MDP.txt'
elif (sys.argv[1] == '1250000'):
    file_path = 'Pi125MDP.txt'
else:
    print("Invalid Input!")
    exit()

with open(file_path) as pi:
    lines = pi.readlines()
    bdate = input("Enter your birthday(mmddyy): ")

all_pi = "3"
for line in lines:
    all_pi += line[:-1]

if bdate in all_pi:
        print("Yea!")
else:
    print("Nah!")
