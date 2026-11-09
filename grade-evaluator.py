import csv
import sys
import os


def load_csv_data():
    """
    Reads assignment records from a CSV file.
    """

    filename = input(
        "Enter the name of the CSV file to process "
        "(e.g., grades.csv): "
    )

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            required_fields = {
                'assignment', 'group', 'score', 'weight'
            }

            if not required_fields.issubset(reader.fieldnames or []):
                print("Error: CSV file is missing required columns.")
                sys.exit(1)

            for row in reader:
                if not all(row.values()):
                    print("Error: CSV contains an empty field.")
                    sys.exit(1)

                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        return assignments

    except (ValueError, KeyError) as error:
        print(f"Error: Invalid CSV data: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


def evaluate_grades(data):

    print("\n--- Processing Grades ---")

    
    if not data:
        print("Error: No assignment records found.")
        return

    
    for item in data:
        if not 0 <= item['score'] <= 100:
            print(
                f"Error: Invalid score for "
                f"{item['assignment']}. Scores must be 0-100."
            )
            return

        if item['weight'] < 0:
            print("Error: Assignment weights cannot be negative.")
            return


    for item in data:
        if item['group'] not in ['Formative', 'Summative']:
            print(f"Error: Invalid category: {item['group']}")
            return


    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for item in data:
        total_weight += item['weight']

        if item['group'] == 'Formative':
            formative_weight += item['weight']

        elif item['group'] == 'Summative':
            summative_weight += item['weight']

    if (round(total_weight, 2) != 100 or
            round(formative_weight, 2) != 60 or
            round(summative_weight, 2) != 40):

        print("Error: Assignment weights are incorrect.")
        print(f"Total weight: {total_weight}")
        print(f"Formative weight: {formative_weight}")
        print(f"Summative weight: {summative_weight}")
        print("Required: Total=100, Formative=60, Summative=40.")
        return
    formative_total = 0
    summative_total = 0

    for item in data:

        weighted_score = (
            item['score'] * item['weight'] / 100
        )

        if item['group'] == 'Formative':
            formative_total += weighted_score

        elif item['group'] == 'Summative':
            summative_total += weighted_score

    formative_grade = (
        formative_total / formative_weight
    ) * 100

    summative_grade = (
        summative_total / summative_weight
    ) * 100

    final_grade = formative_total + summative_total

    gpa = (final_grade / 100) * 5.0

    print(f"\nFormative Grade: {formative_grade:.2f}%")
    print(f"Summative Grade: {summative_grade:.2f}%")
    print(f"Final Grade: {final_grade:.2f}%")
    print(f"GPA: {gpa:.2f}/5.0")

    if formative_grade >= 50 and summative_grade >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    failed_formative = []

    for item in data:

        if (item['group'] == 'Formative'
                and item['score'] < 50):

            failed_formative.append(item)

    highest_weight = -1

    for item in failed_formative:

        if item['weight'] > highest_weight:
            highest_weight = item['weight']

    resubmission_options = []

    for item in failed_formative:

        if item['weight'] == highest_weight:
            resubmission_options.append(item['assignment'])
    print(f"\nFinal Status: {status}")

    if resubmission_options:

        print("\nEligible for Resubmission:")

        for assignment in resubmission_options:
            print(f"- {assignment}")

    else:
        print("\nNo failed formative assignments.")


if __name__ == "__main__":

    course_data = load_csv_data()

    evaluate_grades(course_data)
