package pjatk.tau.lab1.lab1;

public class Triangle {
	public int a;
	public int b;
	public int c;
	public double area;
	
	public Triangle(int a, int b, int c) {
		this.a = a;
		this.b = b;
		this.c = c;
		this.area = this.areaByHeron(a, b, c);
	}
	
	public double areaByHeron() {
		double area = (this.a + this.b + this.c)/2.0d;
		return Math.sqrt(area* (area - this.a) * (area - this.b) * (area - this.c));
	}
	
	public double areaByHeron(int a, int b, int c) {
		double area = (a + b + c)/2.0d;
		return Math.sqrt(area* (area - a) * (area - b) * (area - c));
	}
	
	public boolean areSidesCorrect(int a, int b, int c) {
		if (a+b > c || a+c > b || b+c > a) {
			return true;
		} else {
			return false;
		}
	}
	
	public String triangleInfo(int a, int b, int c) {
		double area = this.areaByHeron(a, b, c);
		return String.format("a = " + a + " b = " + b + " c = " + c + " area: " + area);
	}
	
	public String triangleInfo() {
		return String.format("a = " + this.a + " b = " + this.b + " c = " + this.c + " area: " + this.area);
	}
}
