class Customer():
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_info(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }
