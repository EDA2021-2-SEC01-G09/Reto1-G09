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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList()
    catalog['artworks'] = lt.newList()

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

# Funciones de ordenamiento