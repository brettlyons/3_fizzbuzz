    newList = list(intList)
        # newList is the list to be returned, copy to prevent unwanted mutation
        # of intList.
        for i in range(len(intList)):
            if intList[i] % 5 == 0 and intList[i] % 3 == 0:
                newList[i] = "FizzBuzz"
                elif intList[i] % 3 == 0:
                    newList[i] = "Fizz"
                elif intList[i] % 5 == 0:
                    newList[i] = "Buzz"
                else:
                    newList[i] = intList[i]
                return newList
