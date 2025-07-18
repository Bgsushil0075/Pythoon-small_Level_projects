import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_number_details(number_str, region='US'):
    try:
        # Parse the number
        number = phonenumbers.parse(number_str, region)

        # Check if it's a valid number
        if not phonenumbers.is_valid_number(number):
            return "Invalid phone number."

        # Get region info
        location = geocoder.description_for_number(number, 'en')

        # Get carrier info
        sim_carrier = carrier.name_for_number(number, 'en')

        return {
            "Number": number_str,
            "Location": location,
            "Carrier": sim_carrier,
            "Valid": True
        }

    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    phone_number = input("Enter a phone number with country code (e.g., +14155552671): ")
    details = get_phone_number_details(phone_number)
    print(details)
