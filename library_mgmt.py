from collections import deque

class Library:
    def __init__(self):
        self.catalog = {} 
        self.members = {} 

        self.order_queue = deque()  
        
    def add_book(self, id, name, authors, count):
        self.catalog[id] = {
            "name": name, 
            "authors": authors,
            "count": count
        }
        
    def add_member(self, id, name):
        self.members[id] = name
        
    def request_book(self, member_id, book_id):
        print(f"{self.members[member_id]} requested book {self.catalog[book_id]['name']}")
        self.order_queue.append((member_id, book_id)) 
        
    def process_orders(self):
        while self.order_queue:
            member_id, book_id = self.order_queue.popleft()
            book = self.catalog[book_id]
            
            if book["count"] > 0:
                print(f"Providing book {book['name']} to member {member_id}")
                book["count"] -= 1  
            else:
                print(f"Book {book['name']} is currently out of stock") 
                self.order_queue.append((member_id, book_id))
                

library = Library()

library.request_book(1, 10) 
library.request_book(2, 12)
library.process_orders()