import random
import string

def generate_password(length=12):
    # Define the character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure the password has a mix of all character types
    all_characters = lower + upper + digits + symbols
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
password = generate_password(12)  # Generates a 12-character password
print("Generated Instagram Password:",(password))
      
      