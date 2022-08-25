import json

from logic.person import Person

lista = []


def cargar():
    try:
        archivo = open('db.json', 'r')
        content = archivo.read()
        dictionary = json.loads(content)
        for key, value in dictionary.items():
            persona = Person(key, value['name'], value['last_name'])
            lista.append(persona)
    except json.decoder.JSONDecodeError:
        return


def main():
    cargar()
    print('Vista consola')
    while True:
        conversion(lista)
        if len(lista) == 0:
            opcion = int(input("Menu\n [1] -> Insertar\n [2] -> Salir\nOpción: "))
            if opcion == 1:
                insertar()
            elif opcion == 2:
                break
            else:
                print("[!] Opción inválida")
        else:
            opcion = int(input("Menú\n [1] -> Visualizar\n [2] -> Insertar\n [3] -> Modificar\n"
                               " [4] -> Eliminar\n [5] -> Salir\nOpción: "))
            if opcion == 1:
                visualizar()
            elif opcion == 2:
                insertar()
            elif opcion == 3:
                update(input("ID de la persona a modificar: "))
            elif opcion == 4:
                delete(input("ID de la persona a eliminar: "))
            elif opcion == 5:
                break
            else:
                print("[!] ERROR")


def visualizar():
    for person in lista:
        print(person)


def insertar():
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    p = Person(id_person=id, name=nombre, last_name=apellido)
    lista.append(p)
    print("[i] La Persona ha sido creada con éxito")


def update(id_update):
    for person in lista:
        if person.id_person == id_update:
            nombre = input(f'Nombre actual: {person.name} \nNuevo nombre: ')
            apellido = input(f'Nombre actual: {person.last_name} \nNuevo nombre: ')
            person.name = nombre
            person.last_name = apellido
            print(f'[i] Los Datos han sido actualizados con éxito:\n Nombre: {person.name}\n Apellido: {person.last_name}')


def delete(id_delete):
    for persona in lista:
        if persona.id_person == id_delete:
            lista.remove(persona)
            print("[i] La Persona ha sido eliminada con éxito")


def conversion(data: list = lista):
    datos = {}
    for item in data:
        datos[item.id_person] = {'name': item.name, 'last_name': item.last_name}

    with open('db.json', 'w') as file:
        json.dump(datos, file)
        file.close()


if __name__ == '__main__':
    main()
