public class Employee{
	private String name;
	private int age;
	protected int salary;
	
	public Employee(String name, int age, int salary){
		this.name = name;
		this.age = age;
		this.salary = salary;
	}
	
	Employee(){
		this("Jack", 50, 500);
	}
	
	private int salaryIncrease() {
		this.salary+=300;
		return this.salary + 300;
	}
	
	protected void displaySalary() {
		System.out.println(this.salary);
		System.out.println(this.name);
		System.out.println(this.age);
	}
	
	public void wrapper() {
		salaryIncrease();
		displaySalary();
	}
}