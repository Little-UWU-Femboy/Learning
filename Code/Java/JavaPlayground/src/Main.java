/**
 * A sample class to demonstrate Java compilation, execution, and documentation.
 * This class provides basic arithmetic operations.
 */
public class Main {

    /**
     * The entry point of the application.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        System.out.println("Initializing the Java environment...");

        int result = add(10, 5);
        System.out.println("The result of 10 + 5 is: " + result);

        System.out.println("Project structure is working correctly!");
    }

    /**
     * Adds two integers together.
     * @param a The first number.
     * @param b The second number.
     * @return The sum of a and b.
     */
    public static int add(int a, int b) {
        return a + b;
    }
}
