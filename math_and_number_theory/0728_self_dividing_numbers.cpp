#include <vector>

class Solution {
public:
    static std::vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> output;

        for (int number = left; number <= right; number++)
        {
            if (isSelfDividing(number)) output.push_back(number);
        }

        return output;
    }
private:
    static bool isSelfDividing(int n) {
        int original = n;
        while(n > 0)
        {
            int digit = n % 10;
            if (digit == 0 || original % digit != 0) return false;
            n /= 10;
        }
        return true;
    }
};
