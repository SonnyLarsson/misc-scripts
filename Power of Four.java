//Solutions for the Power of Four problem on leetCode

//This solves the problem without using a loop.
//I had to google some math to get to here.
class SolutionMath {
    public boolean isPowerOfFour(int n) {
        if (n == 0) return false;
        if (n == 1) return true;
        if (n % 2 != 0) return false;
        if (n % 10 == 0) return false;
        
        double x = Math.log(n)/Math.log(4); 
        return x % 1 == 0;
    }
}

//This solves the problem without using a loop.
//This was my initial, very quick solution. 
class SolutionLoop {
    public boolean isPowerOfFour(int n) {
        if (n == 0) return false;
        if (n == 1) return true;
        if (n % 2 != 0) return false;
        if (n % 10 == 0) return false;
        
        //if ((n > 16 || n * -1 > 16) && n % 16 != 0) return false;
        //if ((n > 64) && n % 64 != 0) return false;
        //if ((n > 256 || n * -1 > 256) && n % 256 != 0) return false;
        //if ((n > 1024) && n % 1024 != 0) return false;
        
        // n == 4^x, if x exists
        // 1 == 4^0 -> 1 == 1^0.25
        // 4 == 4^1
        // 16 == 4^2
        // 64 == 4^3
        // 256 == 4^4
        // 1024 == 4^5
        
        double o = (double)n;
        
        while (o > 15 || o < -15) {
            o /= 4;
        }
        
        if (o != 4) return false;   
        
        return true;
    }
}

//Note that both solutions are faster than "100%" of java solutions on leetCode, but that memory usage is middling.
//Both the speed and memory usage stems from my checks before the main event. I kept them because I prefer being the fastest over being better than 80% or so on memory.