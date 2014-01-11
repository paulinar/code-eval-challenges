/* https://www.codeeval.com/open_challenges/3/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static boolean isPrime(int n) {
		if (n <= 1) {
			return false;
		} else {
			for (int i = 2; i < Math.sqrt(n); i++) {
				if (n%i == 0) {
					return false;
				}
			}
			
 		}
		return true;
	}
	
	public static void main(String[] args) {
				
        int largestSoFar = 0;
		for (int i = 2; i <= 1000; i++) {
			if (isPrime(i)) {
				String reversedNum = new StringBuffer(Integer.toString(i)).reverse().toString();
				if (Integer.parseInt(reversedNum) == i) {
					largestSoFar = i;
				}
			}
		}
		System.out.println(largestSoFar);			
	}
}
