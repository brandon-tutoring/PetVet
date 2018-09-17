check_out_info = []
animals_we_take = ["dog", "cat"]

def print_pet(animal):
       print("Name - " + animal["name"])
       print("Kind - " + animal["kind"])
       print("Urgency - ", animal["urgency"])



def vet_function():

       while True:

               start = input("Hello, would you like to:\nCheck in(1)\nCheck out(2)\nShow all animals(3)\nSee most(4) or least(5) urgent\nFind by name(6)\nOr quit(7).\n").strip()

               if start == "1":
                       name_quest = input("What is your pet's name?").strip()
                       kind_quest = input("What kind of animal is your pet?").strip().lower()
                       if kind_quest not in animals_we_take:
                               print("Sorry, we do not take that animal, please try again.")
                               vet_function()
                       urgency_quest = input("What is your pets urgency?").strip()
                       if urgency_quest.isdigit() == False:
                               print("Sorry, that is not a valid input, please input a nuber and try again.")
                               continue
                       urgency_quest = int(urgency_quest)
                       check_out_info.append({"name":name_quest, "kind":kind_quest, "urgency":urgency_quest})

               elif start == "2":
                       if len(check_out_info) > 0:
                               for x in range(len(check_out_info)):
                                       print(x, check_out_info[x]["name"], check_out_info[x]["kind"], check_out_info[x]["urgency"])
                               sign_out_quest = int(input("Please choose the number of the pet you would like to sign out? "))
                               if sign out info < len(check_out_info):
                                       print("Sorry, there is no animla with that number, please try again.")
                                       continue
                               check_out_info.pop(sign_out_question)
                               continue
                       else:
                             print("There are no animals here.")

               elif start == "3":
                       if len(check_out_info) < 1:
                               print("There are no pets in the system at this time.")
                               continue
                       elif len(check_out_info) >= 1:
                               for i in range(0, len(check_out_info)):
                                      print_pet(i)

               elif start == "4":
                       if len(check_out_info) > 1:
                              most_urgent = [check_out_info[0]]
                              for i in range(1, len(check_out_info)):
                                     if check_out_info[i]["urgency"] < most_urgent[0]["urgency"]:
                                             continue
                                     elif check_out_info[i]["urgency"] == most_urgent[0]["urgency"]:
                                             most_urgent.append(check_out_info[i])
                                     elif check_out_info[i]["urgency"] > most_urgent[0]["urgency"]:
                                             most_urgent = check_out_info[i]
                              for animal in most_urgent:
                                     print_pet(animal)
                       elif len(check_out_info) == 1:
                               print_pet(check_out_info[0])
                       else:
                               print("Sorry there are no pets checked in a this time")
                               continue

               elif start == "5":
                      if len(check_out_info) < 1:
                              least_urgent = [check_out_info[0]]
                              for i in range(1, len(check_out_info)):
                                     if check_out_info[i]["urgency"] > least_urgent[0]["urgency"]:
                                             continue
                                     elif check_out_info[i]["urgency"] == least_urgent[0]["urgency"]:
                                             least_urgent.append(check_out_info[i])
                                     elif check_out_info[i]["urgency"] < least_urgent[0]["urgency"]:
                                             least_urgent = check_out_info[i]
                              for animal in most_urgent:
                                     print_pet(animal)
                       elif len(check_out_info) == 1:
                               print_pet(check_out_info[0])
                       else:
                               print("Sorry there are no pets checked in a this time")
                               continue

               elif start == "6":
                       if len(check_out_info) > 0:
                              find_name = input("What is the name of the pet you would like to find?\n")
                              for i in range(0, len(check_out_info)):
                                      if (check_out_info[item]["name"]) == find_name:
                                               print_pet(item)
                                      elif (check_out_info[item]["name"]) != find_name:
                                              print("That pet is not checked in.")
                       else:
                               print("Sorry there are no pets checked in a this time")
                               continue

               elif start == "7":
                       break


               else:
                       print("That was not a valid response, please try again.")
                       continue


vet_function()
