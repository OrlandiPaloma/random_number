import random

valor_aleatorio = random.randint(1,10)

acertou = False

while acertou == False:
  chute = int(input("Chute um valor de 1 a 10: "))

  if chute > valor_aleatorio:
    print("Chute maior do que o numero")

  elif chute < valor_aleatorio:
    print("Chute menor do que o numero")
    
  elif chute == valor_aleatorio:
    acertou == True
    print("Você acertou")