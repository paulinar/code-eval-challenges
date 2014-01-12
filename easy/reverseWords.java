/* https://www.codeeval.com/open_challenges/8/ */

package reverseWords;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    
    public static void main (String[] args) throws IOException {

	    File file = new File(args[0]);
	    BufferedReader in = new BufferedReader(new FileReader(file));
        String line;
	    
	    String reversed = ""; 
	    
	    while ((line = in.readLine()) != null) {
	    	for (int i = line.length() - 1; i >= 0; i--){
	    	    reversed += line.charAt(i);
	        }
	    }
	    System.out.println(reversed);
  }
}