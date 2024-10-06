
class SegregateArray():
    def segregate_array(array):
        '''Create a program in any language to segregate an array of random numbers by EVEN or ODD value.
         On completion of the program, EVEN values should be in the lower array indexes while ODD values should be in the higher array indexes.
        '''
        n = len(array)

        for i in range(n):
            for j in range(n-i-1):
                if not array[j] % 2 == 0:
                    array[j] , array[j+1] = array[j+1], array[j]

        return array





