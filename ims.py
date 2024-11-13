import time

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # "Admin" or "User"

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, "
                f"Price: ${self.price}, Stock: {self.stock_quantity}")

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user": User("user", "user123", "User")
        }
        self.logged_in_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username].password == password:
            self.logged_in_user = self.users[username]
            print(f"Welcome, {self.logged_in_user.role} {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_product(self):
        if self.logged_in_user.role != "Admin":
            print("Permission denied: Only admins can add products.")
            return

        try:
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            stock_quantity = int(input("Enter stock quantity: "))

            if product_id in self.products:
                print("Product ID already exists.")
                return

            product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = product
            print(f"Product '{name}' added successfully.")
        except ValueError:
            print("Invalid input. Please enter correct data types for price and stock quantity.")

    def edit_product(self):
        if self.logged_in_user.role != "Admin":
            print("Permission denied: Only admins can edit products.")
            return

        product_id = input("Enter product ID to edit: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        try:
            name = input("Enter new product name: ")
            category = input("Enter new product category: ")
            price = float(input("Enter new product price: "))
            stock_quantity = int(input("Enter new stock quantity: "))

            product = self.products[product_id]
            product.name = name
            product.category = category
            product.price = price
            product.stock_quantity = stock_quantity
            print(f"Product '{product_id}' updated successfully.")
        except ValueError:
            print("Invalid input. Please enter correct data types for price and stock quantity.")

    def delete_product(self):
        if self.logged_in_user.role != "Admin":
            print("Permission denied: Only admins can delete products.")
            return

        product_id = input("Enter product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products.values():
            print(product)
            if product.stock_quantity < 5:
                print("Warning: Low stock. Consider restocking.")

    def search_product(self):
        search_name = input("Enter product name to search: ")
        found = False
        for product in self.products.values():
            if search_name.lower() in product.name.lower():
                print(product)
                found = True
        if not found:
            print("No matching product found.")

    def filter_by_category(self):
        category = input("Enter category to filter by: ")
        found = False
        for product in self.products.values():
            if product.category.lower() == category.lower():
                print(product)
                found = True
        if not found:
            print("No products found in this category.")

    def adjust_stock(self):
        if self.logged_in_user.role != "Admin":
            print("Permission denied: Only admins can adjust stock.")
            return

        product_id = input("Enter product ID to adjust stock: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        try:
            adjustment = int(input("Enter stock adjustment (positive to add, negative to reduce): "))
            product = self.products[product_id]
            product.stock_quantity += adjustment
            print(f"Product '{product_id}' stock adjusted successfully. New stock: {product.stock_quantity}")
        except ValueError:
            print("Invalid input. Please enter an integer for stock adjustment.")

    def logout(self):
        print("Logging out...")
        time.sleep(1)
        print("Logged out successfully")
        print()
        self.logged_in_user = None

    def run(self):
        print("**************************************************************************")
        print("        *      Welcome to the Inventory Management System      *          ")
        print("**************************************************************************")
        print()
        running = True
        while running:
            if not self.logged_in_user:
                if not self.login():
                    continue

            print("\nMenu:")
            print("1. View Products")
            print("2. Search Product")
            print("3. Filter by Category")
            if self.logged_in_user.role == "Admin":
                print("4. Add Product")
                print("5. Edit Product")
                print("6. Delete Product")
                print("7. Adjust Stock")
            print("0. Logout")
            print("Press x to exit program")

            choice = input("Enter your choice: ")

            if choice == "x":
                print("Shutting Down System...")
                time.sleep(1.5)
                print("System Shut Down Successfully!")
                print()
                running = False
            elif choice == "1":
                self.view_products()
            elif choice == "2":
                self.search_product()
            elif choice == "3":
                self.filter_by_category()
            elif choice == "4" and self.logged_in_user.role == "Admin":
                self.add_product()
            elif choice == "5" and self.logged_in_user.role == "Admin":
                self.edit_product()
            elif choice == "6" and self.logged_in_user.role == "Admin":
                self.delete_product()
            elif choice == "7" and self.logged_in_user.role == "Admin":
                self.adjust_stock()
            elif choice == "0":
                self.logout()
            else:
                print("Invalid choice. Please try again.")
            
ims = InventoryManagementSystem()
ims.run()
