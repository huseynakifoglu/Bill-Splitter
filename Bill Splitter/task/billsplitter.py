# write your code here
import random

number_of_people = int(input("Enter the number of friends joining (including you):\n"))
names = dict()


# function for splitting bill amount people and updating dictionary
def bill_split(list_of_people, bill):
    for member in list_of_people:
        # checking each item of dictionary and updating based on number of items in dictionary
        list_of_people[member] = round((bill / len(list_of_people)), 2)
    return list_of_people


def bill_split_lucky(list_of_people, bill, lucky):
    for member in list_of_people:
        # checking each item of dictionary and updating based on number of items in dictionary
        list_of_people[member] = round((bill / (len(list_of_people) - 1)), 2)
    list_of_people[lucky] = 0
    return list_of_people


def choose_lucky(people):
    lucky = random.choice(list(people.keys()))
    return lucky


if number_of_people > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_people):
        names[input()] = 0
    total_bill = input('Enter the total bill value:\n')
    is_lucky_feature_needed = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if is_lucky_feature_needed == "Yes":
        print(f'{choose_lucky(names)} is the lucky one!')
        print(bill_split_lucky(names, int(total_bill), choose_lucky(names)))
    else:
        print('No one is going to be lucky')
        print(bill_split(names, int(total_bill)))
else:
    print("No one is joining for the party")
