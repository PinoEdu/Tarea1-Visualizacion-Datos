file = open('responses.csv','r')
mascotas = open('mascotas_splitter.csv','w')

flag = True

for line in file:
    aux = line.strip().split(',')
    if flag:
        flag = False
        mascotas.write('¿Tienes una mascota?,Mascota\n')
        continue
    #print(aux[1],aux[2:9])
    for mascota in aux[2:9]:
        if mascota != '':
            mascotas.write(aux[1]+','+mascota+',1'+'\n')
    for mascota in aux[17:25]:
        if mascota != '' and mascota != 'Ninguna':
            mascotas.write(aux[1]+','+mascota+',1'+'\n')