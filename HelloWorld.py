#!/usr/bin/env python
import os
import ctypes

# Carrega a lib para uma variavel 
libLocal = ctypes.CDLL("./HelloWorld_lib.so")

print("A soma dos numeros:")

# chama os metodos dentro da lib
print(libLocal.somar(5, 6))
print(libLocal.HelloWorld_dobro (5))
