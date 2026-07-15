import unicodedata

def normalizar(texto):
    texto = texto.lower().strip()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def checar(resposta, gabarito):
    return normalizar(resposta) == normalizar(gabarito)

print("Seja bem-vindo ao QUIZ das capitais dos estados brasileiros!")

jogador = input('Para iniciar o jogo digite s: ')

if jogador.lower() != 's':
    quit()
print('Legal, vamos jogar!\n')
pontos = 0

pergunta = input("1. Qual a capital do estado de AC? ")
if checar(pergunta, "rio branco"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("2. Qual a capital do estado de AL? ")
if checar(pergunta, "maceió"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("3. Qual a capital do estado de AP? ")
if checar(pergunta, "macapá"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("4. Qual a capital do estado de AM? ")
if checar(pergunta, "manaus"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("5. Qual a capital do estado de BA? ")
if checar(pergunta, "salvador"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("6. Qual a capital do estado de CE? ")
if checar(pergunta, "fortaleza"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("7. Qual a capital do estado de ES? ")
if checar(pergunta, "vitória"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("8. Qual a capital do estado de GO? ")
if checar(pergunta, "goiânia"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("9. Qual a capital do estado de MA? ")
if checar(pergunta, "são luís"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("10. Qual a capital do estado de MT? ")
if checar(pergunta, "cuiabá"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("11. Qual a capital do estado de MS? ")
if checar(pergunta, "campo grande"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("12. Qual a capital do estado de MG? ")
if checar(pergunta, "belo horizonte"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("13. Qual a capital do estado de PA? ")
if checar(pergunta, "belém"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("14. Qual a capital do estado de PB? ")
if checar(pergunta, "joão pessoa"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("15. Qual a capital do estado de PR? ")
if checar(pergunta, "curitiba"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("16. Qual a capital do estado de PE? ")
if checar(pergunta, "recife"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("17. Qual a capital do estado de PI? ")
if checar(pergunta, "teresina"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("18. Qual a capital do estado de RJ? ")
if checar(pergunta, "rio de janeiro"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("19. Qual a capital do estado de RN? ")
if checar(pergunta, "natal"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("20. Qual a capital do estado de RS? ")
if checar(pergunta, "porto alegre"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("21. Qual a capital do estado de RO? ")
if checar(pergunta, "porto velho"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("22. Qual a capital do estado de RR? ")
if checar(pergunta, "boa vista"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("23. Qual a capital do estado de SC? ")
if checar(pergunta, "florianópolis"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("24. Qual a capital do estado de SP? ")
if checar(pergunta, "são paulo"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("25. Qual a capital do estado de SE? ")
if checar(pergunta, "aracaju"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

pergunta = input("26. Qual a capital do estado de TO? ")
if checar(pergunta, "palmas"):
    print("Certo!\n")
    pontos += 1
else:
    print("Errado!\n")

print("Você acertou " + str(pontos) + " das 26 capitais.\n")
