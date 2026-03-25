public class Main{
    public static void main(){
        String templateFormat = "Value is %d and name is %s\n";
        int x = 50;
        String name = "Jack";

        System.out.println(templateFormat.formatted(x, name));
    }
}
