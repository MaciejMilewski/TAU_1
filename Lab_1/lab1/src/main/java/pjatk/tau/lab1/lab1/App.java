/**
 * Pierwsze laboratorium na przedmiocie Testowanie Automatyczne - lato 2021
 * 
 * Zadanie:
 * 1. Utworzenie struktury katalogów i dodanie tam swojego projektu lub jego części.
 * 2. Wejść na stronę http://junit.sourceforge.net/javadoc/org/junit/Assert.html i wybrać 3 różne assercje, następnie napisać z nimi testy (~10).
 * 3. Zaimplementować wyjątek w swoim projekcie.
 * 
 * Autor: Maciej Milewski 17947
 * Repozytorium: https://github.com/MaciejMilewski/TAU_1/tree/main/Lab_1
 */

package pjatk.tau.lab1.lab1;

/*
 * Main class contains several simple mathematical functions which will be later tested using JUnit
 */
public class App {

	/**
	 * Returns a sum of two double variables
	 *
	 * @param a first number
	 * @param b second number
	 * @return sum of a and b
	 */
	public static double sum(double a, double b) {
		return a + b;
	}

	/**
	 * Returns a subtraction of two double variables
	 *
	 * @param a first number
	 * @param b second number
	 * @return subtraction of a and b
	 */
	public static double subtraction(double a, double b) {
		return a - b;
	}

	/**
	 * Returns a multiplication of two double variables
	 *
	 * @param a first number
	 * @param b second number
	 * @return multiplication of a and b
	 */
	public static double multiplication(double a, double b) {
		return a * b;
	}

	/**
	 * Returns a division of two double variables
	 *
	 * @param a number to be divided
	 * @param b divider
	 * @return division of a and b
	 */
	public static double divide(double a, double b) {
		if (b == 0) {
			throw new IllegalArgumentException("You cant't divide by 0");
		}
		return a / b;
	}

	/**
	 * Checks if number is negative
	 *
	 * @param a number to be checked
	 * @return true if number is negative and false otherwise
	 */
	public static boolean isNegative(double x) {
		if (x < 0) {
			return true;
		} else {
			return false;
		}
	}
	
	/**
	 * Convert a String variable to Array of Characters
	 *
	 * @param str String to be converted
	 * @return Array of characters from String
	 */
	public static char[] convertStringToArray(String str) {
        char[] charactersArray = new char[str.length()]; 
  
        for (int i = 0; i < str.length(); i++) { 
            charactersArray[i] = str.charAt(i); 
        } 
  
        return charactersArray;
	}
	
	/**
	 * Calculates perimeter of triangle
	 *
	 * @param a first side of triangle
	 * @param b second side of triangle
	 * @param c third side of triangle
	 * @return triangle perimeter
	 * @throws Exception 
	 */
	public static double trianglePerimeter(double a, double b, double c) throws Exception {
		if (a + b <= c || a + c <= b || b + c <= a) {
			throw new Exception("It's not triangle");
		}
		return a + b + c;
	}
}
