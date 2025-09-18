#!/usr/bin/env python

import re

# a dictionary to store all the patterns as a key(pattern-type) value(respective regex) pair
PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url": r"https?://[^\s]+",
    "phone": r"(?:\(\d{3}\)\s*|\d{3}[-.])?\d{3}[-.]\d{4}",
    "credit_card": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?\b",
    "html_tag": r"<[^>]+>",
    "hashtag": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
}

# define a function that will extract the required data's using the power of regex
def extract_data (text: str, pattern_type: str) -> list:
    # validation for the selected pattern type 
    if pattern_type not in PATTERNS:
        raise ValueError (f"unknown pattern: {pattern_type}")
    # a variable to store the regular expression
    regex = PATTERNS[pattern_type]
    #varible that will store the matches and return them
    result = re.findall(text, regex)
    return result

# demo test
if __name__ == "__main__":
    sample_test = """
    Hello, I am Yonas. 
    My email is resstassure@fmail.com, and I visit https://www.example.com often.
    Call me at (123) 456-7890 or 123-456-7890. 
    My credit card: 1234-5678-9012-3456. 
    Let's meet at 2:30 PM or 14:30.
    Here’s some HTML: <div class="example">Hello</div>.
    Don’t forget the hashtags: #python #RegexHackathon.
    That book cost $1,234.56.
    """
    # for loop to iterate over a list of pattern types for testing
    user_input = ["email", "url", "phone", "credit_card", "time", "html_tag", "hashtag", "currency"]
    for category in user_input:
        """ passing the category to the above fucntion with the sample test data and print the result"""
        matches = extract_data(sample_test, category)
        """prints the category with the matching data in a clear formated way"""
        print(f"{category.capitalize()}s: {matches}")