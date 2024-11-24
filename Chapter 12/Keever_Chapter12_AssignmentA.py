import numpy as np
import csv

# Import the CSV file information
def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip to next line
        data = []
        for row in reader:
            data.append(row[2:])  # Take exam scores
    return np.array(data, dtype=int)

# Print the first few rows of the dataset
def first_rows(data, num_rows=5):
    print("First few rows of the dataset:")
    print(data[:num_rows])

# Calculate statistics
def calculate_statistics(data):
    print("\nExam Statistics:")
    num_exams = data.shape[1]
    for n in range(num_exams):
        exam_scores = data[:, n]
        print(f"Exam {n+1}:")   # Print the statstics previously calculated
        print(f"    Mean: {np.mean(exam_scores):.2f}")
        print(f"    Median:: {np.median(exam_scores):.2f}")
        print(f"    Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"    Minimum: {np.min(exam_scores)}")
        print(f"    Maximum: {np.max(exam_scores)}")

# Calculate the overall statistics
def calculate_overall_statistics(data):
    all_scores = data.flatten()
    print("\nOverall statistics for all exams combined:")   # Print previously stated overall statistics
    print(f"    Mean: {np.mean(all_scores):.2f}")
    print(f"    Median: {np.median(all_scores):.2f}")
    print(f"    Standard Deviation: {np.std(all_scores):.2f}")
    print(f"    Minimum: {np.min(all_scores)}")
    print(f"    Mamimum: {np.max(all_scores)}")

# Determine how many students passed or failed
def pass_fail_statistics(data, passing_grade=60):
    num_exams = data.shape[1]
    for n in range(num_exams):
        exam_scores = data[:, n]
        passed = np.sum(exam_scores >= passing_grade)
        failed = np.sum(exam_scores < passing_grade)
        print(f"\nExam {n+1}:")     # Print the information
        print(f"    Passed: {passed}")
        print(f"    Failed: {failed}")

# Calculate the overall pass percentage based on exam scores
def overall_pass_percentage(data, passing_grade=60):
    total_students = data.shape[0] * data.shape[1]
    passed_students = np.sum(data >= passing_grade)
    pass_percentage = (passed_students / total_students) * 100
    print(f"\nOverall pass percentage: {pass_percentage:.2f}%")

# Calling the main
def main():
    filename = 'grades.csv'
    data = load_data(filename)
    first_rows(data)
    calculate_statistics(data)
    calculate_overall_statistics(data)
    pass_fail_statistics(data)
    overall_pass_percentage(data)

# Ensuring the main function is called only when the script is direct
if __name__ == '__main__':
    main()
