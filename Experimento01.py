
#				 											ME323 - EXPERIMENTO 01
#LUKAS SILVA DA ROSA 		        RA:183167
#JOAN LIMA RIOS				RA:175870
#FABIO PERRONE				RA:170788

import random
import matplotlib.pyplot as plt

n = 10000
portas = []
porta_aberta = []
porta_troca = []
result_troc = [0]*(n+1)
result_n_troc = [0]*(n+1)

for i in range(n):

	portas = {'A','B','C'}

	porta_certa = random.choice(list(portas)) #escolhe aleatóriamente uma das três portas para ser a porta premiada
	porta_escolhida = random.choice(list(portas)) #escolhe aleatóriamente uma das três portas para ser a porta escolhida

	#escoher aleatoriamente uma porta para abrir sem ser a escolhida pelo usuário ou a porta premiada
	porta_aberta = random.choice(list(portas.difference(porta_certa).difference(porta_escolhida))) 
	#porta escolhida após a abertura da porta
	porta_troca = list(portas.difference(porta_escolhida).difference(porta_aberta))[0]

	if porta_escolhida == porta_certa:
		result_troc[i] = 0
		result_n_troc[i] = 1

	if porta_troca == porta_certa:
		result_troc[i] = 1
		result_n_troc[i] = 0

for i in range(n):
	result_troc[i+1] = result_troc[i+1] + result_troc[i]
	result_n_troc[i+1] = result_n_troc[i+1] + result_n_troc[i]

for i in range(n):
	result_troc[i+1] = result_troc[i+1]/(i+1)
	result_n_troc[i+1] = result_n_troc[i+1]/(i+1)


R_T_P, = plt.plot(result_troc, label = 'Resultado Trocando Porta')
R_N_T_P, = plt.plot(result_n_troc, color = 'red', label = 'Resultado Não Trocando Porta')
plt.legend(handles=[R_T_P, R_N_T_P])
plt.title('ME323 - Experimento 01')
plt.xlabel('Número de jogadas')
plt.ylabel('Probabilidade Acumulada')
plt.savefig('Grafico01.png')
plt.show()
