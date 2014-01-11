/* https://www.codeeval.com/open_challenges/25/ */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
		BufferedReader in = new BufferedReader(new FileReader(file));
		String line;
		
		HashMap<String, String> conversions = new HashMap<String, String>();
		conversions.put("zero", new String("0"));
		conversions.put("one", new String("1"));
		conversions.put("two", new String("2"));
		conversions.put("three", new String("3"));
		conversions.put("four", new String("4"));
		conversions.put("five", new String("5"));
		conversions.put("six", new String("6"));
		conversions.put("seven", new String("7"));
		conversions.put("eight", new String("8"));
		conversions.put("nine", new String("9"));
		
		while ((line = in.readLine()) != null) {
			
			List<String> toOutput = new ArrayList<String>(20);
			
			String[] lineArray = line.split(";");
			
			if (lineArray.length > 0) {
				for(int i=0; i < lineArray.length; i++) {
					toOutput.add(conversions.get(lineArray[i]));
				}
		    }
            
            StringBuilder builder = new StringBuilder();
		    for (String elem : toOutput) {
			    builder.append(elem);
		    }
		    String finalOutput = builder.toString();
		    System.out.println(finalOutput);
		}
	}

}

