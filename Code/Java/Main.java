public class Main{
    public static void main(String[] args){
        var x = new Employee(20, "Jack");

        String name = x.info();
        IO.println(name); // Java 25

        System.out.println(x.name);
        x.practice("Tmp");

        System.out.println(x.name);
    }
}
