from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

try:
    parts = user_input.split(",")
    cleaned_strings = strip_whitespaces(parts)
    number_list = [float(item) for item in cleaned_strings]
    unique_numbers = remove_duplicates(number_list)

    print(f"Cleaned and unique data: {unique_numbers}")
    print("-" * 20)
    print(f"Mean: {calculate_mean(unique_numbers):.2f}")
    print(f"Maximum: {find_maximum(unique_numbers)}")
    print(f"Minimum: {find_minimum(unique_numbers)}")

except ValueError:
    print("Data Error: Please make sure you only enter numbers separated by commas.")