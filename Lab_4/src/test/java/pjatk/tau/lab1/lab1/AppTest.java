/**
 * Czwarte laboratorium na przedmiocie Testowanie Automatyczne - lato 2021
 * 
 * Zadanie:
 * (Termin oddania 20/04/2021 23:59) 
 * 1. Dodać do projektu Mockito
 * 2. Zamockować dwa elementy w projekcie np. 2 różne klasy i napisać przy ich użyciu po 3 testy (dla każdego użyć inny typ zwracany) - użyć when/given (https://github.com/arturadom/TAU_2021/tree/main/Laboratorium%204)
 * 3. Napisać i użyć stub (dla chętnych)
 * 
 * Autor: Maciej Milewski 17947
 * Repozytorium: https://github.com/MaciejMilewski/TAU_1/tree/main/Lab_4
 */

package pjatk.tau.lab1.lab1;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.*;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.doReturn;

import org.junit.Test;
import org.junit.jupiter.api.Assertions;

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
	
	@Test
	public void isCoprime_correctResult() {
		CoPrimeNumber coprime_number = mock(CoPrimeNumber.class);
		given(coprime_number.isCoprime(13, 15)).willReturn(true);
		
		CoPrimeNumber another_coprime_number = mock(CoPrimeNumber.class);
		given(another_coprime_number.isCoprime(11, 12)).willReturn(true);
		
		Assertions.assertEquals(coprime_number.coprime, another_coprime_number.coprime);
	}
	
	@Test
	public void isCoprimeVerdict_correctResult() {
		CoPrimeNumber coprime_number = mock(CoPrimeNumber.class);
		when(coprime_number.isCoprimeVerdict()).thenReturn("these numbers are coprime");
		String expected = "these numbers are coprime";

		Assertions.assertEquals(coprime_number.isCoprimeVerdict(), expected);
	}
	
	@Test
	public void findGCD_correctResult() {
		CoPrimeNumber coprime_number = mock(CoPrimeNumber.class);
		given(coprime_number.findGCD(20, 28)).willReturn(4);
		int gcd = coprime_number.findGCD(20, 28);
		int expected = 4;
		
		Assertions.assertEquals(gcd, expected);
	}
	
	@Test
	public void triangleArea_correctResult() {
		Triangle triangle = mock(Triangle.class);
		given(triangle.areaByHeron(3, 4, 5)).willReturn(6.0);
		double area = triangle.areaByHeron(3, 4, 5);
		double expected = 6.0;
		
		Assertions.assertEquals(area, expected);
	}
	
	@Test
	public void areTriangleSidesValid_correctResult() {
		Triangle triangle = mock(Triangle.class);
		given(triangle.areSidesCorrect(3, 4, 5)).willReturn(true);
		boolean area = triangle.areSidesCorrect(3, 4, 5);
		boolean expected = true;
		
		Assertions.assertEquals(area, expected);
	}
	
	@Test
	public void getTriangleInfo_correctResult1() {
		Triangle triangle = mock(Triangle.class);
		doReturn("a = 3 b = 4 c = 5 area: 6.0").when(triangle).triangleInfo();
		String expected = "a = 3 b = 4 c = 5 area: 6.0";
		
		Assertions.assertEquals(triangle.triangleInfo(), expected);
	}
}
