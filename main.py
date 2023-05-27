# lista contendo outra lista com 2 indices cada dentro com nome e notas.
resultados = [['João', 'e4_t4_p8_s8'], ['Maria', 'e5_t5_p9_s9'], ['Pedro', 'e6_t6_p10_s10'], 
              ['Lucas', 'e7_t7_p6_s8'], ['Ana', 'e8_t8_p7_s9'], ['Julia', 'e8_t6_p9_s10']]
menu ="""
###### FILTRE OS CANDIDATOS PELA NOTA ######   
 """
resultadoP = """
######## SEGUE ABAIXO A LISTA DOS CANDIDATOS #####
"""

#função criada para adicionar usuario quando usuario digita "s" na opção do loop de adicionar novo participante
def adicionarCandidatos(nome,nE,nT,nP,nS):
        resultados.append([nome, f"e{nE}_t{nT}_p{nP}_s{nS}"])

def buscar_candidato():
    while 1==1:# foi criado um loop para sempre rodar o programa até que o usuário decida encerrar 
        #no fim de cada consulta
        print(menu)
        nota_entrevista = int(input("Digite a nota mínima da entrevista: "))
        nota_teorico = int(input("Digite a nota mínima do teste teórico: "))
        nota_prarico = int(input("Digite a nota mínima do teste prático: "))
        nota_soft = int(input("Digite a nota mínima da avaliação soft skills: "))
        
        candidatos_disponiveis = [] #vou adicionar os candidatos nessa lista que tem os critérios 
                                    #pedidos no imput
        for i in resultados:
            nome, notas = i
            e, t, p, s = notas.split('_')
            if int(e[1:]) >= nota_entrevista and int(t[1:]) >= nota_teorico and int(p[1:]) >= nota_prarico and int(s[1:]) >= nota_soft:
                candidatos_disponiveis.append(i)
        print(resultadoP)
        for candidato in candidatos_disponiveis:
            nome, notas = candidato
            print(nome + " " + notas)
        resposta = input("Quer fazer uma nova consulta?(s)para sim e(n)para não: ")
        if resposta == "n":
            break
        resposta2 = input("Deseja adicionar um novo candidato?(s)para sim e(n)para não: ")
        if resposta2 == "s":
            
            nomeCandidato = input("Digite o nome do novo candidato: ")
            entrevistaCandidato = input("Digite a nota da entrevista do novo candidato: ")
            teoricoCandidato = input("Digite a nota do teste teórico do novo candidato: ")
            praticoCandidato = input("Digite a nota do teste prático do novo candidato: ")
            softCandidato = input("Digite a nota da avaliação soft skills do novo candidato: ")
           # resultados.append([nomeCandidato, f"e{entrevistaCandidato}_t{teoricoCandidato}_p{praticoCandidato}_s{softCandidato}"])

            adicionarCandidatos(nomeCandidato,entrevistaCandidato,teoricoCandidato,praticoCandidato,softCandidato)
buscar_candidato()