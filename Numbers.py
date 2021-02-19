
class Numbers:

    def filterEvenNumbers(self, numbers):
        nums = []

        for index, value in enumerate(numbers):
            if index%2 == 0 and value %2 == 0:
                nums.append(value)
        
        return nums

if __name__ == '__main__':
    obj = Numbers()
    result = obj.filterEvenNumbers([2,1,3,4,6,5,9,7,8,18,8,7,18])
    print(result)