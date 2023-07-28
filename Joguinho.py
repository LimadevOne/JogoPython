import random 

respostas = ['Talvez', 'Aos sabados, elefantes esquecem de ir visitar suas maes','Sim', 'Não','De onde veio isso?', 'Ontem eu fiz um teste e descobri, mecanicos não vendem pão', 'Eu vi santos, e eles não mentem', 'Indie é música boa', 'Por que não temos ar-condicionado compartilhado?', 'Coach não é profissional nem curso','o amor não é banal']

while True:
  pergunta = input("Faça uma pergunta... \n")
  print(random.choice(respostas))
  print("\n")
