/* https://www.codeeval.com/open_challenges/18/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
	    File file = new File(args[0]);
	    BufferedReader in = new BufferedReader(new FileReader(file));
	    String line;
	    while ((line = in.readLine()) != null) {
	    	String[] lineArray = line.split(",");
	        int x = Integer.parseInt(lineArray[0]);
	        int n = Integer.parseInt(lineArray[1]);
            if (x == n) {
                System.out.println(n);
            } else while (n < x && x != n) {
	            	n *= 2;
	            }
	        System.out.println(n);
	        }
	    }
	}