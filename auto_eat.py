
def auto_eat(remain_enc, inv_list, value,memo = None):
    """
    Finds the list of items that relieves the encumbered state and relieves the highest amount of hunger.
    Prioritizes encumbrance relief over hunger.
    
    Input:
     encumbrance: the total amount of space filled in the inventory
     inv_list: list of items in inventory.
     player: player class
     value - function that maps an item to some value. Currently using to map the heal_val attribute from items

    Output:
     subset of items from inventory.
     
    Complexity:
     We think the run time is worst case O(n*m^2), where n is the number of
     items in the inventory, and m is the remaining target encumbrance.
     This is because gather
    """
    if memo is None:
        memo = {}
    if inv_list == []:
        return []

    max_remain = remain_enc

    #The maximum valued list for this specific layer
    max = list()

    maxvalue = 0
    for i in inv_list:
        sub_sol = list()
        copy = inv_list.copy()
        copy.remove(i)
        layer = tuple(copy)
        
        # If the layer's empty, return
        if layer == tuple([]):
            return []

        #Check if we already have a max value list for this layer.
        if layer not in memo:
            if i.size <= remain_enc and value(i) > 0:
                remain_enc -= i.size
                sub_sol.append(i)
                sub_sol.extend(auto_eat(remain_enc,copy,value,memo))
                
                
                sub_sol_val = list_value(sub_sol,value)
                
                #if the 'sub_sol' list has a higher value than 'max', then 'sub_sol'
                #becomes 'max' for this layer.
                if sub_sol_val > maxvalue: 
                    maxvalue = sub_sol_val
                    max = sub_sol
                    
        remain_enc = max_remain
        inv_list.remove(i)

        #After iterating through all possibilities in inv_list, assign the max value
        #list for the layer to memo[layer]
        memo[layer] = max
    
    return memo[layer]


def list_value(list,value):
    """
    #returns the total value of the list passed in based on the function 'value' that is
    #taken as an argument.
    """
    total = 0
    for val in list:
        total += value(val)
    return total

