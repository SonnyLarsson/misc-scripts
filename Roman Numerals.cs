//Solution for the Roman Numerals problem on leetCode.
//Not elegant, but pretty fast. Eats too much memory though.

public class Solution {
    public int RomanToInt(string s) {
        
        int total = 0;
        
        if (s.Contains("CM")) {
            total += 900;
            s = s.Replace("CM", "");
        }
        
        if (s.Contains("M")) {
            var mCount = s.Count(x => (x == 'M'));
            total += 1000 * mCount;
            s = s.Replace("M", "");
        }
        
        if (s.Contains("CD")) {
            total += 400;
            s = s.Replace("CD", "");
        }
        
        if (s.Contains("D")) {
            var dCount = s.Count(x => (x == 'D'));
            total += 500 * dCount;
            s = s.Replace("D", "");
        }
        
        if (s.Contains("XC")) {
            total += 90;
            s = s.Replace("XC", "");
        }
        
        if (s.Contains("C")) {
            var cCount = s.Count(x => (x == 'C'));
            total += 100 * cCount;
            s = s.Replace("C", "");
        }
               
        if (s.Contains("XL")) {
            total += 40;
            s = s.Replace("XL", "");
        }
        
        if (s.Contains("L")) {
            var lCount = s.Count(x => (x == 'L'));
            total += 50 * lCount;
            s = s.Replace("L", "");
        }
        
        if (s.Contains("IX")) {
            total += 9;
            s = s.Replace("IX", "");
        }
        
        if (s.Contains("X")) {
            var xCount = s.Count(x => (x == 'X'));
            total += 10 * xCount;
            s = s.Replace("X", "");
        }
        
        if (s.Contains("IV")) {
            total += 4;
            s = s.Replace("IV", "");
        }
        
        if (s.Contains("V")) {
            total += 5;
            s = s.Replace("V", "");
        }
        
        total += s.ToCharArray().Length;         
        
        return total;        
    }
}