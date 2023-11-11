import sys
import os


additional_paths = ["./CG", "./mathh", "./sport"]


for path in additional_paths:
    full_path = os.path.abspath(path)
    sys.path.append(full_path)


import project
import mathpy
import sportscript


def main():
    print("Choose a script to run:")
    print("1. Run script1")
    print("2. Run script2")
    print("3. Run script3")

    choice = input("Enter your choice (1, 2, , 3 or q ): ")

    if choice == '1':
        project.run_quiz()
    elif choice == '2':
        mathpy.run_quiz()
    elif choice == '3':
        sportscript.run_quiz()

    elif choice == 'q':
        quit()

if __name__ == "__main__":
    main()
