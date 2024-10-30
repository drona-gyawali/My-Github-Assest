from content import personal_diary
from config import host,user,password,database

def main():
    run=personal_diary(host=host,user=user,database=database,password=password)


    while True:
    print("\n Welcome to our note app")
    print("1. Add Content")
    print("2. View all Content")
    print("3. View by date")
    print("4. Delete Content")
    print("5. Save content")
    print("6. Exit")
    choice = input("Choose an option: ")

    actions = {
        '1': run.create_note,
        '2': run.view_content,
        '3': run.search_date,
        '4': run.delete_content,
        '5': run.save_local,
        '6': lambda: print("You chose to Exit")
    }

    action = actions.get(choice, lambda: print("Invalid option"))
    
    # If choice is '6', break the loop after printing the exit message
    if choice == '6':
        action()
        break
    else:
        action()

if __name__=='__main__':
    main()

