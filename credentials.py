class Credentials:
    """
    Class that generates new instances of users.
    """
    credentials_list = []

    def __init__(self,credentials_name,name,password,email):
        self.credentials_name = credentials_name
        self.name = name
        self.password = password
        self.email = email