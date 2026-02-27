peso = float(input("Digite o seu peso (em Kg): "))
altura = float(input("Digite sua altura (em metros): ").replace(",","."))
imc = peso / (altura ** 2)

print (f"seu imc é {imc}")
if imc < 18.5: 
    print("você está abaixo do peso. ")
   
elif imc >= 18.5 and imc < 25:
    print ("você está no peso ideal")
    
else:
    print ("você está acima do peso.")
  

