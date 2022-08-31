// Longest prefix solution. Fast, but not great on memory.

public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        Array.Sort(strs, (x, y) => x.Length.CompareTo(y.Length));
        
        var testStr = strs[0];
        
        if (strs[0].Length > 0 && strs.Length > 1) {
                       
            for (int i = strs[0].Length; i > -1; i--) {                
                testStr = strs[0].Substring(0, i);
                var match = true;

                for (int n = 1; n < strs.Length; n++) {
                    if (testStr != strs[n].Substring(0, i)) {
                        match = false;
                    }                
                }
                
                if (match) {
                    break;
                }
            }
        }
        
        return testStr;
    }
}