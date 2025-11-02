def solution(array, commands):
    answer = []    
    for i in range(len(commands)):
        indexed_array = array[commands[i][0]-1:commands[i][1]]
        indexed_array.sort()
        answer.append(indexed_array[commands[i][2]-1])
    return answer