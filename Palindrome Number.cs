//Solution for the Palindrome Number problem on leetCode
//Did not enjoy this one.

public class Solution {
    public bool IsPalindrome(int x) {        
        
        var number = x;          
        var reversedNumber = 0;
        var remainder = 0;
        
        while (number > 0) { // 121, 12, 1, 0
            reversedNumber *= 10; // 0, 10, 30, 40
            remainder = number % 10; // 1, 2, 1, 0
            number = (number - remainder) / 10; // 12, 1, 0, 0
            reversedNumber += remainder; // 1, 3, 4, 0
        }
        
        return x == reversedNumber;
    }
}