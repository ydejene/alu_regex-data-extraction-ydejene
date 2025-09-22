# Regex Data Extraction Tool

## Project Overview

This project demonstrates the power of Regular Expressions (Regex) in extracting structured data from raw text. It is implemented in Python and targets multiple data formats such as emails, phone numbers, URLs, and more.

The program processes input strings, applies carefully designed regex patterns, and outputs the results in a structured, easy-to-read format.

## Features
The tool extracts the following types of data:

- **Email addresses**
- **Phone numbers(various formats, e.g., 123-456-7890, (123) 456-7890)**
- **URLS**
- **Credit card numbers**
- **Currency amounts (e.g., $1,234.56)**
- **Times (12-hour and 24-hour formats, e.g., 2:30 PM, 14:30)**
- **HTML tags**
- **Hashtags**

## Setup Instructions
1. Clone the respository: 
``` bash
git clone https://github.com/ydejene/alu_regex-data-extraction-ydejene.git
```

2. Navigate to the project folder:
```bash
cd alu_regex-data-extraction-ydejene
```

3. Run the script:
```bash
python dataExtractionWithRegex.py
```

4. Modify the sample text inside the script to test your own data.

## Sample Output
Example run:
```bash
$ ./dataExtractionWithRegex.py
Emails: ['resstassure@fmail.com']
Urls: ['https://www.example.com']
Phones: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit_cards: ['1234-5678-9012-3456']
Times: ['2:30 PM', '14:30']
Html_tags: ['<div class="example">', '</div>']
Hashtags: ['#python', '#RegexHackathon']
Currencys: ['$1,234.56']
```

## Edge-Case Handling
The regex patterns are designed to handle tricky cases such as:
 - **Malformed emails →** test@@mail.com (skipped)
 - **Phone formats →** 123-456-7890, 123.456.7890, (123) 456-7890
 - **Credit cards →** 1234-5678-9012-3456 or 1234 5678 9012 3456
 - **Currencies →** $1,234.56, $1000, $0.99
 - **Times →** both 12-hour (2:30 PM) and 24-hour (14:30)

 ## Repository Organization

 - **dataExtractionWithRegex.py →** main Python script with regex patterns
 - **README.md →** project overview and documentation
 - **Sample inputs →** included inside the script for easy testing

 Meaningful commits are made throughout development to track progress.

 ## License
This project is licensed under the MIT License.

