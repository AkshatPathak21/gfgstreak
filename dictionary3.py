def insert_dict(query, dict):
    
    dict[query[1]]=query[2]
    
    

# deleting from dictionary
def del_dict(query, dict):
    
   if (dict[query[1]]):
       del dict[query[1]]
       return True
   else:
       return False
        
    
    
    
    

# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print("Marks of {} is {}".format(key,dict[key]))
    else:
        return False
    
 