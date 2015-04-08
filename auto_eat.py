def auto_eat(player, inv_list, value, memo = None, remain = None):
    """
    Finds the list of items that restores the amount of hunger and relieves the highest amount of 'value' (encumbrance)
    
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
    if remain is None:
        remain = player.hunger
    if inv_list == []:
        return []
    
    #player value remaining
    new_remain = remain

    new_inventory = inv_list
    inv_id = tuple(new_inventory)

    if not (new_remain, inv_id) in memo:
        if new_remain < smallest(new_inventory):
            memo[(new_remain, inv_id)] = []
        else:
            # try using a dictionary again
            sub_sol = {}
            total = 0
            for i in new_inventory:
                new_inventory.remove(i)
                if i.hung_value <= new_remain and i.hung_value > 0:
                    new_remain -= value(i)
                    inv_id = tuple(new_inventory)
                    total += value(i)
                    print("new remain {} total size {}".format(new_remain, total))
                    if not total in sub_sol:
                        sub_sol[total] = []
                    sub_sol[total].append(i)
                    sub_sol[total].extend(auto_eat(player, new_inventory, value, memo,new_remain))
                    print("sub {} total {}".format(sub_sol[total], total))

            memo[(new_remain, inv_id)] = sub_sol[max(sub_sol)] if sub_sol else []
    return memo[(new_remain, inv_id)]



def smallest(ilist):
    """
    Helper function that finds the smallest size in the list of items.
    """
    if ilist == []:
        return 0
    current = ilist[0]
    for i in ilist:
        if -1*i.hung_value < current:
            current = -1*i.hung_value
    return current


