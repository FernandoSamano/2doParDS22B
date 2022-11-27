#!/usr/bin/python
#-*- coding: utf-8 -*-

from Farmacia.Empleado import Empleado

class Persona():
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

