class User:
    """Un utilisateur."""

    def __init__(self, name, contact_method):
        """Initialise un nom et une methode de contact."""
        if len(name) < 6:
            raise ShortName()
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        """Envoit un message."""
        self.contact_method.send(message)

class ShortName(Exception):
    def __init__(self, name, *args, **kwargs):
        msg = f'Name is too short minimum 6 : {name}'
        super().__init__(msg, *args, **kwargs)

user = User('tesf', 'courrier')
print(user.name)