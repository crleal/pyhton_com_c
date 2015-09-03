Shared Objects no Python

Como gosto muito de escrever em python resolvi fazer algo parecido com o post anterior só que desta vez o python acessando uma lib em c.

Eu utilizei o modulo ctypes. O módulo ctypes provê a compatibilidade dos tipos de dados em C permitindo chamar bibliotecas, como por exemplo DDLs e shared objects.

Vamos ao exemplo:

1 - Programa exemplo em c:

    HelloWorld.c


2 - Compilando o HelloWorld.c:

    gcc -Wall HelloWorld.c -shared -fPIC -o HelloWorld_lib.so 

3 - Programa em Python:

    HelloWorld.py


4 - Executando o python:
    
    Python HelloWorld.py

Resultado:

A soma dos numeros:
11
Metodo dobro!
10



