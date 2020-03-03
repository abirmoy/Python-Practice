#one.py

def func():
    print("FUNC() IN ONE.PY")

print("Top level in one.py")

if __name__ == "__main__":
    print("One.py is being run directly.")
else:
    print("One.py has been imported")