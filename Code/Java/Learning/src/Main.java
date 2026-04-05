public class Main{
    static int x = 20;
    private int y = 50;
    
    public static void staticMethod(){
        System.out.println(x); // Works since this is a static variable
        // System.out.println(y); // Trying to do this will throw an compile time error
    }
    
    public static void main(String[] args){
        staticMethod();
    }
}
