public class Employee{
	private String name;
	private int age;
	protected int salary;
	
	public Employee(String name, int age){
		this.name = name;
		this.age = age;
	}
	
	private int salaryIncrease() {
		this.salary+=300;
		return this.salary + 300;
	}
	
	protected void displaySalary() {
		System.out.println(this.salary);
	}
	
	public void wrapper() {
		salaryIncrease();
		displaySalary();
	}
}