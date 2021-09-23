"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import sys
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print('')
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Elegir el tipo de ordenamiento que desea utilizar")
    print("3- REQ. 1: listar cronológicamente los artistas ")
    print("4- Organizar un número dado de obras de arte de acuerdo a su fecha de adquisición")
    print("5- REQ. 2: listar cronológicamente las adquisiciones")
    print("6- REQ. 3: clasificar las obras de un artista por técnica")
    print("7- REQ. 4: clasificar las obras por la nacionalidad de sus creadores")
    print("8- REQ. 5: transportar obras de un departamento")
    print("9- REQ. 6: proponer una nueva exposición en el museo")
    print("0- Salir")

def initCatalog(DataStructure):
    """
    Inicializa el catalogo de obras y artistas
    """
    return controller.initCatalog(DataStructure)

def loadData(catalog):
    """
    Carga la información en la estructura de datos
    """
    controller.loadData(catalog)

#######################################################################################################################
#Funciones de verificación
#######################################################################################################################

def InformationSampleInput(lst):
    size = lt.size(lst)
    print('El archivo tiene ', str(size), ' elementos.')
    sample_size = int(input('Ingrese el tamaño de la muestra: '))
    if sample_size > size:
        print('El tamaño de la muestra es mayor que el tamaño de los datos')
        valid = False
    else:
        valid = True

    return sample_size, valid

#######################################################################################################################
#Funciones de exposición de resultados
#######################################################################################################################

def printLastArtists(artists):
    print('Los últimos 3 artistas en el archivo cargado son: ')
    filteredList = controller.getTheLasttElements(artists,3)
    for artist in lt.iterator(filteredList):
            print('Nombre: ' + artist['DisplayName'] + ', Bio: ' + artist['ArtistBio'] +
              ', Nacionalidad: ' + artist['Nationality'] + ', Género: ' + artist['Gender'])

#######################################################################################################################

def printLastArtworks(artworks):
    print('Las últimas 3 obras de arte en el archivo cargado son: ')
    filteredList = controller.getTheLasttElements(artworks,3)
    for artwork in lt.iterator(filteredList):
        print('ID: ' + artwork['ObjectID'] + ', Titulo: ' + artwork['Title'] + ', Fecha de creación: ' +
               artwork['Date'] + ', Artist(as): ' + artwork['CreditLine'] + 
                ', Clasificación: ' + artwork['Classification'])

#######################################################################################################################

def PrintsortArtistYearBirth(result):
    size = lt.size(result)
    FirstFilteredList = controller.getTheFirstElements(result, 3) 
    LastFilteredList = controller.getTheLasttElements(result, 3) 

    print('Existen ', size, ' artistas registrados que nacieron en el rango de fechas indicado')
    print('')
    print('Los primeros 3 artistas son: ')
    for artist in lt.iterator(FirstFilteredList):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])
    print('')
    print('Los últimos 3 artistas son: ')  
    for artist in lt.iterator(LastFilteredList):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])

#######################################################################################################################

def PrintSortArtworksAdquisition(result):
    # TODO completar modificaciones para el laboratorio 4
    FilteredList = controller.getTheFirstElements(result, 10)
    print('Las primeras 10 obras de arte son: ')
    for artwork in lt.iterator(FilteredList):
        print('Titulo: ' + artwork['Title'] + ', Fecha de adquisición: ' + artwork['DateAcquired']) 
        

#######################################################################################################################

def PrintsortArtworksAdquisitionRange(result):
    size_purchase = result[2]
    size = lt.size(result[1])

    FirstFilteredList = controller.getTheFirstElements(result[1],3)
    LastFilteredList = controller.getTheLasttElements(result[1],3)
    print('Existen ', size, ' obras de arte adquiridas en el rango de fechas indicado')
    print('Existen', size_purchase, ' obras de arte adquiridas por compra en el rango de fechas indicado')
    print('')
    print('Las primeras 3 obras son: ')
    for artwork in lt.iterator(FirstFilteredList):
        ID = artwork['ConstituentID']
        ID_list = ID.strip(ID[0]).strip(ID[-1]).split(', ')
        Autors = ''
        for Autor_ID in ID_list:
            autor_name = ArtistsID[Autor_ID]['DisplayName']
            Autors += ' ,' + autor_name
        Autors = Autors[2:]

        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  Autors + 
                    ', Fecha: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras son: ')  
    for artwork in lt.iterator(LastFilteredList):
        ID = artwork['ConstituentID']
        ID_list = ID.strip(ID[0]).strip(ID[-1]).split(', ')
        Autors = ''
        for Autor_ID in ID_list:
            autor_name = ArtistsID[Autor_ID]['DisplayName']
            Autors += ' ,' + autor_name
        Autors = Autors[2:]

        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  Autors + 
                    ', Fecha de adquisición: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])

#######################################################################################################################

def PrintClasifyArtistsTechnique(result):
    total_artworks = result[1]
    total_techniques = result[2]
    most_used_technique = result[3]
    size_total = lt.size(total_artworks)
    size_techniques = len(total_techniques)
    print('Existen ', size_total, ' obras registradas del artista')
    print('El artista utilizó ', size_techniques, ' técnicas en sus obras')
    print('La técnica más utilizada por el artista es: '+ most_used_technique)
    print('')
    print('Las obras de arte del artista que utilizan esta técnica son: ')
    for artwork in lt.iterator(total_techniques[most_used_technique]):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] + 
                ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])

#######################################################################################################################

def PrintlasifyNationalityArtworks(result):
    FilteredList = controller.getTheFirstElements(result,10)
    
    print('Las primeras 10 nacionalidades por número de obras son: ')
    print('{:<20}{:<20}'.format('Nacionalidad','Número de obras'))
    for nationality in lt.iterator(FilteredList):
        num_artworks_nationality = lt.size(nationality[1])
        nationality_name = nationality[0]
        print('{:<20}{:<20}'.format(nationality_name,num_artworks_nationality))
    print('')
    artworks_major_nationality = lt.getElement(result,1)[1]
    num_artworks_major_nacionality = lt.size(artworks_major_nationality)
    print('Existen ', num_artworks_major_nacionality, ' obras de arte de la mayor nacionalidad')
    num_exposition = int(input('Ingrese el número de obras que desea ver de la mayor nacionalidad: '))
    print('')
    print('Las primeras', num_exposition,' obras de arte de la mayor nacionalidad son: ')
    NationalityFilteredList = controller.getTheFirstElements(artworks_major_nationality,num_exposition)
    for artwork in lt.iterator(NationalityFilteredList):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] + 
                ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])
    
#######################################################################################################################    

def PrintTransportArtworksDepartment(result):
    artworks_department = result[1]
    total_cost = result[2]
    total_weight = result[3]
    print('Se deben transportar', lt.size(artworks_department), ' obras de arte')
    print('El valor estimado de transporte de todas las obras es ', total_cost, ' USD')
    print('')
    print('Las 5 obras mas antiguas a transportar son: ')
    for artwork in lt.iterator(result[4]):
        artwork_data = artwork[0]
        print('Título: ' + artwork_data['Title'] + ', Clasificación' + artwork_data['Classification'] + 
                    ', Fecha de creación: ' + artwork_data['Date'] + ', Medio '+ artwork_data['Medium'] + 
                    ', Dimensiones: ' + artwork_data['Dimensions'] + ' Costo de transporte: ' + str(artwork[1]) + ' USD')  
    print('')
    print('Las 5 obras mas costosas para transportar son: ')
    for artwork in lt.iterator(result[5]):
        artwork_data = artwork[0]
        print('Título: ' + artwork_data['Title'] + ', Clasificación' + artwork_data['Classification'] + 
                    ', Fecha de creación: ' + artwork_data['Date'] + ', Medio '+ artwork_data['Medium'] + 
                    ', Dimensiones: ' + artwork_data['Dimensions'] + ' Costo de transporte: ' + str(artwork[1]) + ' USD')  

#######################################################################################################################
#Función de Menú
#######################################################################################################################
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Estructuras de datos disponibles:')
        print('1)Lista encadenada')
        print('2)Lista ordenada ')
        DataStructure_choice = input('Eliga el tipo de estrucura de datos: ')
        if DataStructure_choice == 1:
            DataStructure = 'SINGLE_LINKED'
        else:
            DataStructure = 'ARRAY_LIST'

        print("Cargando información de los archivos ....")
        catalog = initCatalog(DataStructure)
        loadData(catalog)
        ArtistsID = controller.ArtistsID(catalog['artists'])
        print('')
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('')
        artists = catalog['artists']
        printLastArtists(artists)
        print('')
        artworks = catalog['artworks']
        printLastArtworks(artworks)
        print('')
    elif int(inputs[0]) == 2:
        print('Algoritmos de ordenamiento disponibles: ')
        print('1) Insertion Sort')
        print('2) Shell Sort')
        print('3) Merge Sort')
        print('4) Quick Sort')
        SortingMethod = input('Ingrese el algoritmo elegido: ')
    elif int(inputs[0]) == 3:
        lst= catalog['artists']
        information = InformationSampleInput(lst)
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            initial_year_birth = int(input('Ingrese el primer año de nacimiento del intervalo: '))
            end_year_birth = int(input('Ingrese el último año de nacimiento del intervalo: '))
            print('Cargando...')
            result = controller.sortArtistYearBirth(lst, sample_size, SortingMethod, 
                                                        initial_year_birth, end_year_birth)
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            print('')
            PrintsortArtistYearBirth(result[1])

    elif int(inputs[0]) == 4:
        lst = catalog['artworks']
        information = InformationSampleInput(lst)
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            print('Cargando...')
            result = controller.sortArtworksAdquisition(lst,sample_size,SortingMethod)
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            print('')
            PrintSortArtworksAdquisition(result[1])
    elif int(inputs[0]) == 5:
        lst = catalog['artworks']
        information = InformationSampleInput(lst)
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            initial_date_adquisition = str(input('Ingrese la primera fecha de adquisición del intervalo: '))
            end_date_adquisition = str(input('Ingrese la primera de adquisición del intervalo: '))
            print('Cargando...')
            result = controller.sortArtworksAdquisitionRange(lst, sample_size, SortingMethod, 
                                                        initial_date_adquisition, end_date_adquisition)
            print('Cargando...')
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            print('')
            PrintsortArtworksAdquisitionRange(result)
    elif int(inputs[0]) == 6:
        information = InformationSampleInput(catalog['artworks'])
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            Artists_name = input('Ingrese el nombre del artista: ')
            print('Cargando...')
            result = controller.ClasifyArtistsTechnique(catalog, sample_size, Artists_name)
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            print('')
            PrintClasifyArtistsTechnique(result)
    elif int(inputs[0]) == 7:
        information = InformationSampleInput(catalog['artworks'])
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            print('Cargando...')
            result = controller.ClasifyNationalityArtworks(catalog, sample_size, SortingMethod)
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            print('')
            PrintlasifyNationalityArtworks(result[1])
    elif int(inputs[0]) == 8:
        information = InformationSampleInput(catalog['artworks'])
        sample_size = information[0]
        valid = information[1]
        if valid == True:
            department = str(input('Ingrese el nombre del departamento: '))
            print('Cargando...')
            result = controller.TransportArtworksDepartment(catalog, sample_size, SortingMethod, department)
            print('')
            print("Para la muestra de", sample_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0]))
            PrintTransportArtworksDepartment(result)              
    else:
        sys.exit(0)
sys.exit(0)