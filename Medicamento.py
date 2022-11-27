#!/usr/bin/python
#-*- coding: utf-8 -*-

class Medicamento:
    def __init__(self):
        self.nombre = None
        self.marca = None
        self.proveedor = None

    def setNombre(self,nombre):
        self.nombre= nombre

    def getNombre(self):
        return self.nombre

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def pedirMedicamento(self):
        self.nombre = input("Nombre: ")
        self.marca = input("Marca: ")
        self.proveedor = input("Proveedor: ")

    def mostrarMedicamento(self):
        print("Nombre de medicamento: "+self.nombre)
        print("Marca de medicamento: "+self.marca)
        

    
Medicamento=Medicamento()