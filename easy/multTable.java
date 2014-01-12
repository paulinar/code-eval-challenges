package multTable;

/* https://www.codeeval.com/open_challenges/23/ */

public class Main {

	public static void main(String[] args) {
		
		for (int i = 1; i <= 12; i++) {          // column 
			for (int j = 1; j <= 12; j++) {      // row
				System.out.printf("%4d", j * i); 
				// %4d means to right-align and take up 4 spaces
				// use printf because writing a formatted string to an output stream using specified format string and arguments 
			}
			System.out.println(); // go to next row of multiplication table
		}
	}
}