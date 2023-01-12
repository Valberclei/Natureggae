class Contact():
    def __init__(self, nome, email, message):
        self.__nome = nome
        self.__email = email
        self.__message = message

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message