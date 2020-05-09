carros=['Mustang','Sonic','Challenger','Aveo']
def saludo():
    print('Hello world!')
def ordenar_lista():
    carros.sort()
    print(carros)
def agregar_elemento(variable):
    carros.append(variable)
    print("Elemento agregado")
    print(carros)
while True:
    print("Menu principal")
    print("1 Ordenar Lista")
    print("2 Saludar")
    print("3 Agregar elemento")
    op=int(input("Selecciona una opcion"))
    if op==1:
        ordenar_lista()
    elif op==2:
        saludo()
    elif op==3:
        au=input("Ingresa el nombre del auto")
        agregar_elemento(au)
        break
