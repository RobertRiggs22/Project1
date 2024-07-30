from pymongo import MongoClient
import json

class databaseHandler:

    def __init__(self):
            #Connect to server
            client = MongoClient("localhost", 27017)
            self.db = client.get_database("bookstore")

            #gets the next user id to be given out
            maxUID = self.db.users.find_one(sort=[("uid", -1)])
            if maxUID == None:
                self.userID = 1
            else:
                self.userID = maxUID["uid"] + 1
            #gets the next book id to be given out
            maxBID = self.db.books.find_one(sort=[("bid", -1)])
            if maxBID == None:
                self.bookID = 1
            else:
                self.bookID = maxBID["bid"] + 1
            #gets the next order id to be given out
            maxOID = self.db.orders.find_one(sort=[("oid", -1)])
            if maxOID == None:
                self.orderID = 1
            else:
                self.orderID = maxOID["oid"] + 1

    def createUser(self, username, password, role):
        new_user = {"uid": self.userID, "username": username, "password": password, "role": role}
        self.db.users.insert_one(new_user)
        self.userID = self.userID + 1

    def createBook(self, title, description, pagecount, price):
        new_book = {"bid": self.bookID, "title": title, "description": description, "pagecount": pagecount, "price": price}
        self.db.books.insert_one(new_book)
        self.bookID = self.bookID + 1

    def createOrder(self, uid, bid):
        new_order = {"oid": self.orderID, "uid": uid, "bid": bid}
        self.db.orders.insert_one(new_order)
        self.orderID = self.orderID + 1

    def allUsers(self):
        users = self.db.users.find({})
        for user in users:
            print(user)

    def allBooks(self):
        books = self.db.books.find({})
        for book in books:
            print(book)

    def allBookspretty(self):
        books = self.db.books.find({})
        for book in books:
            print("ID: " + str(book["bid"]) + "\tTitle: " + book["title"] + "\tDescription: " + book["description"] + "\tPage count: " + str(book["pagecount"]) + "\tPrice: " + str(book["price"]))

    def allOrders(self):
        orders = self.db.orders.find({})
        for order in orders:
            print(order)

    def updateUser(self, uid, username, password, role):
        try:
            user_to_update = {"uid": int(uid)}
            updated_user = {"$set": {"username": username, "password": password, "role": role}}
            self.db.users.update_one(user_to_update, updated_user)
        except:
            input("Invalid Input. Press enter to continue.")

    def updateBook(self, bid, title, description, pagecount, price):
        try:
            book_to_update = {"bid": int(bid)}
            updated_book = {"$set": {"title": title, "description": description, "pagecount": pagecount, "price": price}}
            self.db.books.update_one(book_to_update, updated_book)
        except:
            input("Invalid Input. Press enter to continue.")

    def updateOrder(self, oid, uid, bid):
        try:
            order_to_update = {"oid": int(oid)}
            updated_order = {"$set": {"uid": uid, "bid": bid}}
            self.db.orders.update_one(order_to_update, updated_order)
        except:
            input("Invalid Input. Press enter to continue.")

    def deleteUser(self, uid):
        try:
            user_to_delete = {"uid": int(uid)}
            self.db.users.delete_one(user_to_delete)
        except:
            input("Invalid Input. Press enter to continue.")

    def deleteBook(self, bid):
        try:
            book_to_delete = {"bid": int(bid)}
            self.db.books.delete_one(book_to_delete)
        except:
            input("Invalid Input. Press enter to continue.")

    def deleteOrder(self, oid):
        try:
            order_to_delete = {"oid": int(oid)}
            self.db.orders.delete_one(order_to_delete)
        except:
            input("Invalid Input. Press enter to continue.")

    def login(self, username, password):
        user = self.db.users.find_one({"username": username, "password": password})
        if user == None:
            return None
        else:
            return (user["uid"], user["role"])
        
    def bookExists(self, bid):
        try:
            result = self.db.books.find_one({"bid": int(bid)})
            return result
        except:
            pass

    def getUserOrders(self, uid):
        try:
            user_orders = self.db.orders.find({"uid": int(uid)})
            test = user_orders[0]
            for order in user_orders:
                print(order)
        except:
            print("No order history found.")

    def getUserOrderspretty(self, uid):
        try:
            user_orders = self.db.orders.find({"uid": int(uid)})
            test = user_orders[0]
            print("Books ordered:")
            for order in user_orders:
                ordered_books = self.db.books.find({"bid": int(order["bid"])})
                test = ordered_books[0]
                for book in ordered_books:
                    print(book["title"])
        except:
            print("No order history found.")