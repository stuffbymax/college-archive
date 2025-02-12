from faker import Faker
import pandas as pd

fake = Faker()

data = {
    "Name": [fake.name() for _ in range(5)],
    "Bank IBAN": [fake.iban() for _ in range(5)],
    "Credit Card": [fake.credit_card_number() for _ in range(5)],
    "CVV": [fake.credit_card_security_code() for _ in range(5)],
    "Expiry": [fake.credit_card_expire() for _ in range(5)]
}

df = pd.DataFrame(data)
print(df)



# ~ for _ in range(100):  # Generate 100 records
    # ~ print(f"Name: {fake.name()}")
    # ~ print(f"Address: {fake.address()}")
    # ~ print(f"Email: {fake.email()}")
    # ~ print(f"Phone: {fake.phone_number()}")
    # ~ print(f"Text: {fake.text()}")
    # ~ print(f"Bank IBAN: {fake.iban()}")
    # ~ print(f"SWIFT Code: {fake.swift()}")
    # ~ print(f"Credit Card: {fake.credit_card_number()} ({fake.credit_card_provider()})")
    # ~ print(f"CVV: {fake.credit_card_security_code()}")
    # ~ print(f"Expiry Date: {fake.credit_card_expire()}")
    # ~ print("=" * 50)
