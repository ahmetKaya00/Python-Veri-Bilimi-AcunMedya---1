class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def __str__(self):
        return f"Müşteri: {self.name}, E-posta: {self.email}"