import Customer, CustomerAddress

customer1 = Customer.Customer("C001", "John Doe", "john.doe@example.com")
customer1.customer_category = "Bank"
address1 = CustomerAddress.CustomerAddress(customer1, "New York", "NY", "10001")

print(customer1.get_customer_info())
print(address1.getCustName())  
print(f"Address: {address1.city}, {address1.state}, {address1.zip_code}")
print(f"Customer Category: {customer1.customer_category}")

