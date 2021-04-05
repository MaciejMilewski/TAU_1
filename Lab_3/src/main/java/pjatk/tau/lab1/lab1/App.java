/**
 * Trzecie laboratorium na przedmiocie Testowanie Automatyczne - lato 2021
 * 
 * Zadanie:
 * 1. Instalacja Maven'a
 * 2. Projekt z laboratoriów 1 dostosować do środowiska Mavenowego
 * 3. Dopisanie nowej funkcjonalności w projekcie
 * 4. Utworzenie minimum 7 nowych testów
 * 5. Dodanie dwóch nowych dependencji
 * 6. Utworzenie minimum 3 nowych testów do punktu 5.
 * 
 * Autor: Maciej Milewski 17947
 * Repozytorium: https://github.com/MaciejMilewski/TAU_1/tree/main/Lab_3
 */

package pjatk.tau.lab1.lab1;

import java.time.Instant;
import java.time.temporal.TemporalField;
import java.util.Arrays;

import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;
import org.joda.time.DateTime;
import org.joda.time.DateTimeFieldType;

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
	 * Checks if number is positive
	 *
	 * @param a number to be checked
	 * @return true if number is positive and false otherwise
	 */
	public static boolean isPositive(double x) {
		if (x >= 0) {
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
	 * Convert an array of strings into single string variable
	 *
	 * @param arr array of Strings
	 * @return string composed of elements from input array
	 */
	public static String convertArrayToString(String arr[]) {
	      StringBuffer sb = new StringBuffer();
	      String stringArray[] = arr;
	      for(int i = 0; i < stringArray.length; i++) {
	         sb.append(stringArray[i]);
	      }
	      
	      Arrays.toString(stringArray);
		return String.join("", stringArray);
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
	
	/**
	 * Gives median of double array
	 *
	 * @param arr array of doubles to analyze
	 * @return median 
	 */
	public static double median(double arr[]) {
		DescriptiveStatistics descriptiveStatistics = new DescriptiveStatistics();
		for (double v : arr) {
		    descriptiveStatistics.addValue(v);
		}

		return descriptiveStatistics.getPercentile(50);
	}
	
	/**
	 * Gets current year
	 *
	 * @return current year as integer 
	 */
	public static int currentYear() {
		DateTime dt = new DateTime();
		int year = dt.getYear();
		
		return year;
	}
}
