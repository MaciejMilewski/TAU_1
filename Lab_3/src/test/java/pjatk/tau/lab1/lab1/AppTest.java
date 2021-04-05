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

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.*;

import org.junit.Test;

/**
 * Over 10 unit tests for function using 3 different assert methods
 */
public class AppTest {

	/**
	 * Sum correctly two numbers.
	 * 
	 * @result Two number of double type will be added correctly
	 */
	@Test
	public void sum_correctInput_correctResult() {
		double result = App.sum(34.3, 26.2);
		assertEquals(60.5, result, 0);
	}
	
	/**
	 * Sum incorrectly two numbers.
	 * 
	 * @result Two number of double type will be added incorrectly
	 */
	@Test
	public void sum_correctInput_incorrectResult() {
		double result = App.sum(34.3, 26.2);
		assertNotEquals(64.5, result, 0);
	}

	/**
	 * Subtract correctly two numbers.
	 * 
	 * @result Subtract second number from first number of double type correctly
	 */
	@Test
	public void subtraction_correctInput_correctResult() {
		double result = App.subtraction(111.7, 11.7);
		assertEquals(100, result, 0);
	}
	
	/**
	 * Subtract incorrectly two numbers.
	 * 
	 * @result Subtract second number from first number of double type incorrectly
	 */
	@Test
	public void subtraction_correctInput_incorrectResult() {
		double result = App.subtraction(111.7, 11.7);
		assertNotEquals(1001, result, 0);
	}

	/**
	 * Multiply correctly two numbers.
	 * 
	 * @result Multiply 2 numbers of double type correctly
	 */
	@Test
	public void multiplication_correctInput_correctResult() {
		double result = App.multiplication(10.0, 3.0);
		assertEquals(30, result, 0);
	}
	
	/**
	 * Multiply incorrectly two numbers.
	 * 
	 * @result Multiply 2 numbers of double type incorrectly
	 */
	@Test
	public void multiplication_correctInput_incorrectResult() {
		double result = App.multiplication(10.0, 3.0);
		assertNotEquals(38, result, 0);
	}

	/**
	 * Divide correctly two numbers.
	 * 
	 * @result Divide first number by second number of double types correctly
	 */
	@Test
	public void divide_correctInput_correctResult() {
		double result = App.divide(21.0, 3.0);
		assertEquals(7, result, 0);
	}

	/**
	 * Divide by 0.
	 * 
	 * @result exception should be thrown
	 */
	@Test
	public void divide_divideBy0_exception() {
		try {
			@SuppressWarnings("unused")
			double result = App.divide(21.0, 0);
			fail("Dividing by 0 -> must throw exception!");
		} catch (IllegalArgumentException e) {
			assertEquals("You cant't divide by 0", e.getMessage());
		}
	}

	/**
	 * Check correctly if number is negative
	 * 
	 * @result True for negative input
	 */
	@Test
	public void isNegative_correctInput_correctResult() {
		boolean result = App.isNegative(-12.3);
		assertTrue(result);
	}
	
	/**
	 * Check correctly if positive number is true
	 * 
	 * @result True for negative input
	 */
	@Test
	public void isPositive_correctInput_correctResult() {
		boolean result = App.isPositive(12.3);
		assertTrue(result);
	}
	
	/**
	 * Check correctly if negative number is false
	 * 
	 * @result True for negative input
	 */
	@Test
	public void isPositive_incorrectInput_incorrectResult() {
		boolean result = App.isPositive(-12.3);
		assertFalse(result);
	}

	/**
	 * Check incorrectly if number is negative
	 * 
	 * @result False for positive input
	 */
	@Test
	public void isNegative_correctInput_incorrectResult() {
		boolean result = App.isNegative(12.3);
		assertFalse(result);
	}

	/**
	 * Check if conversion is correct
	 * 
	 * @result True for correct conversion
	 */
	@Test
	public void convertStringToArray_correctInput_correctResult() {
		char[] result = App.convertStringToArray("Maciek");
		char[] expected = { 'M', 'a', 'c', 'i', 'e', 'k' };
		assertArrayEquals(expected, result);
	}
	
	/**
	 * Check if conversion is correct
	 * 
	 * @result True for correct conversion
	 */
	@Test
	public void convertArrayToString_correctInput_correctResult() {
		String arr[] = { "M", "a", "c", "i", "e", "k" };
		String result = App.convertArrayToString(arr);
		String expected = "Maciek";
		
		assertEquals(expected, result);
	}
	
	/**
	 * Check if conversion is incorrect
	 * 
	 * @result True for correct conversion
	 */
	@Test
	public void convertArrayToString_correctInput_incorrectResult() {
		String arr[] = { "M", "a", "c", "i", "e", "k" };
		String result = App.convertArrayToString(arr);
		String expected = "Adbabshdkb";
		
		assertNotEquals(result, expected);
	}
	
	/**
	 * Check if result Array of conversion is not null
	 * 
	 * @result True if result array is not null
	 */
	@Test
	public void convertStringToArray_correctInput_resultNotNull() {
		char[] result = App.convertStringToArray("Maciek");
		assertNotNull(result);
	}

	/**
	 * Give incorrect triangle parameters
	 * 
	 * @result exception should be thrown
	 */
	@Test
	public void trianglePerimeter_incorrectInput_exception() {
		try {
			@SuppressWarnings("unused")
			double result = App.trianglePerimeter(1, 2, 3);
			fail("Incorrect triangle parameters -> must throw exception!");
		} catch (Exception e) {
			assertEquals("It's not triangle", e.getMessage());
		}
	}
	
	/**
	 * Give correct median of double array
	 * 
	 * @result true if median is correct
	 */
	@Test
	public void median_correctInput_correctOutput() {
		double arr[] = new double[] {11, 51 , 16, 11 , 6519, 191 ,0 , 98, 19854, 11, 32, 11};
		double result = App.median(arr);
		double expected = 24.0;
		
		assertEquals(result, expected, 0);
	}
	
	/**
	 * Check if median is incorrect
	 * 
	 * @result true if median is incorrect
	 */
	@Test
	public void median_correctInput_incorrectOutput() {
		double arr[] = new double[] {11, 51 , 16, 11 , 6519, 191 ,0 , 98, 19854, 11, 32, 11};
		double result = App.median(arr);
		double expected = -117.0;
		
		assertNotEquals(result, expected, 0);
	}
	
	/**
	 * Check if output is correct
	 * 
	 * @result true if year is 2021
	 */
	@Test
	public void currentYear_correctOutput() {
		int result = App.currentYear();
		int expected = 2021;
		
		assertEquals(result, expected);
	}
}
