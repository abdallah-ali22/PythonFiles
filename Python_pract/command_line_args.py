import sys

if len(sys.argv) == 1:
    print("tell me password after file name")
else:
    password = sys.argv[1]
    print("password:", password)