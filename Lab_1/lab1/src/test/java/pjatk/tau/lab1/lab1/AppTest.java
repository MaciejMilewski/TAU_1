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

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;

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
}
