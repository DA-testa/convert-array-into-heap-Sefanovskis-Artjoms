# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(len(data),0,-1):
        currentElementIndex = i
        canSwap = True
        while canSwap:
            if currentElementIndex < 2:
                canSwap = False
                break
            parentElement = data[currentElementIndex//2-1]
            currentElement = data[currentElementIndex-1]

            if currentElement < parentElement:
                currentElement, parentElement = parentElement,currentElement
                swaps.append([currentElementIndex//2-1,currentElementIndex-1])
                currentElementIndex = currentElementIndex//2
            else:
                canSwap = False
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    # implement input form keyboard and from files
    inpMethod = input()
    # let user input file name to use, don't allow file names with letter a
    if "F" in inpMethod:
        fileName = input()
        if "a" in fileName:
            return
        with open("./tests/" + fileName, "r") as f:
            n = int(f.readline())
            data = list(map(int,f.readline().split()))
    elif "I" in inpMethod:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))



    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for val in swaps:
        print(val[0], val[1])


if __name__ == "__main__":
    main()
