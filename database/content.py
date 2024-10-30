import mysql.connector
from datetime import datetime

class personal_diary:
    def __init__(self,host,user,database,password) -> None:
        self.conn=mysql.connector.connect(
        host=host,
        user=user,
        database=database,
        password=password
        )
        self.cursor=self.conn.cursor()
    
    def create_note(self):
        content=input('Enter the content')
        time=datetime.now()
        query="INSERT INTO diary_entries (entry_date, content) VALUES (%s, %s)"
        self.cursor.execute(query,(time,content))
        self.conn.commit()
        print(f'Content has been saved')

    def search_date(self):
        content=input('Enter the date please')
        query= "select * from diary_entries where entry_date = %s"
        self.cursor.execute(query,(content,))
        result=self.cursor.fetchall()
        try:
            if result:
                for row in result:
                    print(f'Date: {row[1]}, Content: {row[2]}')
            else:
                print(f'Not a valid {content}')
        except Exception as e:
            print('Something went wrong', e)
        
    
    def view_content(self):
        query="select * from diary_entries order by entry_date desc"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        try:
            if result:
                for row in result:
                    print(f'Date: {row[1]}, Content: {row[2]}')
            else:
                print('Nothing to show')
        except Exception as e:
            print('Something went wrong /', e )
    
    def delete_content(self):
        content=input('Enter the date for deletion')
        query="delete from diary_entries where entry_date= %s"
        self.cursor.execute(query,(content,))
        self.conn.commit()
        print(f'Content created on {content} has been removed permanently')

    
    def save_local(self,filename='diary.txt'):
        query="select * from diary_entries order by entry_date desc"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        with open(filename,'w') as file:
            try:
                for entry in result:
                    file.write(f"Date: {entry[1]}\nEntry: {entry[2]}\n\n")
                print(f'Entries Saved on {filename}')
            except Exception as e:
                print('Ethier file not present or', e)
        

    
    # def __del__(self):
    #     self.cursor.close()
    #     self.conn.close()




