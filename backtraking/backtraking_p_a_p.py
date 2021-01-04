# -*- coding: utf-8 -*-
import time
from colored import fg, bg, attr
from os import system
import time

from arrays import Array2D
from pilas import Stack

class LaberintoADT:
    def __init__(self , archivo_inicio):
        archivo = open(archivo_inicio, 'rt')
        self.__laberinto = Array2D(int(archivo.readline().strip()),int(archivo.readline().strip()),'1')
        self.__laberinto.clearing('1') # todo pared
        self.__entrada=[]
        self.__salida=[]
        self.__camino = Stack()
        self.__previa = None



        lineas = archivo.readlines()
        for ren in range(len(lineas)):
            lineas[ren]=lineas[ren].strip()
            col=0
            for cell in lineas[ren].split(','):
                self.__laberinto.set_item(ren,col,cell)
                col += 1
    def set_previa(self,posicion):
        self.__previa=posicion

    def get_previa(self):
        return self.__previa

    def mostrar_laberinto( self ):
        #self.__laberinto.to_string()
        for ren in range(self.__laberinto.get_num_rows()):
            for col in range(self.__laberinto.get_num_cols()):
                #print(self.string_to_wall(self.__laberinto.get_item(ren,col)),end='')
                self.string_to_wall(self.__laberinto.get_item(ren,col))
            print("")

    def mostrar_actual( self ):
        lab = self.__laberinto
        actual = self.__camino.peek()
        lab.set_item(actual[0],actual[1],'A')

        for ren in range(lab.get_num_rows()):
            for col in range(lab.get_num_cols()):
                self.string_to_wall(lab.get_item(ren,col))

            print("")


    def string_to_wall(self, celda):
        if celda == '1':
            print(
                    "{} {}{}".format(
                        bg('white'),
                        ' ',
                        attr("reset")),end='')
        elif celda== '0':
            print(
                    "{} {}{}".format(
                        bg('black'),
                        ' ',
                        attr("reset")),end='')
        elif celda == 'E':
            print(
                    "{} {}{}".format(
                        bg('blue'),
                        'E',
                        attr("reset")),end='')
        elif celda == 'S':
            print(
                    "{} {}{}".format(
                        bg('green'),
                        'S',
                        attr("reset")),end='')
        elif celda == 'C':
            print(
                    "{} {}{}".format(
                        bg('light_green'),
                        ' ',
                        attr("reset")),end='')
        elif celda == 'A':
            print(
                    "{} {}{}".format(
                        bg('light_green'),
                        ' ',
                        attr("reset")),end='')
        else:
            print(
                    "{} {}{}".format(
                        bg('red'),
                        ' ',
                        attr("reset")),end='')

    def set_entrada( self ):
        encontrada = False
        for ren in range(self.__laberinto.get_num_rows()):
            for col in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(ren,col) == 'E':
                    self.__entrada=[ren,col]
                    encontrada = True
                    self.__camino.push([ren,col])
        return encontrada

    def set_salida( self ):
        encontrada = False
        for ren in range(self.__laberinto.get_num_rows()):
            for col in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(ren,col) == 'S':
                    self.__salida=[ren,col]
                    encontrada = True
        return encontrada

    def agragar_solucion(self):
        while not self.__camino.is_empty():
            paso=self.__camino.pop()
            self.__laberinto.set_item(paso[0],paso[1],'C')


    def resolver( self ):
        actual = self.__camino.peek()

        # revisar izq
        if self.__laberinto.get_item(actual[0],actual[1]-1) == '0' \
            and self.__laberinto.get_item(actual[0],actual[1]-1) != 'X' \
            and self.get_previa() != [actual[0],actual[1]-1]:
            #print('mover izq')
            self.set_previa(actual)
            self.__camino.push([actual[0],actual[1]-1])
        # revisar arriba
        elif self.__laberinto.get_item(actual[0]-1,actual[1]) == '0'  \
        and self.__laberinto.get_item(actual[0]-1,actual[1]) != 'X' \
        and self.get_previa() != [actual[0]-1,actual[1]]:
            #print('mover arriba')
            self.set_previa(actual)
            self.__camino.push([actual[0]-1,actual[1]])
        # revisar der
        elif self.__laberinto.get_item(actual[0],actual[1]+1) == '0' \
        and self.__laberinto.get_item(actual[0],actual[1]+1) != 'X' \
        and self.get_previa() != [actual[0],actual[1]+1] :
            #print('mover derecha')
            self.set_previa(actual)
            self.__camino.push([actual[0],actual[1]+1])
        # revisar abajo
        elif self.__laberinto.get_item(actual[0]+1,actual[1]) == '0' \
        and self.__laberinto.get_item(actual[0]+1,actual[1]) != 'X' \
        and self.get_previa() != [actual[0]+1,actual[1]]:
            #print('mover abajo')
            self.set_previa(actual)
            self.__camino.push([actual[0]+1,actual[1]])
        else:
            self.__laberinto.set_item(actual[0],actual[1],'X')
            self.__camino.pop()


    def imprime_camino(self):
        self.__camino.to_string()

    def es_la_salida(self):
        actual = self.__camino.peek()
        try:
            if self.__laberinto.get_item(actual[0],actual[1]-1)=='S':
                return True
            elif self.__laberinto.get_item(actual[0]-1,actual[1])=='S':
                return True
            elif self.__laberinto.get_item(actual[0],actual[1]+1)=='S':
                return True
            elif self.__laberinto.get_item(actual[0]+1,actual[1])=='S':
                return True
            else:
                return False

        except Exception as e:
            print(f"Error:{e}")



def main():

    l = LaberintoADT('./entrada.lab')
    l.mostrar_laberinto()
    if l.set_entrada() :
        while not l.es_la_salida():
            l.resolver()
            #system('clear')
            l.mostrar_actual()

        l.imprime_camino()
        l.agragar_solucion() #vacia la pilas
        l.mostrar_laberinto()
    else:
        print("No hay entrada")
main()
