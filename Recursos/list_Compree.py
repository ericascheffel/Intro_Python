#from string import maketrans

LISTA_BASE= list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle kyicrpylq() gq pcamkkclbcb lmu ynnjw ml rfc spj") 
STRG_BASE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle kyicrpylq() gq pcamkkclbcb lmu ynnjw ml rfc spj"

list_chave =[chr(letra) for letra in range(ord('a'), ord('z')+1)] # gera o alfabeto
print(list_chave)

list_valor =[chr(letra+2) for letra in range(ord('a'), ord('z')+1)] # progressão alfabéticaalterada para +2
list_valor.remove("|")
list_valor.remove("{")
list_valor.extend("a")
list_valor.extend("b")
print(list_valor)



TRADUCAO = "".maketrans(str(list_chave),str(list_valor))
print(TRADUCAO)

EXTRA = "map"

print("Traduzindo:", EXTRA.translate(TRADUCAO))

print("Traduzindo:", STRG_BASE.translate(TRADUCAO))


# MODELO CONSTRUÇÃO SO ALFABETO
"""
ALFABETO =[]
# list de a-z
for i in range(ord('a'), ord('z')+1): #ord() devolve um valor relativo do caracter
    ALFABETO.append(chr(i))
print(ALFABETO)
"""
