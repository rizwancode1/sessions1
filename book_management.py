import json

# javascript object notation


FILE_NAME = "books.json"

# 1 load ; 2 save, 3 list_data # add book


# load data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            text = json.load(file)
            return text
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


# Book_data
def save_data(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file)


# list data
def list_data(books):
    print('\n')
    for index, book in enumerate(books, 1):
        print(f"({index}) Title: {book['title']}, Author: {book['author']}")


# add book
def add_book(books):
    title = input("Enter book title : ")
    author = input("Enter book author : ")
    books.append({"title": title, "author": author})

    # save to json
    save_data(books)


def update_book(books):
    list_data(books)

    index = int(input("Enter the number of book you want to update : "))

    if 1 <= index <= len(books):
        title = input("Enter book title you want to update : ")
        author = input("Enter book author  you want to update : ")
        books[index - 1] = {"title": title, "author": author}
        save_data(books)

    else:
        print("invalid number entered")





def delete_book(books):
    list_data(books)

    index = int(input("Enter the number of book you want to delete : "))

    if 1 <= index <= len(books):
        del books[index - 1]
        save_data(books)

    else:
        print("invalid number entered")


def main():

    books = load_data()

    while True:

        print("-------- Welcome to our book library -------")

        print("1. List books")
        print("2. Add a book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")

        try:
            print("\n")
            choice = int(input("Enter your choice : "))
            # print('type of choice', type(choice))
        except:
            print("invalid choice entered")


        if choice == 1:
            list_data(books)
        elif choice == 2:
            add_book(books)
        elif choice == 3:
            update_book(books)
        elif choice == 4:
            delete_book(books)
        elif choice == 5:
            break
        else:
            print("invalid choice entered")






if __name__ == "__main__":

    print(__name__)
    main()

