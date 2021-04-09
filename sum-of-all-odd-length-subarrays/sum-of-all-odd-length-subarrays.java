class Solution {
    public int sumOddLengthSubarrays(int[] a) {
            int sum = 0;
            int group = 3;

            for (int i = 0; i < a.length; i++) {
                sum += a[i];
            }

            while (group <= a.length) {
                for (int i = 0; i < a.length; i++) {
                    for (int j = i; i + group <= a.length && j < i + group && j < a.length; j++) {
                        sum += a[j];
                    }
                }
                group += 2;
            }

            return sum;
        }
}