#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>

using namespace std;

const int MAX_BOOKS = 100; // Maximum number of books
const int MAX_ORDERS = 100; // Maximum number of orders
const int MAX_USERS = 1; // Maximum number of users

// Structure to store book information
struct Book {
    string title;
    string author;
    double price;
};

// Structure to store order information
struct Order {
    string customerName;
    Book books[MAX_BOOKS];
    double discount;
};

// Structure to store user information
struct User {
    string username;
    string password;
};

// Function prototypes
void displayMenu();
bool loginUser(User users[], string& loggedInUser);
void manageBooks(Book books[]);
void manageOrders(Order orders[], const Book books[]);
void printQuotation(const Order& order);

int main() {
    // User login credentials
    User users[MAX_USERS] = {{"user", "user123"}};

    // Sample books and orders
    Book books[MAX_BOOKS];
    Order orders[MAX_ORDERS];

    int choice;
    string loggedInUser;

    do {
        // Display the menu only if a user is logged in
        if (!loggedInUser.empty()) {
            displayMenu();
            cout << "Enter your choice: ";
            cin >> choice;

            switch (choice) {
                case 1:
                    manageBooks(books);
                    break;
                case 2:
                    manageOrders(orders, books);
                    break;
                case 3:
                    // Logout option
                    loggedInUser.clear();
                    cout << "Logged out successfully.\n";
                    break;
                default:
                    cout << "Invalid choice. Please try again.\n";
            }
        } else {
            // If no user is logged in, prompt for login
            if (loginUser(users, loggedInUser)) {
                cout << "Login successful. Welcome, " << loggedInUser << "!\n";
            } else {
                cout << "Login failed. Please try again.\n";
            }
        }
    } while (choice != 3);

    return 0;
}

// Function to display the main menu
void displayMenu() {
    cout << "\n--- Nethra Book Shop ---\n";
    cout << "1. Manage Books\n";
    cout << "2. Manage Orders\n";
    cout << "3. Logout\n";
}

// Function to handle user login
bool loginUser(User users[], string& loggedInUser) {
    string username, password;

    cout << "\n--- User Login ---\n";
    cout << "Username: ";
    cin >> username;
    cout << "Password: ";
    cin >> password;

    for (int i = 0; i < MAX_USERS; ++i) {
        if (users[i].username == username && users[i].password == password) {
            loggedInUser = username;
            return true;
        }
    }

    return false;
}

// Function to manage books
void manageBooks(Book books[]) {
    int choice;

    do {
        cout << "\n--- Manage Books ---\n";
        cout << "1. View Books\n";
        cout << "2. Add Book\n";
        cout << "3. Search Books\n";
        cout << "4. Back to Main Menu\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                {
                    bool isEmpty = true;
                    for (int i = 0; i < MAX_BOOKS; ++i) {
                        if (!books[i].title.empty()) {
                            cout << "Title: " << books[i].title << "\tAuthor: " << books[i].author << "\tPrice: $" << fixed << setprecision(2) << books[i].price << endl;
                            isEmpty = false;
                        }
                    }

                    if (isEmpty) {
                        cout << "No books available.\n";
                    }
                }
                break;
            case 2:
                {
                    for (int i = 0; i < MAX_BOOKS; ++i) {
                        if (books[i].title.empty()) {
                            cout << "\nEnter Book Details:\n";
                            cout << "Title: ";
                            cin.ignore();
                            getline(cin, books[i].title);
                            cout << "Author: ";
                            getline(cin, books[i].author);
                            cout << "Price: $";
                            cin >> books[i].price;

                            cout << "Book added successfully.\n";
                            break;
                        }
                    }
                }
                break;
            case 3:
                {
                    string searchTitle;
                    cout << "Enter book title to search: ";
                    cin.ignore();
                    getline(cin, searchTitle);

                    bool found = false;
                    for (int i = 0; i < MAX_BOOKS; ++i) {
                        if (!books[i].title.empty() && books[i].title.find(searchTitle) != string::npos) {
                            cout << "Title: " << books[i].title << "\tAuthor: " << books[i].author << "\tPrice: $" << fixed << setprecision(2) << books[i].price << endl;
                            found = true;
                        }
                    }

                    if (!found) {
                        cout << "Book not found. Please try a different title.\n";
                    }
                }
                break;
            case 4:
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);
}

// Function to manage orders
void manageOrders(Order orders[], const Book books[]) {
    int choice;

    do {
        cout << "\n--- Manage Orders ---\n";
        cout << "1. View Book Orders\n";
        cout << "2. Prepare Quotations\n";
        cout << "3. Add Discounts\n";
        cout << "4. Back to Main Menu\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                {
                    bool isEmpty = true;
                    for (int i = 0; i < MAX_ORDERS; ++i) {
                        if (!orders[i].customerName.empty()) {
                            cout << "Customer: " << orders[i].customerName << "\tBooks: " << sizeof(orders[i].books) / sizeof(orders[i].books[0]) << "\tDiscount: $" << fixed << setprecision(2) << orders[i].discount << endl;
                            isEmpty = false;
                        }
                    }

                    if (isEmpty) {
                        cout << "No orders available.\n";
                    }
                }
                break;
            case 2:
                {
                    for (int i = 0; i < MAX_ORDERS; ++i) {
                        if (orders[i].customerName.empty()) {
                            cout << "\nEnter Order Details:\n";
                            cout << "Customer Name: ";
                            cin.ignore();
                            getline(cin, orders[i].customerName);

                            int numBooks;
                            cout << "Enter the number of books in the order: ";
                            cin >> numBooks;

                            for (int j = 0; j < numBooks; ++j) {
                                string bookTitle;
                                cout << "Enter book title #" << j + 1 << ": ";
                                cin.ignore();
                                getline(cin, bookTitle);

                                for (int k = 0; k < MAX_BOOKS; ++k) {
                                    if (!books[k].title.empty() && books[k].title == bookTitle) {
                                        orders[i].books[j] = books[k];
                                        break;
                                    }
                                }
                            }

                            cout << "Order placed successfully.\n";
                            break;
                        }
                    }
                }
                break;
            case 3:
                {
                    string customerName;
                    cout << "Enter customer name to apply discount: ";
                    cin.ignore();
                    getline(cin, customerName);

                    for (int i = 0; i < MAX_ORDERS; ++i) {
                        if (!orders[i].customerName.empty() && orders[i].customerName == customerName) {
                            double discount;
                            cout << "Enter discount amount: $";
                            cin >> discount;

                            orders[i].discount = discount;
                            cout << "Discount applied successfully.\n";
                            break;
                        }
                    }
                }
                break;
            case 4:
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);
}

// Function to print a quotation with discounts
void printQuotation(const Order& order) {
    if (order.customerName.empty()) {
        cout << "No customer name in the order.\n";
        return;
    }

    double total = 0.0;

    cout << "\n--- Quotation ---\n";
    cout << "Customer: " << order.customerName << "\n";
    cout << "Books:\n";

    for (const Book& book : order.books) {
        if (!book.title.empty()) {
            cout << "Title: " << book.title << "\tAuthor: " << book.author << "\tPrice: $" << fixed << setprecision(2) << book.price << endl;
            total += book.price;
        }
    }

    cout << "Discount: $" << fixed << setprecision(2) << order.discount << "\n";
    cout << "Total Price: $" << fixed << setprecision(2) << (total - order.discount) << "\n";
}
