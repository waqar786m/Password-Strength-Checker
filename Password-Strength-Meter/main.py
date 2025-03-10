import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = ""

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback += "❌ Password should be at least 8 characters long.\n"
    
    # Uppercase and Lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback += "❌ Include both uppercase and lowercase letters.\n"
    
    # Digits check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback += "❌ Add at least one number (0-9).\n"
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback += "❌ Include at least one special character (!@#$%^&*).\n"
    
    # Strength Rating
    if score == 4:
        feedback += "✅ Strong Password!"
    elif score == 3:
        feedback += "⚠️ Moderate Password - Consider adding more security features."
    else:
        feedback += "❌ Weak Password - Improve it using the suggestions above."
    
    return feedback

# Streamlit UI
st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    result = check_password_strength(password)
    st.text_area("Feedback", result, height=150)
