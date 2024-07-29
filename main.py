import databaseHandler as dbhm
import logging

def main():

    #logging
    logging.basicConfig(filename="Bookstore.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    dbh = dbhm.databaseHandler()
    logging.info("Connected to bookstore database.")
    while True:
        response = input("\nSelect what you would like to do.\n[L] Login\n[C] Create Account\n")
        response = response.upper()
        print("")
        match response:
            case "L":
                username = input("Enter username: ")
                password = input("Enter password: ")
                result = dbh.login(username, password)
                if result == None:
                    input("Incorrect login. Press enter to continue.")
                else:
                    uid = result[0]
                    role = result[1]
                    break
            case "C":
                username = input("Enter username: ")
                password = input("Enter password: ")
                dbh.createUser(username, password, "user")
                input("Account Created. Press enter and login.")
                logging.info("User " + username + " account created.")
            case _:
                input("Invalid Input. Press enter to continue.")

    if role == "admin":
        print("Logged in as admin.")
        logging.info("Admin " + username + " logged in.")
        while True:
            response = input("\nSelect what you would like to do.\n[AU] Add user\n[AB] Add book\n[AO] Add order\n[UU] Update user\n[UB] Update book\n[UO] Update order\n[DU] Delete user\n[DB] Delete book\n[DO] Delete order\n[SU] Show all users\n[SB] Show all books\n[SO] Show all orders\n[Q] Quit\n")
            response = response.upper()
            print("")
            match response:
                case "AU":
                    temp_username = input("Enter username: ")
                    password = input("Enter password: ")
                    role = input("Enter role: ")
                    dbh.createUser(temp_username, password, role)
                    logging.info("User " + temp_username + " added.")
                case "AB":
                    title = input("Enter title: ")
                    description = input("Enter description: ")
                    pagecount = input("Enter pagecount: ")
                    price = input("Enter price: ")
                    dbh.createBook(title, description, pagecount, price)
                    logging.info("Book " + title + " added.")
                case "AO":
                    #CONSIDER MAKING IT SO THAT THE ONLY WAYS ORDERS ARE ADDED IS THROUGH THE CUSTOMER'S MENU, NOT MANUALLY ENTERING IDS LIKE THIS
                    uid = input("Enter user id: ")
                    bid = input("Enter book id: ")
                    dbh.createOrder(uid, bid)
                    logging.info("Order between user ID " + uid + " and book ID " + bid + " added.")
                case "UU":
                    uid = input("Enter user id: ")
                    temp_username = input("Enter new username: ")
                    password = input("Enter new password: ")
                    role = input("Enter new role: ")
                    dbh.updateUser(uid, temp_username, password, role)
                    logging.info("User " + temp_username + " updated.")
                case "UB":
                    bid = input("Enter book id: ")
                    title = input("Enter new title: ")
                    description = input("Enter new description: ")
                    pagecount = input("Enter new pagecount: ")
                    price = input("Enter new price: ")
                    dbh.updateBook(bid, title, description, pagecount, price)
                    logging.info("Book " + title + " updated.")
                case "UO":
                    oid = input("Enter order id: ")
                    uid = input("Enter new user id: ")
                    bid = input("Enter new book id: ")
                    dbh.updateOrder(oid, uid, bid)
                    logging.info("Order between user ID " + uid + " and book ID " + bid + " updated.")
                case "DU":
                    uid = input("Enter user id: ")
                    dbh.deleteUser(uid)
                    logging.info("User ID " + uid + " deleted.")
                case "DB":
                    bid = input("Enter book id: ")
                    dbh.deleteBook(bid)
                    logging.info("Book ID " + bid + " deleted.")
                case "DO":
                    oid = input("Enter order id: ")
                    dbh.deleteOrder(oid)
                    logging.info("Order ID " + oid + " deleted.")
                case "SU":
                    dbh.allUsers()
                    input("\nPress enter to continue.")
                case "SB":
                    dbh.allBooks()
                    input("\nPress enter to continue.")
                case "SO":
                    dbh.allOrders()
                    input("\nPress enter to continue.")
                case "Q":
                    logging.info("Admin " + username + " logged out.")
                    break
                case _:
                    input("Invalid Input. Press enter to continue.")
    else:
        print("Logged in as user.")
        logging.info("User " + username + " logged in.")
        while True:
            response = input("\nSelect what you would like to do.\n[P] Purchase book\n[O] Order history\n[Q] Quit\n")
            response = response.upper()
            print("")
            match response:
                case "P":
                    dbh.allBooks()
                    print("")
                    bid = input("Type the bid of the book you would like.\n")
                    result = dbh.bookExists(bid)
                    if result == None:
                        input("Invalid Input. Press enter to continue.")
                    else:
                        dbh.createOrder(uid, bid)
                        input("Order Placed. Press enter to continue.")
                        logging.info("Order between user ID " + str(uid) + " and book ID " + str(bid) + " added.")
                case "O":
                    dbh.getUserOrders(uid)
                    input("\nPress enter to continue.")
                case "Q":
                    logging.info("User " + username + " logged out.")
                    break
                case _:
                    input("Invalid Input. Press enter to continue.")
        


if __name__ == '__main__':
        main()