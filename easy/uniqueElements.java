/* https://www.codeeval.com/open_challenges/29/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		
	    File file = new File(args[0]);
	    BufferedReader in = new BufferedReader(new FileReader(file));
	    String line;
	    while ((line = in.readLine()) != null) {
	        String[] lineArray = line.split(",");
	        ArrayList<String> outputArrayList = new ArrayList<String>();
	        if (lineArray.length > 0) {
	            for (String elem : lineArray) {
	            	if (!outputArrayList.contains(elem)) {
		            	outputArrayList.add(elem);
	            	}
	            }
	        }
	        System.out.println(outputArrayList.toString().replaceAll("\\s+", "").replaceAll("\\[", "").replaceAll("\\]",""));
	    }
	}
}
