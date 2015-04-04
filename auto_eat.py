def auto_eat(encumbrance, inv_list, value, memo = None):
    """
    Finds the number of items that can be consumed
    from the player's inventory that provides the most "value" replenished and
    results in the least player encumberance.
    
    Input:
     inventory: list of usable items
     player: player class
     value - function that maps an item to some value. Currently using to map the heal_val attribute from items
        
    Output:
     list of items from inventory.
    
    """
    # Currently this function is not working as designed
    # Just base code that is used to test the auto_eat button
    if memo is None:
        memo = {}
    
    #inventory remaining
    new_enc = encumbrance
    total = 0
    #print("remain {} total {}".format(remain, total))
    new_inventory = inv_list
    sub_max = {}
    
    print("remaining encumb: {}".format(new_enc))

    if not (total,new_enc) in memo:
        if new_enc < smallest(new_inventory):
           # print("smallest {}".format(smallest(inventory)))
            return []
        else:
            sub_sol = {}
            for i in new_inventory:
                if i.size <= new_enc:
                    new_enc -= i.size
                    new_inventory.remove(i)
                    total += value(i)
                    if not total in sub_sol:
                        sub_sol[total] = []
                    sub_sol[total].append(i)
                    sub_sol[total].extend(auto_eat(new_enc, new_inventory, value, memo))
            memo[(total,new_enc)] = sub_sol[max(sub_sol)] if sub_sol else []

    return memo[(total,new_enc)]



def smallest(ilist):
    """
    Helper function that finds the smallest size in the list of items.
    """
    if not ilist:
        return 0
    current = ilist[0].size
    for i in ilist:
        if i.size < current:
            current = i.size
    return current


