def solution(sizes):    
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
        
    max_x, max_y = 0, 0 
    for size in sizes:
        if max_x < size[0]:
            max_x = size[0]
        if max_y < size[1]:
            max_y = size[1]
    
    return max_x * max_y


    
        
    
        