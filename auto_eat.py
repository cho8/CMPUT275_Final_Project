def auto_eat(inv_remain, inv_list, value, memo = None):
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
    remain = inv_remain
    total = 0
    #print("remain {} total {}".format(remain, total))
    new_inventory = inv_list
    sub_max = {}
    
    print("remaining inv: {}".format(remain))

    if not (total,remain) in memo:
        if remain < smallest(new_inventory):
           # print("smallest {}".format(smallest(inventory)))
            return []
        else:
            sub_sol = []
            for i in new_inventory:
                if i.size <= remain:
                    remain -= i.size
                    new_inventory.remove(i)
                    total += value(i)
                    sub_sol.append(i)
                    sub_sol.extend(auto_eat(remain, new_inventory, value, memo))
            memo[(total,remain)] = sub_sol

    return memo[(total,remain)]



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


