#descuento salud 7% y afp 12%

import csv
import openpyxl

def registrar_trabajador(lista):
    lista_trabajadores.append(lista)
    return lista

def listar_trabajadores(lista):
    for fila in lista:
        print(f'Nombre: {fila[0]} | Cargo: {fila[1]} | Sueldo: {fila[2]} | Desc. salud: {fila[3]} | Desc. AFP: {fila[4]} | Sueldo liquido: {fila[5]}')

def imprimir_plantilla(lista):
    with open('plantilla_sueldos.csv','w',newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter='\t')
        escritor_csv.writerow(['Nombre','Cargo','Sueldo','Desc. salud','Desc. AFP','Sueldo liquido'])
        for fila in lista:
            escritor_csv.writerow(fila)
    
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    with open('plantilla_sueldos.csv','r') as data:
        reader = csv.reader(data, delimiter='\t')
        for row in reader:
            ws.append(row)
    
    return wb.save('plantilla_sueldo.xls')

lista_trabajadores = []

while True:         
    print('-'*20)
    print('1.-Registrar trabajador')
    print('2.-Listar todos los trabajadores')
    print('3.-Imprimir planilla de sueldos')
    print('4.-Salir')
    print('-'*20)
    opc = int(input('Ingrese la opcion: '))
    
    match opc:
        case 1:      
            nomTrab = input('Ingrese nombre de trabajador: ')
            cargo = input('ingrese el cargo: ')
            sueldo = int(input('ingrese el sueldo bruto: '))
            descuento_salud = int(sueldo * 0.07)
            descuento_afp = int(sueldo * 0.12)
            sueldo_liquido = int(sueldo - (descuento_salud + descuento_afp))
            datos_trabajador = [nomTrab,cargo,sueldo,descuento_salud,descuento_afp,sueldo_liquido]
            registrar_trabajador(datos_trabajador)
        case 2:  
            listar_trabajadores(lista_trabajadores)
        case 3:
            cargo_especifico = []
            print('-'*20)
            print('1.-Imprimir todos los cargos')
            print('2.-Imprimir cargo especifico')
            print('3.-Cancelar')
            print('-'*20)
            res = int(input('Ingrese su opcion: '))
            match res:
                case 1:
                    imprimir_plantilla(lista_trabajadores)
                case 2:
                    cargo_esp = input('Escriba el cargo a buscar: ')
                    for fila in lista_trabajadores:
                        if cargo_esp == fila[1]:
                            cargo_especifico.append(fila)
                        else:
                            print('no se encontro resultados')
                    imprimir_plantilla(cargo_especifico)
                case _:
                    print('opcion invalida, volviendo al menu principal')
        case 4:
            print('Programa finalizado')
            break
        case _:
            print('Opcion invalida')
    
