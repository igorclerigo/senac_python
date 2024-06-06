
# Solicitação de input ao usuário
palavra = input("Informe uma palavra (ping/time/Botafogo/vivo): ").lower()
def check(a):
    if a == "ping":
        return "pong"
    elif a == "time":
        return "Botafogo"
    elif a == "vivo":
        return "morto"
    else:
        return "Palavra desconhecida"
    
print(check(palavra))

# No print, a palavra vira parâmetro da função check, pois 'a' recebe o valor que está dentro de palavra. Na hora de retornar, 
#a função se transforma no valor que vc colocar no return.

