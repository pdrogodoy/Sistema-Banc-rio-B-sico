menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
  opcao = input(menu)

  #DEPOSITAR
  if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
      print("Falha!!, deposite um valor maior que 0.")
      
  #SACAR    
  elif opcao == "s":
    valor = float(input("Informe o valor que deseja sacar: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Operação falhou !! Você não possui saldo suficiente.")

    elif excedeu_limite:
      print("Operação falhou !! Você ultrapassou o limite.")

    elif excedeu_saques:
      print("Operação falhou !! Você atingiu o limite de saques.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
    
    else:
      print("Operação falhou !! Valor inválido.")

  #EXTRATO
  elif opcao == "e":
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo Atual: {saldo:.2f}")
    print("\n=============================")

  #SAIR  
  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")