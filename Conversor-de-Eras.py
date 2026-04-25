import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    #  não tava funcionado dentro do else então criei uma função pra rodar a opção de limpar a tela
    
def converter_dias_para_anos():
    while True:
        try:
            dias = int(input("Digite o numero de dias: "))
            resultado = dias // 365
            print(f"O numero de dias {dias} é igual a {resultado} ano")
            time.sleep(2) # coloquei um tempo de espera
            sair_ou_ficar = input("Você deseja sair ? (s/n): ").lower().strip() # pergunta sé o usuario quer ficar 
            
            if sair_ou_ficar == "s":
                print("Saindo")
                break
            else:
                print("Continuando então ")
                limpar_tela()
                
        
        except ValueError:
            print("Apenas numeros")

def converter_anos_para_dias():
    while True:
        try:
            anos = int(input("Digite o numero de anos: "))
            resultado = anos * 365
            print(f"O ano {anos} é igual a {resultado} dias")
            time.sleep(2)
            sair_ou_ficar = input("Deseja sair ? (s/n): ").lower().strip()
            
            if sair_ou_ficar == "s":
                print("Saindo...")
                break
            
            elif sair_ou_ficar == "n":
                print("Continuar...")
                limpar_tela()
            
            else:
                print("Apenas s/n")
        
        except ValueError:
            print("Apenas numeros")
    
while True:
    try:
        print("\n1- Converter dias para anos")
        print("2- Converter anos para dias")
        print("00- Sair")
        
        opc = int(input("Qual opção você deseja ?: "))
        
        if opc == 1:
            limpar_tela()
            converter_dias_para_anos()
        
        elif opc == 2:
            limpar_tela()
            converter_anos_para_dias()
        
        elif opc == 00:
            limpar_tela()
            print("Saindo...")
            break
        
        else:
            print("O numero selecionado não existe")
        
    except ValueError:
        print("A opção selecionada não existe")