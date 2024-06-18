def assess_password_strength(password):
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special = any(char in "!@#$%^&*()-_+=" for char in password)
    
    criteria = [length, uppercase, lowercase, digits, special]
    strength = sum(criteria)
    
    if all(criteria):
        strength_level = "Very Strong"
        feedback = "Excellent password!"
    elif strength == 4:
        strength_level = "Strong"
        feedback = "Strong password!"
    elif strength == 3:
        strength_level = "Moderate"
        feedback = "Not bad, but could be better."
    elif strength == 2:
        strength_level = "Weak"
        feedback = "Weak password, try adding more variety."
    else:
        strength_level = "Very Weak"
        feedback = "Very weak password, improve it!"
        
        if not length:
            feedback = "Password too short, use 8+ characters."
        elif not uppercase:
            feedback = "Add an uppercase letter."
        elif not lowercase:
            feedback = "Add a lowercase letter."
        elif not digits:
            feedback = "Add a digit."
        elif not special:
            feedback = "Add a special character (!@#$%^&*()-_+=)."
    
    return strength_level, feedback

def main():
    print("Password Strength Assessment Tool")
    while True:
        password = input("Enter a password to assess (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        
        strength_level, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength_level}")
        print(f"Feedback: {feedback}\n")

if __name__ == "__main__":
    main()

