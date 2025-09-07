import csv

with open('customers.csv', 'r') as customers_file:
  customers = csv.reader(customers_file)

  for customer in customers:
    id = customer[0]
    first_name = customer[2]
    last_name = customer[3]
    email = customer[9]
    print(f"Customer #{id}, {first_name} {last_name}, {email}")