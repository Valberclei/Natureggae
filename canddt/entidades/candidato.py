class Candidato():
    def __init__(self, nome, sexo, idade, nivel, formacao, pix, celular):
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade
        self.__nivel = nivel
        self.__formacao = formacao
        self.__pix = pix
        self.__celular = celular

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao

    @property
    def pix(self):
        return self.__pix

    @pix.setter
    def pix(self, pix):
        self.__pix = pix

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular