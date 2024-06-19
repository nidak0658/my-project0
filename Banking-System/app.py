class Customer {
private:
    int customerId;
    string name;
    string address;
    string contactNumber;
    // Other attributes as needed

public:
    Customer(int id, const string& n, const string& addr, const string& contact)
        : customerId(id), name(n), address(addr), contactNumber(contact) {}

    // Getters
    int getCustomerId() const { return customerId; }
    string getName() const { return name; }
    string getAddress() const { return address; }
    string getContactNumber() const { return contactNumber; }
};

class Account {
private:
    int accountNumber;
    string accountType;
    double balance;
    Customer owner;
    // Other attributes as needed

public:
    Account(int accNum, const string& type, double initialBalance, const Customer& cust)
        : accountNumber(accNum), accountType(type), balance(initialBalance), owner(cust) {}

    // Methods
    void deposit(double amount) {
        balance += amount;
    }

    bool withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }

    bool transfer(Account& toAccount, double amount) {
        if (withdraw(amount)) {
            toAccount.deposit(amount);
            return true;
        }
        return false;
    }

    // Getters
    int getAccountNumber() const { return accountNumber; }
    string getAccountType() const { return accountType; }
    double getBalance() const { return balance; }
    const Customer& getOwner() const { return owner; }
};

class Transaction {
private:
    int transactionId;
    string transactionType;
    double amount;
    int accountNumber;
    // Other attributes as needed

public:
    Transaction(int id, const string& type, double amt, int accNum)
        : transactionId(id), transactionType(type), amount(amt), accountNumber(accNum) {}

    // Getters
    int getTransactionId() const { return transactionId; }
    string getTransactionType() const { return transactionType; }
    double getAmount() const { return amount; }
    int getAccountNumber() const { return accountNumber; }
};

class BankingServices {
private:
    vector<Customer> customers;
    vector<Account> accounts;
    vector<Transaction> transactions;
    int nextCustomerId;
    int nextAccountNumber;
    int nextTransactionId;
    // Other attributes as needed

public:
    BankingServices() : nextCustomerId(1), nextAccountNumber(1), nextTransactionId(1) {}

    // Methods for customer management
    void addCustomer(const string& name, const string& addr, const string& contact) {
        Customer newCustomer(nextCustomerId++, name, addr, contact);
        customers.push_back(newCustomer);
    }

    Customer* findCustomerById(int id) {
        for (auto& cust : customers) {
            if (cust.getCustomerId() == id) {
                return &cust;
            }
        }
        return nullptr;  // Customer not found
    }

    // Methods for account management
    void openAccount(const Customer& cust, const string& type, double initialBalance) {
        Account newAccount(nextAccountNumber++, type, initialBalance, cust);
        accounts.push_back(newAccount);
    }

    Account* findAccountByNumber(int accNum) {
        for (auto& acc : accounts) {
            if (acc.getAccountNumber() == accNum) {
                return &acc;
            }
        }
        return nullptr;  // Account not found
    }

    // Methods for transactions
    void recordTransaction(const string& type, double amount, int accNum) {
        Transaction newTransaction(nextTransactionId++, type, amount, accNum);
        transactions.push_back(newTransaction);
    }

    // Banking operations
    bool deposit(int accNum, double amount) {
        Account* acc = findAccountByNumber(accNum);
        if (acc) {
            acc->deposit(amount);
            recordTransaction("Deposit", amount, accNum);
            return true;
        }
        return false;  // Account not found
    }

    bool withdraw(int accNum, double amount) {
        Account* acc = findAccountByNumber(accNum);
        if (acc && acc->withdraw(amount)) {
            recordTransaction("Withdrawal", amount, accNum);
            return true;
        }
        return false;  // Account not found or insufficient balance
    }

    bool transfer(int fromAccNum, int toAccNum, double amount) {
        Account* fromAcc = findAccountByNumber(fromAccNum);
        Account* toAcc = findAccountByNumber(toAccNum);
        if (fromAcc && toAcc && fromAcc->transfer(*toAcc, amount)) {
            recordTransaction("Transfer", amount, fromAccNum);
            recordTransaction("Transfer", amount, toAccNum);
            return true;
        }
        return false;  // Either account not found or insufficient balance in 'from' account
    }

    // Methods for account information and transaction history
    void printAccountInfo(int accNum) {
        Account* acc = findAccountByNumber(accNum);
        if (acc) {
            cout << "Account Number: " << acc->getAccountNumber() << endl;
            cout << "Account Type: " << acc->getAccountType() << endl;
            cout << "Balance: $" << acc->getBalance() << endl;
            cout << "Owner: " << acc->getOwner().getName() << endl;
            // Additional account details as needed
        } else {
            cout << "Account not found." << endl;
        }
    }

    void printTransactionHistory(int accNum) {
        cout << "Transaction History for Account " << accNum << ":" << endl;
        for (auto& trans : transactions) {
            if (trans.getAccountNumber() == accNum) {
                cout << "Transaction ID: " << trans.getTransactionId() << endl;
                cout << "Type: " << trans.getTransactionType() << endl;
                cout << "Amount: $" << trans.getAmount() << endl;
                // Additional transaction details as needed
                cout << "--------------------------" << endl;
            }
        }
    }
};

int main() {
    // Create banking services instance
    BankingServices bank;

    // Add customers
    bank.addCustomer("John Doe", "123 Main St", "555-1234");
    bank.addCustomer("Jane Smith", "456 Elm St", "555-5678");

    // Open accounts
    Customer* john = bank.findCustomerById(1);
    Customer* jane = bank.findCustomerById(2);

    bank.openAccount(*john, "Savings", 1000.0);
    bank.openAccount(*john, "Checking", 500.0);
    bank.openAccount(*jane, "Savings", 1500.0);

    // Perform transactions
    bank.deposit(1, 500.0);
    bank.withdraw(1, 200.0);
    bank.transfer(1, 2, 300.0);

    // Print account information and transaction history
    bank.printAccountInfo(1);
    bank.printTransactionHistory(1);

    return 0;
}
