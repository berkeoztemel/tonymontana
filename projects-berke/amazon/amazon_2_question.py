

class AscendingOrder:
    def bubble_sort(array):
        '''Create a program in any language to arrange the numbers in ascending order.
        '''
        n = len(array)

        for i in range(n):
            for j in range(n-i-1):
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1], array[j]
        return array










