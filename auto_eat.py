def auto_eat(player, inv_list, value, memo = None, remain = None):
    """
    Finds the smallest number of items that can restore the amount of missing
    'value' (health, hunger, stamina, etc.)
    
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
    if inv_list is None:
        return []
    
    #player value remaining
    new_remain = remain
    total = 0
    #print("remain {} total {}".format(remain, total))
    new_inventory = inv_list

    if not (total, remain) in memo:
        if remain < smallest(new_inventory,value):
            print("remain smaller than smallest")
            return []
        else:
            sub_sol = {}
            for i in new_inventory:
                if value(i) <= remain and value(i) > 0:
                    new_remain -= value(i)
                    new_inventory.remove(i)
                    total += value(i)
                    if not total in sub_sol:
                        sub_sol[total] = []
                    sub_sol[total].append(i)
                    print("appended i {}".format(sub_sol[total]))
                    sub_sol[total].extend(auto_eat(player, new_inventory, value, memo,new_remain))
            memo[(total,remain)] = sub_sol[max(sub_sol)] if sub_sol else []
    print("total {}".format(total))
    print("memo {}" .format(memo[(total,remain)]))
    return memo[(total,remain)]



def smallest(ilist,value):
    """
    Helper function that finds the smallest size in the list of items.
    """
    if ilist == []:
        return 0
    current = value(ilist[0])
    for i in ilist:
        if value(i) < current:
            current = value(i)
    return current


