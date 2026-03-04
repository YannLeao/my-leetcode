#include <vector>

class Bank {
private:
    std::vector<long long> balance;

public:
    explicit Bank(std::vector<long long>& balance) : balance(balance) {}

    bool transfer(int account1, int account2, long long money) {
        int i1 = account1 - 1;
        int i2 = account2 - 1;

        if (i1 < 0 || i1 >= balance.size() ||
            i2 < 0 || i2 >= balance.size())
            return false;

        if (balance[i1] < money)
            return false;

        balance[i1] -= money;
        balance[i2] += money;
        return true;
    }

    bool deposit(int account, long long money) {
        int i = account - 1;

        if (i < 0 || i >= balance.size())
            return false;

        balance[i] += money;
        return true;
    }

    bool withdraw(int account, long long money) {
        int i = account - 1;

        if (i < 0 || i >= balance.size())
            return false;

        if (balance[i] < money)
            return false;

        balance[i] -= money;
        return true;
    }
};
