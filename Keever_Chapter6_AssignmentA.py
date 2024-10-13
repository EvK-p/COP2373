import re

# Function to validate phone numbers (Format: (XXX) XXX-XXXX or XXX-XXX-XXXX)
def validate_phone_number(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

# Function to validate social security numbers (Format: XXX-XX-XXXX)
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

# Function to validate zip codes (Format: XXXXX or XXXXX-XXXX)
def validate_zip_code(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

# Main function to get input from the user and validate it
def main():
    # Get user input
    phone = input("Enter a phone number (e.g., 123-456-7890 or (123) 456-7890): ")
    ssn = input("Enter a Social Security Number (e.g., 123-45-6789): ")
    zip_code = input("Enter a ZIP Code (e.g., 12345 or 12345-6789): ")

    # Validate the inputs
    is_phone_valid = validate_phone_number(phone)
    is_ssn_valid = validate_ssn(ssn)
    is_zip_code_valid = validate_zip_code(zip_code)

    # Display the results
    print(f"Phone number valid: {is_phone_valid}")
    print(f"SSN valid: {is_ssn_valid}")
    print(f"ZIP Code valid: {is_zip_code_valid}")

if __name__ == "__main__":
    main()
