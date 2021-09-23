"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time
import math
import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures.arraylist import size, subList
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#######################################################################################################################
# Construccion de modelos
#######################################################################################################################

def newCatalog(DataStructure):

    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure=DataStructure)
    catalog['artworks'] = lt.newList(datastructure=DataStructure)

    return catalog

#######################################################################################################################
# Funciones para agregar informacion al catalogo
#######################################################################################################################

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

#######################################################################################################################

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

#######################################################################################################################
# Funciones para creacion de datos
#######################################################################################################################
def ArtistsID(lst):
    ArtistsID = {}
    for artist in lt.iterator(lst):
        artist_ID = artist['ConstituentID']
        ArtistsID[artist_ID] = artist
    return ArtistsID

#######################################################################################################################

def filteringArtistYearBirth(sub_list, initial_year_birth, end_year_birth):
    date_artists = lt.newList(datastructure='ARRAY_LIST')
    for artist in lt.iterator(sub_list):
        artistsBirthDate = int(artist['BeginDate'])
        if initial_year_birth <= artistsBirthDate and artistsBirthDate <= end_year_birth:
            lt.addLast(date_artists, artist)
    return date_artists

#######################################################################################################################

def filteringArtworksAdquisitionDate(sub_list,initial_date_adquisition,end_date_adquisition):
    date_artworks = lt.newList(datastructure='ARRAY_LIST')
    for artwork in lt.iterator(sub_list):
        artworkAdquisitionDate = artwork['DateAcquired']
        artworkAdquisitionDate_in_days = transformation_date_to_days(artworkAdquisitionDate)
        initial_date_adquisition_in_days = transformation_date_to_days(initial_date_adquisition)
        end_date_adquisition_in_days = transformation_date_to_days(end_date_adquisition)
        if initial_date_adquisition_in_days <= artworkAdquisitionDate_in_days and artworkAdquisitionDate_in_days <= end_date_adquisition_in_days:
            lt.addLast(date_artworks, artwork)
    return date_artworks

#######################################################################################################################

def filteringArtworksAdquisitionDate_Purchase(date_artworks):
    purchase_artworks = lt.newList(datastructure='ARRAY_LIST')
    for artwork in lt.iterator(date_artworks):
        artwork_adquisition = artwork['CreditLine']
        if 'purchase' in artwork_adquisition.lower():
            lt.addLast(purchase_artworks, artwork)
    return purchase_artworks

#######################################################################################################################

def creationInformationTechniquesArtist(sub_list, lst, artist_name):
    artist_ID = getConstituentID_artist(lst, artist_name)
    artist_artworks = lt.newList(datastructure='ARRAY_LIST')
    artist_techniques = {}

    for artwork in lt.iterator(sub_list):
        ID = artwork['ConstituentID']
        artwork_constituent_IDs = ID.strip(ID[0]).strip(ID[-1]).split(', ')
        if artist_ID in artwork_constituent_IDs:
            lt.addLast(artist_artworks, artwork)
            artwork_technique = artwork['Medium']
            if artwork_technique not in artist_techniques:
                artist_techniques[artwork_technique] = lt.newList(datastructure='ARRAY_LIST')
                lt.addLast(artist_techniques[artwork_technique], artwork)
            else:
                lt.addLast(artist_techniques[artwork_technique], artwork)

    return artist_artworks, artist_techniques

#######################################################################################################################
# Funciones de consulta
#######################################################################################################################

def getTheFirstElements(lst, num):
    """
    Retorna los primeros elementos de la lista
    """
    FirstElements = lt.newList()
    for index in range(1, num + 1):
        element = lt.getElement(lst, index)
        lt.addLast(FirstElements, element)
    return FirstElements

#######################################################################################################################

def getTheLasttElements(lst, num):
    """
    Retorna los últimos elementos de la lista
    """
    size = lt.size(lst) + 1
    LastElements = lt.newList()
    for index in range(size - num, size):
        element = lt.getElement(lst, index)
        lt.addLast(LastElements, element)
    return LastElements
    
#######################################################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
#######################################################################################################################

def cmpArtistByBirthDate(artist1, artist2):
    BirthDate_artist1 = int(artist1['BeginDate'])
    BirthDate_artist2 = int(artist2['BeginDate'])

    return BirthDate_artist1 > BirthDate_artist2

#######################################################################################################################

def transformation_date_to_days(date):
    date_list = date.split('-')
    if len(date_list) != 1:
        date_in_days = int(date_list[0])*365 + int(date_list[1])*30 + int(date_list[2])
    else:
        date_in_days = 0
    return date_in_days

#######################################################################################################################

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2 Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    DateAcquired_artwork_1 = transformation_date_to_days(artwork1['DateAcquired'])
    DateAcquired_artwork_2 = transformation_date_to_days(artwork2['DateAcquired'])
    return DateAcquired_artwork_1 > DateAcquired_artwork_2

#######################################################################################################################

def getConstituentID_artist(lst, artist_name_input):
    artist_list_size = lt.size(lst)
    found_artist = False
    index = 1
    while found_artist == False and index <= artist_list_size:
        artist =lt.getElement(lst, index)
        artist_name_list = artist['DisplayName']
        if artist_name_list.lower() == artist_name_input.lower():
            artist_ID = artist['ConstituentID']
            found_artist = True
        else:
            index += 1
    return artist_ID

#######################################################################################################################

def cmpNationalities(nationality1, nationality2):
    size_nationality1 = lt.size(nationality1[1])
    size_nationality2 = lt.size(nationality2[1])
    return size_nationality1 > size_nationality2

#######################################################################################################################

def cmpArtworkByDateCreated(artwork1, artwork2):
    DateCreated_artwork1 = artwork1[0]['Date']
    DateCreated_artwork2 = artwork2[0]['Date']

    return DateCreated_artwork1 > DateCreated_artwork2

#######################################################################################################################

def cmpArtworkBycost(artwork1, artwork2):
    Cost_artwork1 = artwork1[1]
    Cost_artwork2 = artwork2[1]

    return Cost_artwork1 > Cost_artwork2

#######################################################################################################################

def calculate_dimensions_weight(Weight, Length, Width, Height):
    if Weight != '':
        Weight = float(Weight)
    else:
        Weight = 0
    
    if Width != '' and Length != '':
        area = float(Height)*float(Length)/10000
    else:
        area = 0
    
    if Height != '':
        volume = area*float(Height)/100
    else:
        volume = area

    return Weight, area, volume

#######################################################################################################################

def cmpArtworkBySize(artwork1, artwork2):
    Height1 = artwork1['Height']
    Height2 = artwork2['Height']
    Length1 = artwork1['Length']
    Length2 = artwork2['Length']
    Width1  = artwork1['Width']
    Width2  = artwork2['Width']

    area1 = calculate_dimensions_weight(0, Length1, Width1, Height1)[1]
    area2 = calculate_dimensions_weight(0, Length2, Width2, Height2)[1]

    return area1 > area2

#######################################################################################################################
# Funciones de ordenamiento
#######################################################################################################################

def SortingMethodExecution(SortingMethod, sub_list, cmpFunction):
    if SortingMethod == 1:
        sorted_list = insertion.sort(sub_list, cmpFunction)
    elif SortingMethod == 2:
        sorted_list = shell.sort(sub_list, cmpFunction)
    elif SortingMethod == 3:
        sorted_list = merge.sort(sub_list, cmpFunction)
    else:
        sorted_list = quick.sort(sub_list, cmpFunction)

    return sorted_list

#######################################################################################################################

def sortArtistYearBirth(sub_list, SortingMethod, initial_year_birth, end_year_birth):
    sub_list = sub_list.copy()
    start_time = time.process_time()

    date_artists = filteringArtistYearBirth(sub_list, initial_year_birth, end_year_birth)

    sorted_list = SortingMethodExecution(SortingMethod, date_artists, cmpArtistByBirthDate)
    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    
    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def sortArtworksAdquisition(sub_list, SortingMethod):
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = SortingMethodExecution(SortingMethod, sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def sortArtworksAdquisitionRange(sub_list, SortingMethod, initial_date_adquisition, end_date_adquisition):
    sub_list = sub_list.copy()
    start_time = time.process_time()

    date_artwork = filteringArtworksAdquisitionDate(sub_list,initial_date_adquisition,end_date_adquisition)
    purchase_artworks_num = lt.size(filteringArtworksAdquisitionDate_Purchase(date_artwork))

    sorted_list_date = SortingMethodExecution(SortingMethod, date_artwork, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    
    return elapsed_time_mseg, sorted_list_date, purchase_artworks_num

#######################################################################################################################

def ClasifyArtistsTechnique(sub_list, lst, artist_name):
    sub_list = sub_list.copy()
    start_time = time.process_time()

    information = creationInformationTechniquesArtist(sub_list, lst, artist_name)
    artist_artworks = information[0]
    artist_techniques = information[1]

    major_technique_artwork_num = 0
    for technique in artist_techniques:
        technique_artwork_num = lt.size(artist_techniques[technique])
        if technique_artwork_num > major_technique_artwork_num:
            major_technique_artwork_num = technique_artwork_num
            major_technique = technique

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return elapsed_time_mseg, artist_artworks, artist_techniques, major_technique

#######################################################################################################################

def ClasifyNationalityArtworks(sub_list, lst, SortingMethod):
    sub_list = sub_list.copy()
    start_time = time.process_time()
    ArtistsID_list = ArtistsID(lst)
    NationalitiesArtworks = {}

    for artwork in lt.iterator(sub_list):
        ID = artwork['ConstituentID']
        ID_list = ID.strip(ID[0]).strip(ID[-1]).split(', ')
        for Constituent_ID in ID_list:
            artist = ArtistsID_list[Constituent_ID]
            artists_nationality = artist['Nationality']
            if artists_nationality == '':
                artists_nationality = 'Desconocido'
            if artists_nationality not in NationalitiesArtworks:
                NationalitiesArtworks[artists_nationality] = lt.newList(datastructure='ARRAY_LIST')
                lt.addLast(NationalitiesArtworks[artists_nationality], artwork)
            else:
                lt.addLast(NationalitiesArtworks[artists_nationality], artwork)

    List_artworks_nationalities = lt.newList(datastructure='ARRAY_LIST')
    for nationality in NationalitiesArtworks:
        artworks = NationalitiesArtworks[nationality]
        element = [nationality, artworks]
        lt.addLast(List_artworks_nationalities, element)
    
    sorted_list = SortingMethodExecution(SortingMethod, List_artworks_nationalities, cmpNationalities)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def TransportArtworksDepartment(sub_list, SortingMethod, department):
    start_time = time.process_time()
    ArtworksDepartment = lt.newList()
    total_cost = 0
    total_weight = 0

    for artwork in lt.iterator(sub_list):
        department_artwork = artwork['Department']
        if department_artwork == department:
            Weight = artwork['Weight (kg)']
            Height = artwork['Height (cm)']
            Length = artwork['Length (cm)']
            Width = artwork['Width (cm)']

            dimensions_weight = (Weight, Length, Width, Height)
            cost_rectangular = dimensions_weight[2]
            cost_weight = dimensions_weight[0]

            if cost_rectangular != 0 or cost_weight != 0:
                if cost_weight < cost_rectangular:
                    artwork_cost = cost_rectangular
                else:
                    artwork_cost = cost_weight
            else:
                artwork_cost = 48
            
            total_cost += artwork_cost

            lt.addLast(ArtworksDepartment, [artwork, artwork_cost])

    sub_list_date = ArtworksDepartment.copy()
    sub_list_cost = ArtworksDepartment.copy()
    ordered_list_date = SortingMethodExecution(SortingMethod, sub_list_date, cmpArtworkByDateCreated)
    ordered_list_cost = SortingMethodExecution(SortingMethod, sub_list_cost, cmpArtworkBycost)
    oldest_artworks = lt.subList(ordered_list_date,1,5)
    most_expensive_artworks = lt.subList(ordered_list_cost,1,5)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, ArtworksDepartment, total_cost, total_weight, oldest_artworks, most_expensive_artworks

#######################################################################################################################
                
def CreateARtworkExposition(catalog, sample_size, SortingMethod, initial_year_creation, end_year_creation, total_area):
    sub_list = lt.subList(catalog['artworks'], 1, sample_size)
    date_artworks_list = lt.newList(datastructure='ARRAY_LIST')
    start_time = time.process_time()

    for artwork in lt.iterator(sub_list):
        artworkCreationDate = int(artwork['Date'])
        Height = artwork['Height']
        Length = artwork['Length']
        Width  = artwork['Width']
        if (initial_year_creation <= artworkCreationDate and artworkCreationDate <= end_year_creation) and (Length != '' and Width != '') and Height == '':
            lt.addLast(date_artworks_list, artwork)
            
    sorted_list = SortingMethodExecution(SortingMethod, date_artworks_list, cmpArtworkBySize)
    exposition_artworks = lt.newList()

    area_filled = 0
    index = 1
    while area_filled <= total_area and index <= lt.size(sorted_list):
        artwork = lt.getElement(sorted_list, index)
        artwork_area = artwork['Length']*artwork['Width']
        area_filled += artwork_area
        lt.addLast(exposition_artworks, artwork)

    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    
    return elapsed_time_mseg, exposition_artworks, area_filled