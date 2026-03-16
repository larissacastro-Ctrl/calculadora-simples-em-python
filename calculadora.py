#Calculadora em python

print("Calculadora")
#pedir o número para o usuário
num1 =float(input("Digite o primeiro número: "))
num2 =float(input("Digite o segundo número: "))

#pedir operação
operacao = input("Escolha a operação(+,-,*,/):")

#verificar a operacao
if operacao == "+":
    resultado = num1 +num2
elif operacao == "-":
    resultado = num1 -num2
elif operacao == "*":
    resultado = num1 *num2
elif operacao == "/":
    resultado = num1 /num2

#caso o usuário não coloque nenhuma das operacoes 
else:
    print("Operação inválida")
    resultado = None

#mostrar o resultado
if resultado!= None:
    print("Resultado: ",resultado)