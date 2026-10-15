from Customer import Customer
class CustomerAddress(Customer):

    def __init__(self, customer, city: str, state: str, zip_code: str):
        super().__init__(customer.customer_id, customer.name, customer.email)
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def getCustName(self):
        return f"customer name : {self.name}"

    Customer1 = Customer(101,"sai","sai@abc.com")
    print(Customer1.name)
