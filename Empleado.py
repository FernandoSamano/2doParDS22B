#!/usr/bin/python
#-*- coding: utf-8 -*-

from Farmacia.metodopago import metodopago
from Farmacia.metodopago import metodopago

class Empleado(metodopago, metodopago):
    def __init__(self):
        self.tipo = None

    def setTipo(self,tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo



    def pedirDatos(self):
        super.banco = input("banco: ")
        super.pago = input("pago: ")
        self.tipo = input("Tipo: ")
      

    def mostrarDatos(self):
        print("\nbanco: "+super().banco)
        print("\ncredito o contando: "+super().pago)
        print("\nnumero tarjeta: "+self.numtar)


