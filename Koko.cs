// This is a solution to the Koko Eating bananas problem on LeetCode.

public class Solution {  
    
    public int MinEatingSpeed(int[] piles, int h) {    
        
        Array.Sort(piles, 0, piles.Length); //For some reason I'm getting ooindex-errors on single-index arrays without this.
        
        int lastPos = piles.Length-1;        
        
        if (piles.Length == h) {return piles[lastPos];};
        
        long kokosMaximumBananaSpeed = 0; //Has to be long because of large number testcases
        
        int top = piles[lastPos];
        int middle;
        int bottom = 1;
                        
        while(bottom <= top) {
            
            middle = bottom + (top - bottom)/2;            
            kokosMaximumBananaSpeed = calculator(piles, middle, h);

            if(kokosMaximumBananaSpeed > h) {
                
                bottom = middle + 1;
                
            } else {
            
                top = middle - 1;
            
            }
        }
               
        return bottom;
    }
    
    private long calculator(int[] piles, int middlePos, int h) {
        
        int dividedPiles = 0;
        
        foreach (int pile in piles) {
            
            int remainder = 0;
            dividedPiles += pile/middlePos;
            
            if (pile > middlePos && pile % middlePos > 0) {
            
                dividedPiles += 1;
            
            }             
            
            if (pile<middlePos) {
            
                dividedPiles +=1;
            
            }
            
        }
        
        return dividedPiles;
    }
}