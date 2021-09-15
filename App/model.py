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
import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures.arraylist import subList
from DISClib.Algorithms.Sorting import insertionsort as insert
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(DataStructure):

    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure=DataStructure)
    catalog['artworks'] = lt.newList(datastructure=DataStructure)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creacion de datos

# Funciones de consulta

def getLastArtists(catalog, number):
    """
    Retorna los últimos artistas
    """
    artists = catalog['artists']
    size = lt.size(artists) + 1
    lastartists = lt.newList()
    for cont in range(size - number, size):
        artist = lt.getElement(artists, cont)
        lt.addLast(lastartists, artist)
    return lastartists

def getLastArtworks(catalog, number):
    """
    Retorna las últimas obras
    """
    artworks = catalog['artworks']
    size = lt.size(artworks) + 1
    lastartworks = lt.newList()
    for cont in range(size - number, size):
        artwork = lt.getElement(artworks, cont)
        lt.addLast(lastartworks, artwork)
    return lastartworks
    
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2 Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    DateAcquired_artwork_1 = artwork1['DateAcquired'].split('-')
    DateAcquired_artwork_2 = artwork2['DateAcquired'].split('-')
    if len(DateAcquired_artwork_1) != 1 and len(DateAcquired_artwork_2) != 1:
        value_artwork_1 = int(DateAcquired_artwork_1[0])*365 + int(DateAcquired_artwork_1[1])*30 + int(DateAcquired_artwork_1[2])
        value_artwork_2 = int(DateAcquired_artwork_2[0])*365 + int(DateAcquired_artwork_2[1])*30 + int(DateAcquired_artwork_2[2])
    elif len(DateAcquired_artwork_1) == 1 and len(DateAcquired_artwork_2) != 1:
        value_artwork_1 = 0
        value_artwork_2 = int(DateAcquired_artwork_2[0])*365 + int(DateAcquired_artwork_2[1])*30 + int(DateAcquired_artwork_2[2])
    elif len(DateAcquired_artwork_2) == 1 and len(DateAcquired_artwork_1) != 1:
        value_artwork_2 = 0
        value_artwork_1 = int(DateAcquired_artwork_1[0])*365 + int(DateAcquired_artwork_1[1])*30 + int(DateAcquired_artwork_1[2])
    else:
        value_artwork_1 = 0
        value_artwork_2 = 0
    return value_artwork_1 > value_artwork_2


# Funciones de ordenamiento

def sortArtworks_adquisition(catalog, saple_size, SortingMethod):
    '''
    Ordena la sublista de una tamaño dado por medio del 
    algoritmo de ordenamiento seleccionado 
    '''
    sub_list = lt.subList(catalog['artworks'], 1, saple_size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if SortingMethod == 1:
        sorted_list = insert.sort(sub_list, cmpArtworkByDateAcquired)
    elif SortingMethod == 2:
        sorted_list = shell.sort(sub_list, cmpArtworkByDateAcquired)
    elif SortingMethod == 3:
        sorted_list = merge.sort(sub_list, cmpArtworkByDateAcquired)
    else:
        sorted_list = quick.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    return elapsed_time_mseg, sorted_list