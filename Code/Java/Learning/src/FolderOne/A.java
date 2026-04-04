package FolderOne;

/**
 * Class A demonstrates different Java access modifiers
 * including default, public, protected, and private.
 * 
 * It also shows how methods and variables with different
 * access levels can be accessed from other classes.
 */
public class A{

    /** 
     * Default access variable.
     * Accessible within the same package.
     */
    String defaultVar;  // Can be accessed from B, but not C

    /** 
     * Public access variable.
     * Accessible from any class.
     */
    public String publicVar; // Can be accessed from B and C

    /** 
     * Protected access variable.
     * Accessible within the same package and subclasses.
     */
    protected String protectedVar; // Can be accessed from B, but not C

    /** 
     * Private access variable.
     * Accessible only within this class.
     */
    private String privateVar; // Cannot be accessed from B and C
    
    /**
     * Default constructor that initializes all variables
     * with sample string values.
     */
    
    public A(){
        defaultVar = "DEFAULT";
        publicVar = "PUBLIC";
        protectedVar = "PROTECTED";
        privateVar = "PRIVATE";
    }
    
    /**
     * Default access method.
     * Can be called within the same package.
     */
    void defaultMethod(){
        IO.println("From Default Method");
    }
    
    /**
     * Public method accessible from any class.
     */
    public void publicMethod(){
        IO.println("From Public Method");
    }
    
    /**
     * Protected method accessible within the same package
     * and subclasses.
     */
    protected void protectedMethod(){
        IO.println("From Public Method");
    }
    
    /**
     * Private method accessible only within this class.
     */
    private void privateMethod(){
        IO.println("From Private Method");
    }
    
    /**
     * Wrapper method used to access private members.
     * 
     * Calls the private method and prints the private variable.
     */
    public void wrapper(){
        privateMethod();
        IO.println(this.privateVar);
    }
    
}
