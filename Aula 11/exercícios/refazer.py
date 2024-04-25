lista_tesouro = [1,2,3,4,5,6,7,8,9,10]

TESOURO = 5
tentativas = 3


for contagem in lista_tesouro:
    escolha = int(input("Informe a posição que deseja tentar: "))
    
    if contagem == TESOURO:
        print("Parabéns, você achou o tesouro!")
        exit()
    
    
    if tentativas == 0: 
        tentativas = tentativas - 1
        print(f"Você errou. {tentativas} chances sobrando!")
  
    #print("Você esgotou as tentativas. programa encerrando...")
         



    
    

        
    
    