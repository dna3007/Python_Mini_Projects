import re

def clean_phone_number(phone_number):
    phone_number = re.sub(r'\+\d{1,3}', '', phone_number)
    phone_number = re.sub(r'[\(\)\s\-]', '', phone_number)

    return phone_number


phone_number = "+141 (95) 10-846423"
cleaned_number = clean_phone_number(phone_number)
print(cleaned_number)
