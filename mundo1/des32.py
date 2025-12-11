from datetime import date as NeymarJunior
games_eduu = int(input('Digite aqui um ano qualquer para verificar se é bissexto ou 0 para analisar o ano atual: '))
if games_eduu == 0:
    games_eduu = NeymarJunior.today().year
if games_eduu % 4 == 0 and games_eduu % 100 != 0 or games_eduu % 400 == 0:
    print(games_eduu, 'é bissexto!')
else:
    print(games_eduu, 'não é bissexto!')