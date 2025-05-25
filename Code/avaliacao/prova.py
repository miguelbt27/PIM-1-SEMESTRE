from .questoes import questoes
import banco 

# RF06 - Função para a prova do aluno
def aplicar_prova(email):
    maximo_tentativas = 3

    if len(banco.tentativas_alunos.get(email, [])) >= maximo_tentativas:
        print("Você já atingiu o número máximo de tentativas!")
        return

    print(f"\nTentativa {len(banco.tentativas_alunos.get(email, [])) + 1} de {maximo_tentativas}")
   
    # RF07 - Cálculo de nota
    # A cada pergunta, o aluno tem que responder e vamos atribuindo uma pontuação
    nota = 0
    for questao in questoes:
        print("\n" + questao["pergunta"])
        for opcao in questao["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta: ").strip().upper()
        if resposta == questao["resposta"]: # Se a resposta estiver correta
            nota += questao["valor"]
        else:
            print(f"Resposta errada! A correta era: {questao['resposta']}")

    print(f"\nSua nota final: {nota}/{sum(q['valor'] for q in questoes)}")
    banco.tentativas_alunos.setdefault(email, []).append(nota) # Adicionando a pontuação na lista de tentativas
    banco.salvar_tentativas() # Salvando as tentativas no arquivo

    restantes = maximo_tentativas - len(banco.tentativas_alunos[email])
    if restantes:
        print(f"Você ainda tem {restantes} tentativa(s).\n")
    else:
        print("Suas tentativas acabaram.\n")

# RF08 - Função para calcular a média das notas do aluno
def calcular_media(email):
    notas = banco.tentativas_alunos.get(email, [])
    return sum(notas) / len(notas) if notas else 0

# RF08 - Função para mostrar o resultado da avaliação do aluno
def mostrar_resultado_aluno(email):
    media = calcular_media(email)
    print(f"Média das tentativas: {media:.2f}")

# RF11 - Função para exibir o gabarito da prova
def mostrar_gabarito():
    print("\nGabarito das questões:")
    for questao in questoes:
        print(f"{questao['pergunta']}")
        print(f"Resposta correta: {questao['resposta']}\n")