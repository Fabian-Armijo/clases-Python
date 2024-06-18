#descuento salud 7% y afp 12%
import csv

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
            def registrar_trabajador(lista):
                lista_trabajadores.append(lista)
                return lista_trabajadores        
            
            nomTrab = input('Ingrese nombre de trabajador: ')
            cargo = input('ingrese el cargo: ')
            sueldo = int(input('ingrese el sueldo bruto: '))
            descuento_salud = int(sueldo * 0.07)
            descuento_afp = int(sueldo * 0.12)
            sueldo_liquido = int(sueldo - (descuento_salud + descuento_afp))
            datos_trabajador = [nomTrab,cargo,sueldo,descuento_salud,descuento_afp,sueldo_liquido]
            registrar_trabajador(datos_trabajador)
            
        case 2:
            def listar_trabajadores(lista):
                for i in lista:
                    print(f'Nombre: {i[0]} | Cargo: {i[1]} | Sueldo: {i[2]} | Desc. salud: {i[3]} | Desc. AFP: {i[4]} | Sueldo liquido: {i[5]}')
            
            listar_trabajadores(lista_trabajadores)    
        case 3:
            def imprimir(lista):
                with open('planilla_sueldos.txt','w',newline='') as archivo_txt:
                    escribir = csv.writer(archivo_txt)
                    escribir.writerow(['Nombre','Cargo','Sueldo','Desc. salud','Desc AFP','Sueldo liquido'])
                    for i in lista:
                        escribir.writerow(i)
                
            print('-'*20)
            print('1.-Imprimir todos los cargos')
            print('2.-Seleccionar algun cargo especifico')
            print('-'*20)
            res = int(input('Ingrese la opcion: '))
            match res:
                case 1:
                    imprimir(lista_trabajadores)
                case 2:
                    cargo_especifico = []
                    buscar_cargo = input('Ingrese el cargo a buscar: ')
                    for i in lista_trabajadores:
                        for j in i:
                            if j == buscar_cargo:
                                cargo_especifico.append(i)
                    
                    imprimir(cargo_especifico)
                case _:
                    print('Opcion invalida, vuelva a hacerlo')
            
        case 4:
            print('Programa finalizado')
            break
        case _:
            print('Opcion invalida')
    