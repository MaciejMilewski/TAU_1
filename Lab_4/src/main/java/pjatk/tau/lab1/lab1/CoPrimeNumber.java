package pjatk.tau.lab1.lab1;

public class CoPrimeNumber {
	public int firstNumber;
	public int secondNumber;
	public int GCD = 1;
	public boolean coprime;

	public CoPrimeNumber(int firstNumber, int secondNumber) {
		this.firstNumber = firstNumber;
		this.secondNumber = secondNumber;
		this.coprime = isCoprime();
	}
	
	public boolean isCoprime() {
		int min, max;
		min = this.firstNumber;
		if (min > this.secondNumber) {
			min = this.secondNumber;
			max = this.firstNumber;
		} else {
			min = this.firstNumber;
			max = this.secondNumber;
		}
		while (max > min) {
			int r = max % min;
			if (r == 0) {
				this.GCD = min;
				break;
			} else {
				max = min;
				min = r;
			}
		}
		if (this.GCD == 1) {
			this.coprime = true;
			return true;
		} else {
			this.coprime = false;
			return false;
		}
	}
	
	public boolean isCoprime(int firstNumber, int secondNumber) {
		int min, max;
		int GCD = 1;
		min = firstNumber;
		if (min > secondNumber) {
			min = secondNumber;
			max = firstNumber;
		} else {
			min = firstNumber;
			max = secondNumber;
		}
		while (max > min) {
			int r = max % min;
			if (r == 0) {
				GCD = min;
				break;
			} else {
				max = min;
				min = r;
			}
		}
		if (GCD == 1) {
			return true;
		} else {
			return false;
		}
	}
	
	public int findGCD(int x, int y) {
		if (y == 0) {
	        return x;
	    }
	    return findGCD(y, x % y);
	}
	
	public String isCoprimeVerdict() {
		if(this.coprime == true) {
			return "these numbers are coprime";
		} else {
			return "these numbers are not coprime";
		}
	}
	
	public String isCoprimeVerdict(int firstNumber, int secondNumber) {
		if(this.isCoprime(firstNumber, secondNumber)) {
			return "these numbers are coprime";
		} else {
			return "these numbers are not coprime";
		}
	}
	
	@Override
    public String toString() {
		String result = isCoprimeVerdict();
        return String.format("First number = " + this.firstNumber + " " + "Second number = " + this.secondNumber + " " + "Verdict: " + result);
    }
}
