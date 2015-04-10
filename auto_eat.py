def auto_eat(remain_enc, inv_list, value, memo = None):
    """
    Finds the list of items that restores the amount of value and relieves the highest amount of encumbrance.
    Prioritizes encumbrance relief over hunger.
    
    Input:
     encumbrance: the total amount of space filled in the inventory
     inv_list: list of items in inventory.
     player: player class
     value - function that maps an item to some value. Currently using to map the heal_val attribute from items
        
    Output:
     list of items from inventory.
    
    """
    # Currently this function is not working as designed
    # Just base code that is used to test the auto_eat button
    
    if memo is None:
        memo = {}
    if inv_list == []:
        return []
    
    #player value remaining
    new_remain = remain_enc

    new_inventory = inv_list
    inv_id = tuple(new_inventory)

    if not (new_remain, inv_id) in memo:
        if new_remain < smallest(new_inventory,value):
            memo[(new_remain, inv_id)] = []
        else:
            # try using a dictionary again
            sub_sol = {}
            total = 0
            for i in inv_list:
                if i.size <= new_remain:
                    new_remain -= i.size
                    new_inventory.remove(i)
                    inv_id = tuple(new_inventory)
                    total += value(i)
                    print("new remain {} total size {}".format(new_remain, total))
                    if not total in sub_sol:
                        sub_sol[total] = []
                    sub_sol[total].append(i)
                    sub_sol[total].extend(auto_eat(new_remain, new_inventory, value, memo))
                    print("sub {}".format(sub_sol[total]))
                new_remain = remain_enc
            memo[(new_remain, inv_id)] = sub_sol[max(sub_sol)] if sub_sol else []
    else:
        print("memo!")
    return memo[(new_remain, inv_id)]



def smallest(ilist, value):
    """
    Helper function that finds the smallest size in the list of items.
    """
    if ilist == []:
        return 0
    current = ilist[0]
    for i in ilist:
        if value(i) < value(current):
            current = i
    return value(current)



