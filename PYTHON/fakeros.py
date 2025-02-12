from faker import Faker

fake = Faker()

print(fake.name())         # Random full name
print(fake.address())      # Random address
print(fake.email())        # Random email
print(fake.phone_number()) # Random phone number
print(fake.text())         # Random text
