dicionario = {}
    
for i in range(13):
    new={i:i**2}
    dicionario.update(new)
    #print(dicionario)
print(dicionario)

nuevo_dict = {i:i**2 for i in range(13)}
print(nuevo_dict)
