#!/usr/bin/python
#-*- coding: utf-8 -*-

from Farmacia.Persona import Persona
from Farmacia.Persona import Persona

class Proveedor(Persona, Persona):
    def __init__(self):
        self.telefono = None
        self.empresa = None

    def setTelefono(self,telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setEmpresa(self,empresa):
        self.empresa = empresa

    def getEmpresa(self ):
        return self.empresa

    def mostrarDatos(self ):
        print("\nBnaco: "+super().banco)
        print("\npago: "+super().pago)
        print("\nnumero tarjeta: "+self.numtar)
        

    def pedirDatos(self):
        super.nombre = input("Banco: ")
        super.apellido = input("Credito o contado: ")
        self.telefono = input("numero tarjeta: ")
       

