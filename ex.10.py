#10. Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.

valor = int(input("digite um numero : "))
aux = 0
print("*" * 18)
print("Tabuada de {}".format(valor))
print("*" * 18)
while(aux <= 10):
  print("{0} X {1} = {2}".format(aux, valor, (aux * valor)))
  aux = aux + 1