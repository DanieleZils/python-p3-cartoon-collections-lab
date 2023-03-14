def roll_call_dwarves(dwarf_names):
    for i, name in enumerate(dwarf_names, start=1): 
        print(f"{i}. {name}")

# the count = 1
# for one_name in some_list :
# print (f"{the_count}. {one_name}")
  
# roll_call_dwarves(["adam", "maria", "joao"])
def summon_captain_planet(planeteer_calls):
    capitalized_calls = [call.capitalize() + "!" for call in planeteer_calls]
    return capitalized_calls

def long_planeteer_calls(calls):
     for call in calls:
        if len(call) > 4:
            return True
     return False

# long_planeteer_calls(["wof","bar","woooof"])

def find_the_cheese(some_list):
    the_cheeses = ["cheddar", "gouda", "camembert"]
    for food in some_list:
        if food in the_cheeses:
            return food
    return None

  
# find_the_cheese(["thyme", "tomato", "cheddar", "gouda"])