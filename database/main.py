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

        if choice=='1':
            run.create_note()
        elif choice=='2':
            run.view_content()
        elif choice=='3':
            run.search_date()
        elif choice=='4':
            run.delete_content()
        elif choice=='5':

            run.save_local()
        elif choice=='6':
            print('You choose to Exit')
            break
        else:
            print('Invaild option')

if __name__=='__main__':
    main()

