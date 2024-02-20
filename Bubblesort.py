def bubbleSort(mylist):
    n = len(mylist)

    # traverse through all the elements in the list
    for i in range(n-1):

        #last i elements are already in place
        #continue to sort the first (n-i)
        for j in range(0, n-i-1):

            #traverse the list from 0 to n-i-1
            #swap if the element found is greater than the next element
            if mylist[j] > mylist[j+1]:
                tmp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = tmp

starttime = timeit.default_timer()
bubbleSort(randomListOfIntegers)
endtime = timeit.default_timer()