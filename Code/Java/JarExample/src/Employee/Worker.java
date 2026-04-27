package Employee;

public class Worker {
	private String name;
	private int age;
	private final String ID;
	
	public Worker(String ID, int age, String name){
		this.ID = ID;
		this.age = age;
		this.name = name;
	}
	
	public void Display() {
		System.out.println("Worker[name= " + this.name + " age= " + this.age + " ID= " + this.ID);
	}
}
