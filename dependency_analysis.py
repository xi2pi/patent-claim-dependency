# -*- coding: utf-8 -*-
"""

@author: Christian Winkler
"""


def num_combinations(claim_):
    num_com_list = [0] * len(claim_)
    num_com_list[0] = 1
    
    num_com_list_idx = 0
    for i in claim_:
        if num_com_list_idx > 0:
            for j in i:
                num_com_list[num_com_list_idx] += num_com_list[j-1]
        num_com_list_idx += 1
            
    return num_com_list


##############

def dependency_check(claim, no_def):
    claim_def = [False] * len(claim)
    
    no_def = no_def 
    claim_def_idx = no_def
    claim_def[no_def-1] = True
    
    for i in claim[no_def:]:
        
        a = []
        
        for j in i:
            if j == no_def:
                a.append(True)
            elif claim_def[j-1]:
                a.append(True)
            else:
                a.append(False)
                
        claim_def[claim_def_idx] = all(a)    
        claim_def_idx += 1
        
            
    return claim_def

print("Loaded.")
#####





### DEPENDENCY CHECK

claim = [[1], [1], [1,2], [1], [2], [1,2,3,4,5], [2,5], [3,4]]
claim_containing_definition = 2


result = dependency_check(claim, claim_containing_definition)
print(result)


### NUMBER OF COMBINATION
# result = num_combinations(claim)
# print(result)
# print("Total combinations: " + str(sum(result)))


