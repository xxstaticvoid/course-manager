#
# AUTHOR = "Joseph Ebersole"
# DATE = "31-AUG-2025"
# DESC = "Load classes from csv into data stuct and perform operations"

import csv
from typing import List


from Course import Course

#Path to CSV file
csv_file_path = "./classes.csv"

course_list: List[Course] = []

def load_courses(cleaned_csv_row):
    title, number = cleaned_csv_row[0], cleaned_csv_row[1]
    temp_course = Course(len(course_list), title, number)
    course_list.append(temp_course)

def read_from_file(csv_file_path):
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                for element in row:
                    element = element.strip()
                load_courses(row)

    except FileNotFoundError:
        print("File not found")
        return 404
    except Exception as e:
        print(e)
        return 401
    else:
        return 0


def print_menu():
    print("==================")
    print("1. Add course")
    print("2. Remove course")
    print("3. Print courses")
    print("9. Exit")
    print("==================")


def print_title():
    print(r"  ____                            __  __                                   ")
    print(r" / ___|___  _   _ _ __ ___  ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ")
    print(r"| |   / _ \| | | | '__/ __|/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|")
    print(r"| |__| (_) | |_| | |  \__ \  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   ")
    print(r" \____\___/ \__,_|_|  |___/\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   ")
    print(r"                                                           |___/           ")
    print("\n")
    ### CREDIT = "www.asciiart.eu"


def main() -> int:

    result = read_from_file(csv_file_path)
    if result != 0:
        return result

    print_title()

    while True:
        print_menu()
        try:
            user_input = int(input("Enter your choice --> "))
        except ValueError:
            print("Invalid input")
            return 403
        if user_input == 9:
            break
        elif(user_input == 1):
            ##add course
            temp_num = input("What is the course name you want added? --> ")
            temp_name = input("What is the course number you want added? --> ")
            temp_course = Course(len(course_list), temp_num, temp_name)
            course_list.append(temp_course)

        elif(user_input == 2):
            ##remove course
            choice = input("What is the course number you want removed? --> ")
            for course in course_list:
                if course.get_course_number() == choice:
                    course_list.remove(course)
                    del course
                    break


        elif(user_input == 3):
            ##get data
            for course in course_list:
                print(course)
            print("\n-----")

            ## Each class is 3 credits
            credits_left: int = 3 * len(course_list)
            terms_left: int = -(-len(course_list) // 2) ##2 classes per term, round up

            print(f"Credits Left: {credits_left}")
            print(f"Terms Left: {terms_left}   |    Total Week Remaining: {terms_left * 8}")

        else:
            print("Not valid input\n")



    return 0

if __name__ == "__main__":
    result = main()
    print(f"Ended with: {result}")

