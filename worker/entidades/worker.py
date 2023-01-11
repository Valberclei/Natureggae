class Worker():
    def __init__(self, nome, email, address, data_nas, sex, area, level, phone, link_social):
        self.__nome = nome
        self.__email = email
        self.__address = address
        self.__data_nas = data_nas
        self.__sex = sex
        self.__area = area
        self.__level = level
        self.__phone = phone
        self.__link_social = link_social

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
        self.__nome = email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def data_nas(self):
        return self.__data_nas

    @data_nas.setter
    def data_nas(self, data_nas):
        self.__data_nas = data_nas

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def link_social(self):
        return self.__link_social

    @link_social.setter
    def link_social(self, link_social):
        self.__link_social = link_social