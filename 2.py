def pertence (numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

numero = int(input("Informe ume valor qualquer: "))

if pertence(numero):
    print(f"{numero} pertence a sequencia")
else:
    print(f"{numero} nao pertence")