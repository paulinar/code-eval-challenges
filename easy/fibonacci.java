/* https://www.codeeval.com/open_challenges/22/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static int fib(int n) {
		if (n <= 0) {
			return 0;
		} else if (n == 1 || n == 2) {
			return 1;
		} else {
			return fib(n-1) + fib(n-2);
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {

	    File file = new File(args[0]);
	    BufferedReader in = new BufferedReader(new FileReader(file));
	    String line;
	    
	    while ((line = in.readLine()) != null) {
	        System.out.println(fib(Integer.parseInt(line)));
	        }
		
	}

}
