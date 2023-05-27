resultados = [{'nome': 'João', 'notas': {'entrevista': 4, 'teorico': 4, 'pratico': 8, 'soft': 8}},
              {'nome': 'Maria', 'notas': {'entrevista': 5, 'teorico': 5, 'pratico': 9, 'soft': 9}},
              {'nome': 'Pedro', 'notas': {'entrevista': 6, 'teorico': 6, 'pratico': 10, 'soft': 10}},
              {'nome': 'Lucas', 'notas': {'entrevista': 7, 'teorico': 7, 'pratico': 6, 'soft': 8}},
              {'nome': 'Ana', 'notas': {'entrevista': 8, 'teorico': 8, 'pratico': 7, 'soft': 9}},
              {'nome': 'Julia', 'notas': {'entrevista': 8, 'teorico': 6, 'pratico': 9, 'soft': 10}}]

menu = """
###### FILTRE OS CANDIDATOS PELA NOTA ######
"""
resultadoP = """
######## SEGUE ABAIXO A LISTA DOS CANDIDATOS ########
"""

# Função para adicionar um novo candidato
def adicionarCandidato(nome, n_entrevista, n_teorico, n_pratico, n_soft):
    novo_candidato = {'nome': nome, 'notas': {'entrevista': n_entrevista, 'teorico': n_teorico, 'pratico': n_pratico, 'soft': n_soft}}
    resultados.append(novo_candidato)

def formatar_notas(notas):
    return f"e{notas['entrevista']}_t{notas['teorico']}_p{notas['pratico']}_s{notas['soft']}"

def buscar_candidato():
    while True:
        print(menu)
        nota_entrevista = int(input("Digite a nota mínima da entrevista: "))
        nota_teorico = int(input("Digite a nota mínima do teste teórico: "))
        nota_pratico = int(input("Digite a nota mínima do teste prático: "))
        nota_soft = int(input("Digite a nota mínima da avaliação soft skills: "))

        candidatos_disponiveis = []
        for candidato in resultados:
            nome = candidato['nome']
            notas = candidato['notas']
            if (notas['entrevista'] >= nota_entrevista and notas['teorico'] >= nota_teorico and
                notas['pratico'] >= nota_pratico and notas['soft'] >= nota_soft):
                candidatos_disponiveis.append(candidato)

        print(resultadoP)
        for candidato in candidatos_disponiveis:
            nome = candidato['nome']
            notas = candidato['notas']
            notas_formatadas = formatar_notas(notas)
            print(f"{nome}   {notas_formatadas}")

        resposta = input("Quer fazer uma nova consulta? (s) para sim e (n) para não: ").lower()
        while resposta != "s" and resposta != "n":
            resposta = input("Quer fazer uma nova consulta?(s)para sim e(n)para não: ")
        resposta = resposta.lower()
     
        while resposta!= "s"and resposta!="n":
            resposta = input("Resposta invalida: (s)para sim e(n)para não: ")
            resposta = resposta.lower  
        if resposta == "n":
            break
         
        if resposta == "s":
            resposta2 = input("Deseja adicionar um novo candidato?(s)para sim e(n)para não: ")
            resposta2 = resposta2.lower()
            while resposta2 != "s"and resposta2 != "n":
                resposta2 = input("Resposta invalida: (s)para sim e(n)para não: ")
            resposta2 = resposta2.lower()
            if resposta2 == "s":
                    
                nomeCandidato = input("Digite o nome do novo candidato: ")
                entrevistaCandidato = int(input("Digite a nota da entrevista do novo candidato: "))
                teoricoCandidato = int(input("Digite a nota do teste teórico do novo candidato: "))
                praticoCandidato = int(input("Digite a nota do teste prático do novo candidato: "))
                softCandidato = int(input("Digite a nota da avaliação soft skills do novo candidato: "))
                # resultados.append([nomeCandidato, f"e{entrevistaCandidato}_t{teoricoCandidato}_p{praticoCandidato}_s{softCandidato}"])

                adicionarCandidato(nomeCandidato,entrevistaCandidato,teoricoCandidato,praticoCandidato,softCandidato)
buscar_candidato()


