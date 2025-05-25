from .prova import calcular_media
from .questoes import questoes
from banco import tentativas_alunos
# RF09 - Função para exibir o relatório completo para o professor
def relatorio_professor(usuarios_alunos):
    if not tentativas_alunos:
        print("Nenhum aluno completou a prova ainda.")
        return

    print("\nRelatório do Professor:\n")
    for email, notas in tentativas_alunos.items():
        nome = usuarios_alunos.get(email, {}).get("nome", "Desconhecido")
        media = calcular_media(email)
        print(f"{nome} - Média: {media:.2f}")

    acertos = [0] * len(questoes)
    total = [0] * len(questoes)

    for notas_aluno in tentativas_alunos.values():
        for i, nota in enumerate(notas_aluno):
            if nota > 0: # Conta acertos
                acertos[i] += 1
            total[i] += 1 # Conta o total de respostas para cada questão
    # RF10 - Exibe as estatísticas sobre as questões
    if total:
        mais_acertos = acertos.index(max(acertos))
        menos_acertos = acertos.index(min(acertos))
        print("\nQuestões com mais e menos acertos:")
        print(f"Mais acertos: {questoes[mais_acertos]['pergunta']}")
        print(f"Menos acertos: {questoes[menos_acertos]['pergunta']}")