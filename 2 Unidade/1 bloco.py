
addTable = [
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
		['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'b', 'a', 'd', 'c', 'f', 'e'],
		['2', '3', '0', '1', '6', '7', '4', '5', 'a', 'b', '8', '9', 'e', 'f', 'c', 'd'],
		['3', '2', '1', '0', '7', '6', '5', '4', 'b', 'a', '9', '8', 'f', 'e', 'd', 'c'],
		['4', '5', '6', '7', '0', '1', '2', '3', 'c', 'd', 'e', 'f', '8', '9', 'a', 'b'],
		['5', '4', '7', '6', '1', '0', '3', '2', 'd', 'c', 'f', 'e', '9', '8', 'b', 'a'],
		['6', '7', '4', '5', '2', '3', '0', '1', 'e', 'f', 'c', 'd', 'a', 'b', '8', '9'],
		['7', '6', '5', '4', '3', '2', '1', '0', 'f', 'e', 'd', 'c', 'b', 'a', '9', '8'],
		['8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7'],
		['9', '8', 'b', 'a', 'd', 'c', 'f', 'e', '1', '0', '3', '2', '5', '4', '7', '6'],
		['a', 'b', '8', '9', 'e', 'f', 'c', 'd', '2', '3', '0', '1', '6', '7', '4', '5'],
		['b', 'a', '9', '8', 'f', 'e', 'd', 'c', '3', '2', '1', '0', '7', '6', '5', '4'],
		['c', 'd', 'e', 'f', '8', '9', 'a', 'b', '4', '5', '6', '7', '0', '1', '2', '3'],
		['d', 'c', 'f', 'e', '9', '8', 'b', 'a', '5', '4', '7', '6', '1', '0', '3', '2'],
		['e', 'f', 'c', 'd', 'a', 'b', '8', '9', '6', '7', '4', '5', '2', '3', '0', '1'],
		['f', 'e', 'd', 'c', 'b', 'a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'],
	]
multTable = [
		['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
		['0', '2', '4', '6', '8', 'a', 'c', 'e', '3', '1', '7', '5', 'b', '9', 'f', 'd'],
		['0', '3', '6', '5', 'c', 'f', 'a', '9', 'b', '8', 'd', 'e', '7', '4', '1', '2'],
		['0', '4', '8', 'c', '3', '7', 'b', 'f', '6', '2', 'e', 'a', '5', '1', 'd', '9'],
		['0', '5', 'a', 'f', '7', '2', 'd', '8', 'e', 'b', '4', '1', '9', 'c', '3', '6'],
		['0', '6', 'c', 'a', 'b', 'd', '7', '1', '5', '3', '9', 'f', 'e', '8', '2', '4'],
		['0', '7', 'e', '9', 'f', '8', '1', '6', 'd', 'a', '3', '4', '2', '5', 'c', 'b'],
		['0', '8', '3', 'b', '6', 'e', '5', 'd', 'c', '4', 'f', '7', 'a', '2', '9', '1'],
		['0', '9', '1', '8', '2', 'b', '3', 'a', '4', 'd', '5', 'c', '6', 'f', '7', 'e'],
		['0', 'a', '7', 'd', 'e', '4', '9', '3', 'f', '5', '8', '2', '1', 'b', '6', 'c'],
		['0', 'b', '5', 'e', 'a', '1', 'f', '4', '7', 'c', '2', '9', 'd', '6', '8', '3'],
		['0', 'c', 'b', '7', '5', '9', 'e', '2', 'a', '6', '1', 'd', 'f', '3', '4', '8'],
		['0', 'd', '9', '4', '1', 'c', '8', '5', '2', 'f', 'b', '6', '3', 'e', 'a', '7'],
		['0', 'e', 'f', '1', 'd', '3', '2', 'c', '9', '7', '6', '8', '4', 'a', 'b', '5'],
		['0', 'f', 'd', '2', '9', '6', '4', 'b', '1', 'e', 'c', '3', '8', '7', '5', 'a'],
	]

s_box_16 = {
		'0000': '9', '0001': '4', '0010': 'a', '0011': 'b',
		'0100': 'd', '0101': '1', '0110': '8', '0111': '5',
		'1000': '6', '1001': '2', '1010': '0', '1011': '3',
		'1100': 'c', '1101': 'e', '1110': 'f', '1111': '7', 
    }

s_invertida_box_16 = {
		'0000': 'a', '0001': '5', '0010': '9', '0011': 'b',
		'0100': '1', '0101': '7', '0110': '8', '0111': 'f',
		'1000': '6', '1001': '0', '1010': '2', '1011': '3',
		'1100': 'c', '1101': '4', '1110': 'd', '1111': 'e', 
    }

def switch_box(matriz):
	for key in s_box_16:
		if matriz == key:
			return s_box_16[key]

def switch_box_inv(matriz):
	for key in s_invertida_box_16:
		if matriz == key:
			return s_invertida_box_16[key]

def dividir(mensagem,tam_grupo,tam_total):
	matriz_dividida=[]
	i = int(0)
	for x in range(tam_total):			
	    matriz_dividida.append(mensagem[i:i+tam_grupo])
	    i=i+tam_grupo

	for unused in range(len(matriz_dividida)):			# Remover os espaços em branco
		if "" in matriz_dividida:
			matriz_dividida.remove("")

	return matriz_dividida

def juntar_matriz(matriz):	
	matriz_junta = "".join(matriz)
	return matriz_junta

def StrToHexa(mensagem):
	hexadecimal = []
	i = int(0)
	for x in range(0,len(mensagem) // 2+1):			# Transformar a mensagem em Hexadecimal
	    hexadecimal.append(mensagem[i:i+2].encode("utf-8").hex())
	    i=i+2

	for unused in range(len(hexadecimal)):			# Remover os espaços em branco
	    if "" in hexadecimal:
	        hexadecimal.remove("")
	
	return hexadecimal

def Check_4_bits(matriz, hexadecimal):
	i = int(0)
	resto = int(0)
	parte_digrafo_falta = []

	if len(matriz) % 4 != 0:		# Checar se os blocos do Texto estão com 4 caracteres
		resto = len(matriz) % 4
	stop = 4 - resto;
	# print("Stop",stop)
	if resto > 0:					# Se não tiver, complementa com o final do bloco anterior
		for i in range(resto,resto+stop):
			aux = str(0)
			parte_digrafo_falta.append(aux)
		for i in range(0,len(parte_digrafo_falta)):
			aux = str(0)
			hexadecimal.append(aux)
	return hexadecimal

def zero_complement(tam_blocos, bloco_16):
	
	i = int(0)
	j = int(0)
	tmp = list(bloco_16)
	while i < tam_blocos:				# Completa com 0 nos blocos com menos de 4 elementos
		if(len(bloco_16[i]) < 4):
			elemento = bloco_16[i]
			tam = 4 - len(bloco_16[i])
			for x in range(0,tam):
				elemento = '0'+ elemento
				del(tmp[i])
				tmp.insert(i,elemento)
		i+=1
		j=0
	return tmp

def switch_position(bloco):
	lista = []
	aux0 = bloco[0]
	aux1 = bloco[1]
	aux2 = bloco[2]
	aux3 = bloco[3]
	lista.append(aux0)
	lista.append(aux1)
	lista.append(aux3)
	lista.append(aux2)
	lista = juntar_matriz(lista)
	return lista

def switch_position_invertida(bloco):
	lista = []
	aux0 = bloco[0]
	aux1 = bloco[1]
	aux2 = bloco[2]
	aux3 = bloco[3]
	lista.append(aux0)
	lista.append(aux1)
	lista.append(aux3)
	lista.append(aux2)
	lista = juntar_matriz(lista)
	return lista

def xor_key(tam, mensagem,chave):
	
	xor_inicial = []
	xor_final = []

	for x in range(0,tam):					# Xor entre o bloco e a chave
		xor_inicial = hex(int(mensagem[x],16) ^ int(chave,16))
		xor_inicial = xor_inicial.replace("0x","")
		xor_final.append(xor_inicial)
	
	xor_final = zero_complement(len(xor_final),xor_final)
	return xor_final

def multiMatriz(mat):
	new_mat = [['', ''], ['', '']]
	# print("mat 00",mat[0][0])
	# print("mat 01",mat[0][1])
	# print("mat 10",mat[1][0])
	# print("mat 11",mat[1][1])

	# print("addTable{",mat[0][0]," o ",search(multTable, '4', mat[1][0]),"]}")
	# print("addTable{",search(multTable, '4', mat[0][0])," o ",mat[1][0],"]}")
	# print("addTable{",mat[0][1]," o ",search(multTable, '4', mat[1][1]),"]}")
	# print("addTable{",search(multTable, '4', mat[0][1])," o ",mat[1][1],"]}")

	new_mat[0][0] = search(addTable, mat[0][0], search(multTable, '4', mat[1][0]))
	new_mat[0][1] = search(addTable, 			search(multTable, '4', mat[0][0]), mat[1][0])
	new_mat[1][0] = search(addTable, mat[0][1], search(multTable, '4', mat[1][1]))
	new_mat[1][1] = search(addTable, 			search(multTable, '4', mat[0][1]), mat[1][1])
	return new_mat

def multiMatriz_inv(mat):
	# print("mat",mat[0][0])
	new_mat = [['', ''], ['', '']]
	print("0",mat[0][0])
	print("1",mat[0][1])
	print("2",mat[1][0])
	print("3",mat[1][1])
	# aux0 = mat[0][1]
	# aux1 = mat[0][0]
	# aux2 = mat[1][0]
	# aux3 = mat[1][1]
	# print("0",aux0)
	# print("1",aux1)
	# print("2",aux2)
	# print("3",aux3)
	
	new_mat[0][0] = search(addTable, search(multTable, '9', mat[0][0]), search(multTable, '2', mat[1][0]))
	new_mat[0][1] = search(addTable, search(multTable, '9', mat[0][1]), search(multTable, '2', mat[1][1]))
	
	new_mat[1][0] = search(addTable, search(multTable, '2', mat[0][0]), search(multTable, '9', mat[1][0]))
	new_mat[1][1] = search(addTable, search(multTable, '2', mat[0][1]), search(multTable, '9', mat[1][1]))
	
	# new_mat[0][0] = search(addTable, search(multTable, '9', mat[0][0]), search(multTable, '2', mat[1][0]))
	# new_mat[0][1] = search(addTable, search(multTable, '2', mat[0][0]), search(multTable, '9', mat[1][0]))
	# new_mat[1][0] = search(addTable, search(multTable, '9', mat[0][1]), search(multTable, '2', mat[1][1]))
	# new_mat[1][1] = search(addTable, search(multTable, '2', mat[0][1]), search(multTable, '9', mat[1][1]))

	return new_mat

def search(table, l, c):
	l = int(l, 16)
	c = int(c, 16)
	return table[l][c]

def switch_bitsChave(elemento):
	lista = []
	
	aux0 = elemento[0]
	aux1 = elemento[1]
	aux2 = elemento[2]
	aux3 = elemento[3]

	lista.append(aux1)
	lista.append(aux2)
	lista.append(aux3)
	lista.append(aux0)
	lista = juntar_matriz(lista)
	return lista

def xorBinary(a, b):
	result = int(a,2) ^ int(b,2)
	result = bin(result)
	return '{:0>4}'.format(result[2:])

def binToHex(b):
	result = hex(int(b, 2))
	return result[2:]

def make_key(chave):
	num_rodada = int(3)
	i = int(0)
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	lista_chave = []

	# Split a Lista 
	lista_chave.append(bin(int(str(chave[0]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[1]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[2]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[3]), scale))[2:].zfill(num_of_bits))	
	
	for i in range(4,12):

		temp = lista_chave[i-1]
		
		if i < 8:
			r = bin(int(str(1), scale))[2:].zfill(num_of_bits)
		else:
			r = bin(int(str(2), scale))[2:].zfill(num_of_bits)
		if i % 4 == 0:
			
			rot = switch_bitsChave(temp)			# Rotação dos bits
			sw_box = switch_box((rot))				# S-Box
			sw_box = bin(int(str(sw_box), 			# Tranf. da saida S-box
			scale))[2:].zfill(num_of_bits)			# em binario
			temp = xorBinary(str(sw_box), str(r))	# Xor Binario
			
			temp = xorBinary(str(temp), str(lista_chave[i-4]))	# Xor Binario
			lista_chave.append(temp)				# Adiciona a Lista
		else:
			temp = xorBinary(str(temp), str(lista_chave[i-4]))	# Xor Binario
			lista_chave.append(temp)				# Adiciona a Lista
	
	# print(lista_chave)
	return lista_chave

def encrypt(mensagem):
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	saida_Sbox = []
	sw_position = []
	aux = []
	sw_coloum = ""
	
	# ======================================================================
	#						S - Box
	for x in mensagem:
		for i in x:
			binario = bin(int(str(i), scale))[2:].zfill(num_of_bits)
			saida_Sbox.append(switch_box(binario))
			# print(x,"-",binario,"-",saida_Sbox)
	saida_Sbox = juntar_matriz(saida_Sbox)				
	saida_Sbox = dividir(saida_Sbox,4,len(saida_Sbox))
	print("S-Box\n",saida_Sbox)

	# ======================================================================
	#						Deslocar Linhas 
	for x in range(0,len(saida_Sbox)):					# Troca as posições do Texto
		sw_position.append(switch_position(saida_Sbox[x]))
	
	print("SW Linhas\n",sw_position)
	sw_position = juntar_matriz(sw_position)
	
	# s_box_4 = dividir(sw_position,2,len(sw_position))
	saida = sw_position
	return saida

def pre_processing(mensagem,chave):
	hexadecimal = []
	chave_hexa = []
	matriz_blocos = []

	# ========================================================
	# 			Tratamento da Mensagem
	hexadecimal = StrToHexa(mensagem)				# Transformar a Mensagem em Hexadecimal	
	matriz = juntar_matriz(hexadecimal)				# Junta a mensagem num único Bloco
	hexadecimal = Check_4_bits(matriz, hexadecimal)	# Checa se cada bloco possui 4 bits
	matriz = juntar_matriz(hexadecimal)				# Juntar os blocos
	
	# ========================================================
	# 			Tratamento da Chave
	chave_hexa = StrToHexa(chave)					# Transformar a chave em Hexadecimal
	chave_hexa = juntar_matriz(chave_hexa)			# Junta a Chave num unico bloco
	matriz_blocos = dividir(matriz,4,len(matriz))	# Divide a Matriz em blocos de 4

	conj_chave = make_key(chave_hexa)
	return matriz_blocos, conj_chave				# Retorna Matriz e o Conjunto de Chaves


def pre_processing_inv(mensagem,chave):	
	
	chave_hexa = []
	matriz_blocos = []

	# ========================================================
	# 			Tratamento da Mensagem
	matriz_blocos = dividir(mensagem,4,len(mensagem))	# Divide a Matriz em blocos de 4

	# ========================================================
	# 			Tratamento da Chave
	chave_hexa = StrToHexa(chave)					# Transformar a chave em Hexadecimal
	chave_hexa = juntar_matriz(chave_hexa)			# Junta a Chave num unico bloco
	
	conj_chave = make_key(chave_hexa)
	return matriz_blocos, conj_chave				# Retorna Matriz e o Conjunto de Chaves

# ================================================================================

#									 PIPELINE							 		   #

# ================================================================================

def sw_colunas_inv(mensagem):
	
	# ======================================================================
	#						Switch Colunas Inversa
	aux = []
	sw_coloum = ""
	sw_position = juntar_matriz(mensagem)
	s_box_4 = dividir(sw_position,2,len(sw_position))
	tam2 = int(len(s_box_4)/2)
	line_dividido = dividir(s_box_4,2,tam2)

	for x in range(tam2):
		aux.append(multiMatriz_inv(line_dividido[x]))

	for i in aux:
		for j in i:
			for k in j:
				sw_coloum += k	

	sw_coloum = dividir(sw_coloum,4,len(sw_coloum))
	sw_coloum = juntar_matriz(sw_coloum)
	return sw_coloum

def sw_colunas(mensagem):
	# ======================================================================
	#						Switch Colunas	
	# print("äaaaaa",mensagem)
	aux = []
	sw_coloum = ""
	sw_position = juntar_matriz(mensagem)
	s_box_4 = dividir(sw_position,2,len(sw_position))
	tam2 = int(len(s_box_4)/2)
	line_dividido = dividir(s_box_4,2,tam2)

	for x in range(tam2):
		aux.append(multiMatriz(line_dividido[x]))

	for i in aux:
		for j in i:
			for k in j:
				sw_coloum += k	

	sw_coloum = dividir(sw_coloum,4,len(sw_coloum))
	sw_coloum = juntar_matriz(sw_coloum)
	return sw_coloum

def pipeline(mensagem,chave,text_claro,chave_inicial,op):
	chave1 = ""
	chave2 = ""
	chave3 = ""
	sw_coloum = ""
	xor = []
	aux = []
	# ========================================================
	# 			Tratamento da Chave

	for x in range(0,12):
		if x >= 0 and x < 4:
			aux = chave[x]
			chave1 += binToHex(aux)
		if x > 3 and x < 8:
			aux = chave[x]
			chave2 += binToHex(aux)
		if x > 7:
			aux = chave[x]
			chave3 += binToHex(aux)
	
	print("=== Chaves Geradas  ===")
	print("\t",chave1)
	print("\t",chave2)
	print("\t",chave3)
	print("====================== ")
	
	if op == 1:
		# ========================================================
		# 			Encriptação
		
		print("[Criptografar]")
		
		# ========================================================
		#  == ====== ====== - Primeira Rodada - ======= ====== ==
		# ========================================================
		print("\n=== [1 - E] - Primeira Rodada ===\n")
		print("Mensagem em Hexadecimal\n\t",mensagem)		# Mensagem Usada nesse processo
		print("Chave em Hexadecimal\n\t",chave1)			# Chave Usada nesse processo
		
		# ========================================================
		#			Xor Inicial
		xor = xor_key(len(mensagem), mensagem, chave1)		# Xor entre o bloco e a chave
		print("1 - Xor")
		print(xor," = ",mensagem," ^ [",chave1,"]")			# Print Xor
		
		# ========================================================
		#			S-Box e SW Linhas
		print("-- Etapas da Codificação --")
		pri_rodada = encrypt(xor)							# Pipeline do Algoritmo	
		# print("111",pri_rodada)
		# ========================================================
		#			SW Colunas
		pri_rodada = juntar_matriz(pri_rodada)				# Junta em um unico bloco
		sw_coloum = sw_colunas(pri_rodada)					# SW Colunas
		print("SW Colunas\n",sw_coloum)

		# ========================================================
		#			XOR com Chave2
		xor2 = hex(int(sw_coloum,16) ^ int(chave2,16))		# Xor SW Colunas e a Chave
		xor2 = xor2.replace("0x","")						# Remove o elemento 0x
		print("Incluir chave da Rodada")
		print(xor2," = [",sw_coloum,"] ^ [",chave2,"]")		# Print Xor Final da primeira rodada
		
		# ========================================================
		#			Resultado
		print("--- Resultado --- \n",xor2,"")	
		primeira = xor2
		
		# ========================================================
		#  == ====== ====== - Segunda Rodada - ======= ====== ==
		# ========================================================
		
		print("\n=== [2 - E] - Segunda Rodada ===\n")
		print("Mensagem em Hexadecimal\n\t",primeira)		# Mensagem Usada nesse processo
		
		# ========================================================
		#			S-Box e SW Linhas
		print("-- Etapas da Codificação --")
		seg_rodada = encrypt(primeira)						# Pipeline do Algoritmo
		# print("sss",primeira)
		# # ========================================================
		# #			Xor com a Chave3
		# segunda = xor_key(len(seg_rodada), 					# Xor SW Colunas e a Chave
		# 	seg_rodada, chave3)	
		# print("Incluir chave da Rodada")
		# print(segunda," = ",seg_rodada," ^ [",chave3,"]")
		
		# ========================================================
		#			XOR com Chave2
		xor2 = hex(int(seg_rodada,16) ^ int(chave3,16))		# Xor SW Colunas e a Chave
		xor2 = xor2.replace("0x","")						# Remove o elemento 0x
		print("Incluir chave da Rodada")
		print(xor2," = ",seg_rodada," ^ [",chave3,"]")		# Print Xor Final da primeira rodada
		
		# ========================================================
		#			Resultado
		print("\n--- Resultado --- \n",xor2,"\n")

	
	else:

		# ========================================================
		# 			DEcriptação

		print("[DEscriptografar]")
		
		# ========================================================
		#  == ====== ====== - Primeira Rodada - ======= ====== ==
		# ========================================================
		
		print("\n=== [1 - D] - Primeira Rodada ===\n")
		print("Mensagem em Hexadecimal\n\t",mensagem)		# Mensagem Usada nesse processo
		print("Chave em Hexadecimal\n\t",chave3)			# Chave Usada nesse processo
		# ========================================================
		#			Xor Inicial
		xor = xor_key(len(mensagem), mensagem, chave3)		# Xor entre o bloco e a chave
		print("Xor")
		print(xor," = ",mensagem," ^ [",chave3,"]")			# Print Xor
		print("\n-- Etapas da Codificação --")
		# ========================================================
		#			Linhas e S-Box Inversas
		pri_rodada = decrypt(xor)							# Pipeline do Algoritmo	
		# ========================================================
		#			Xor com a Chave2
		primeira = hex(int(pri_rodada,16) ^ int(chave2,16))	# Xor do Pipeline e a Chave
		primeira = primeira.replace("0x","")				# Remove o elemento 0x
		print("Incluir chave da Rodada")
		print(primeira," = ",pri_rodada," ^ [",chave2,"]")	# Print Xor Final da primeira rodada
		# ========================================================
		#			S-Colunas Inversas
		pri_rodada = juntar_matriz(primeira)				# Junta em um unico bloco
		sw_coloum = sw_colunas_inv(primeira)				# SW Colunas
		print("SW Colunas\n",sw_coloum)
		# ========================================================
		#			Resultado
		print("--- Resultado --- \n",sw_coloum,"\n")		# Print Resultado
		ax = [1]
		ax[0] = sw_coloum 									# Passando Primeira para Vetor
		
		# ========================================================
		#  == ====== ====== - Segunda Rodada - ======= ====== ==
		# ========================================================
		print("\n=== [2 - D] - Segunda Rodada ===\n")
		print("Mensagem em Hexadecimal\n\t",ax)				# Mensagem Usada nesse processo
		print("-- Etapas da Codificação --")

		# ========================================================
		#			Linhas e S-Box Inversas
		# print("Dec",ax)
		seg_rodada = decrypt(ax)							# Pipeline do Algoritmo
		# print("Dec",seg_rodada)
		# ========================================================
		#			Xor com a Chave1
		segunda = hex(int(seg_rodada,16) ^ int(chave1,16))	# Xor com a chave
		segunda = segunda.replace("0x","")					# Remove elemento 0x
		print("Incluir chave da Rodada")
		print(segunda," = ",seg_rodada," ^ [",chave1,"]")	# Print do Processo
		# ========================================================
		#			Resultado
		print("\n--- Resultado --- \n",segunda,"\n")		# Print Resultado


def main():
    op = int(input("Criptografia AES - CBC!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    
    if op == 1:
        print("[Criptografar]")
        # mensagem = input('Digite a mensagem:\n')
        # chave = input('Digite a chave[Ela deve possuir dois caracteres]:\n')
        # if len(chave) != 2:
        # 	while len(chave) != 2:
        # 		chave = input('Chave Errada! Digite a chave novamente com DOIS caracteres:\n')
        mensagem = 'FE'
        chave = 'AB'
        
        pre = pre_processing(mensagem,chave)
        pipeline(pre[0],pre[1],mensagem,chave,1)

    elif op == 2:
        print("[Descriptografar]")
        # mensagem = input('Digite a mensagem:\n')
        # chave = input('Digite a chave[Ela deve possuir dois caracteres]:\n')
        # if len(chave) != 2:
        # 	while len(chave) != 2:
        # 		chave = input('Chave Errada! Digite a chave novamente com DOIS caracteres:\n')
        mensagem = '5bd6'
        chave = 'AB'
        
        pre = pre_processing_inv(mensagem,chave)

        pipeline(pre[0],pre[1],mensagem,chave,2)

    else:
        print('Opção Inválida!')

def decrypt(mensagem):
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	saida_Sbox = []
	sw_position = []
	
	# ======================================================================
	#						Deslocar Linhas Inversa
	
	for x in range(0,len(mensagem)):					# Troca as posições do Texto
		sw_position.append(switch_position_invertida(mensagem[x]))
	print("SW Linhas Invertidas\n",sw_position)

	sw_position = juntar_matriz(sw_position)
	
	# ======================================================================
	#							S - Box Inversa
	for x in sw_position:	
		for i in x:
			binario = bin(int(str(i), scale))[2:].zfill(num_of_bits)
			saida_Sbox.append(switch_box_inv(binario))
			# print(x,"-",binario,"-",saida_Sbox)
	
	saida_Sbox = juntar_matriz(saida_Sbox)
	print("S-Box Invertida\n",saida_Sbox)
	saida = saida_Sbox
	return saida
