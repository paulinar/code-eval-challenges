/* https://www.codeeval.com/open_challenges/91/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

    public static void main(String[] args) throws IOException {
		
	    File file = new File(args[0]);
	    BufferedReader in = new BufferedReader(new FileReader(file));
	    String line;
        
	    while ((line = in.readLine()) != null) {
	        String[] lineArray = line.split(" ");
	        ArrayList<Float> outputArrayList = new ArrayList<Float>();
	        if (lineArray.length > 0) {
	            for (String elem : lineArray) {
	            	outputArrayList.add(Float.parseFloat(elem));
	            	}
	            }
	        Collections.sort(outputArrayList);
	        System.out.println(outputArrayList.toString().replaceAll("\\,", "").replaceAll("\\[", "").replaceAll("\\]",""));
	        }
	    }
}
	
