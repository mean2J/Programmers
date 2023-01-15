def solution(array, commands):
    answer=[]
    for cutCommands in commands:
        i=cutCommands[0]
        j=cutCommands[1]
        k=cutCommands[2]
        cutArray=array[i-1:j]
        cutArray.sort()
        answer.append(cutArray[k-1])
    return answer