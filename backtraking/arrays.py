"""
Array
"""
class Array(object):

    def __init__(self, tamano):
        self.__tamano=tamano
        self.__array=[0 for x in range(self.__tamano)]

    def to_string(self):
        print("----")
        print(self.__array)

    def len(self):
        return self.__tamano

    def set_item(self,index , valor):
        if self.__check_limits__(index):
            self.__array[index]=valor
        else:
            raise Exception('Error de limites en index')

    def get_item(self,index):
        return self.__array[index]

    def clear(self, valor):
        self.__array=[valor for x in range(self.__tamano)]

    def __check_limits__(self ,index):
        return index >=0 and index < self.__tamano

"""
Array2D
"""

class Array2D:

    def __init__(self,rows, cols, value):
        self.__cols = cols
        self.__rows = rows
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rows)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__cols)]
        print("")

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,row,col):
        return self.__array[row][col]

    def set_item( self , row , col , valor ):
        self.__array[row][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col]=valor

"Array3D"

class Array3D:
        def __init__( self , depth , rows , cols , value ):
            self.__depth = depth
            self.__cols = cols
            self.__rows = rows
            self.__array =[[[value for x in range(self.__cols)] for y in range(self.__rows)] for z in range(self.__depth)]


        def to_string(self):
            [print("---",end="") for x in range(self.__cols)]
            print("")
            dim = 1
            for d in self.__array:
                print(f"========= Dim {dim} ===========")
                for row in d:
                    print(row)
                dim += 1
            [print("---",end="") for x in range(self.__cols)]
            print("")



        def get_num_rows(self):
            return self.__rows

        def get_num_cols(self):
            return self.__cols

        def get_depth( self ):
            return self.__depth

        def get_item(self,depth,row,col):
            return self.__array[depth][row][col]

        def set_item( self, depth , row , col , valor ):
            self.__array[depth][row][col]=valor

        def clear(self, valor=0):
            for dep in range(self.__depth):
                for ren in range(self.__rows):
                    for col in range(self.__cols):
                        self.set_item(dep,ren,col,valor)