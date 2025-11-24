"""
gradebook.py
Mini Project: GradeBook Analyzer
Author: Sansar Kumar
Date: 2025-11-02
Course: Programming for Problem Solving using Python


"""

import statistics
from typing import Dict, Tuple, List


def read_manual_input() -> Dict[str, int]:
    """Read student names and marks from user input."""
    marks = {}
    while True:
        try:
            n = int(input("How many students will you enter? "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(1, n + 1):
        name = input(f"Student #{i} name: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter name: ").strip()

        while True:
            try:
                m = input(f"{name}'s marks (0-100): ")
                score = int(m)
                if 0 <= score <= 100:
                    marks[name] = score
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter an integer value for marks.")

    return marks


# Statistical Analysis Functions

def calculate_average(marks_dict: Dict[str, int]) -> float:
    values = list(marks_dict.values())
    if not values:
        return 0.0
    return sum(values) / len(values)


def calculate_median(marks_dict: Dict[str, int]) -> float:
    values = sorted(marks_dict.values())
    if not values:
        return 0.0
    return statistics.median(values)


def find_max_score(marks_dict: Dict[str, int]) -> Tuple[str, int]:
    if not marks_dict:
        return ("", 0)
    name = max(marks_dict, key=lambda k: marks_dict[k])
    return (name, marks_dict[name])


def find_min_score(marks_dict: Dict[str, int]) -> Tuple[str, int]:
    if not marks_dict:
        return ("", 0)
    name = min(marks_dict, key=lambda k: marks_dict[k])
    return (name, marks_dict[name])


# Grade Assignment and Distribution

def assign_grade(score: int) -> str:
    if score >= 100:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 30:
        return "D"
    else:
        return "F"


def build_grades_dict(marks_dict: Dict[str, int]) -> Dict[str, str]:
    return {name: assign_grade(score) for name, score in marks_dict.items()}


def grade_distribution(grades_dict: Dict[str, str]) -> Dict[str, int]:
    distribution = {g: 0 for g in ["A", "B", "C", "D", "F"]}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution


# Pass/Fail filter (pass >= 30)

def pass_fail_lists(marks_dict: Dict[str, int]) -> Tuple[List[str], List[str]]:
    passed_students = [name for name, score in marks_dict.items() if score >= 30]
    failed_students = [name for name, score in marks_dict.items() if score < 30]
    return passed_students, failed_students


# Results Table

def print_results_table(marks_dict: Dict[str, int], grades_dict: Dict[str, str]) -> None:
    name_w = max((len(name) for name in marks_dict), default=4)
    header = f"{'Name'.ljust(name_w)}\tMarks\tGrade"
    print(header)
    print('-' * (name_w + 20))
    for name, mark in marks_dict.items():
        grade = grades_dict.get(name, "")
        print(f"{name.ljust(name_w)}\t{str(mark).ljust(5)}\t{grade}")


def analysis_report(marks_dict: Dict[str, int]) -> None:
    if not marks_dict:
        print("No student data to analyze.")
        return

    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    max_name, max_score = find_max_score(marks_dict)
    min_name, min_score = find_min_score(marks_dict)

    grades = build_grades_dict(marks_dict)
    distribution = grade_distribution(grades)
    passed, failed = pass_fail_lists(marks_dict)

    print('\n=== Analysis Summary ===')
    print(f"Average score: {avg:.2f}")
    print(f"Median score: {med}")
    print(f"Max score: {max_score} ({max_name})")
    print(f"Min score: {min_score} ({min_name})")

    print('\nGrade distribution:')
    for g in ['A', 'B', 'C', 'D', 'F']:
        print(f"{g}: {distribution.get(g,0)}")

    print(f"\nPassed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

    print('\nResults Table:')
    print_results_table(marks_dict, grades)


def main_menu():
    print("\nWelcome to GradeBook Analyzer (Manual Input Mode)")
    while True:
        print("\nMenu:")
        print("1) Enter student marks manually")
        print("2) Exit")
        choice = input("Choose an option (1-2): ").strip()

        if choice == '1':
            marks = read_manual_input()
            analysis_report(marks)
        elif choice == '2':
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == '__main__':
    main_menu()
