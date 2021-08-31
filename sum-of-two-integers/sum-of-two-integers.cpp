class Solution {
public:
    int getSum(int a, int b) {
        int sum, carry;
        while (b) {
            sum = a^b;
            carry = (unsigned int)(a&b) << 1;
            a = sum;
            b = carry;
        }
        return a;
    }
};