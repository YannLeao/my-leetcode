class Solution {
public:
    static int pivotInteger(int n) {
        int leftValue = 1, rightValue = n;
        int leftSum = 1, rightSum = n;

        if (n == 1) return n;

        while (leftValue < rightValue)
        {
            if (leftSum < rightSum)
            {
                leftValue++;
                leftSum += leftValue;
            }
            else
            {
                rightValue--;
                rightSum += rightValue;
            }

            if (leftSum == rightSum && leftValue+1 == rightValue-1) return rightValue-1;
        }

        return -1;
    }
};