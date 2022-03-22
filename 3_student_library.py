class Library:
    def __init__(self,listofBooks):
        self.books = listofBooks              

    def displayAvailableBooks(self):
        print("Books Present in the library are: \n")
        for i in self.books:
            print(" ->"+i)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 14 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Have a great day:)")


class Student:
     def requestBook(self):
         self.book =input("Enter the name of the book you want to borrow: ")
         return self.book
    
     def returnBook(self):
         self.book=input("Enter the name of the book you want to return: ")
         return self.book
        

if __name__ == '__main__':
    centralLibrary = Library(["DSA","OOPS","Maths","COA","Computer Networks","Python","English"])
    student = Student()
    while (True):
        welcomeMsg='''\n  Welcome to Central Library  
        Please choose an option:
        1. Display all the books
        2. Request a Book
        3. Return a Book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("Enter you choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central Library")
            exit()
        else:
            print("Invalid choice")