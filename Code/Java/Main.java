public class Main{
    public static void main(String[] args){
        Employee x = new Employee(20, "Jack");
        
        String name = x.info();
        IO.println(name);
    }
}
