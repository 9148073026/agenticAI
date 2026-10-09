from Customer import Customer
class CustomerAddress(Customer):
    
    def getCustName(self):
        return f"customer name : {self.name}"

    Customer1 = Customer(101,"sai","sai@abc.com")
    print(Customer1.name)
