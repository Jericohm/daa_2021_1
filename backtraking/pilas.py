class Stack:
    def __init__( self ):
        self.__data=list()

    def is_empty(self):
        return len(self.__data) == 0

    def length( self ):
        return len(self.__data)

    def push( self , item ):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
    def peek(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data)-1]

    def to_string( self ):
        for item in self.__data:
            print(f"| {item} |")