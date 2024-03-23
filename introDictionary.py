def create_dict(arr):
    
    dict = {}
    for i in range(len(arr)):
        dict[arr[i][0]] = arr[i][1]
    
    
    return dict

