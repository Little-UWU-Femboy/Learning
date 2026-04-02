class Employee{
    int age;
    String name;

    Employee(int age, String name){
        this.name = name;
        this.age = age;
    }

    public String info(){
        return "My name is " + this.name + " and age is " + this.age;
    }

    public void practice(String n){
        name = n;
    }
    
    public void testing(){
        IO.println("Hello Friend Test");
    }
}
