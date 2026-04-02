package AccessModifierExample.FolderOne;

class A{
    String defaultVar;  // Can be accessed from B, but not C
    public String publicVar; // Can be accessed from B and  C
    protected String protectedVar; // Can be accessed from B, but not C
    private String privateVar; // Cannot be accessed from B and C
    
    public A(){
        defaultVar = "DEFAULT";
        publicVar = "PUBLIC";
        protectedVar = "PROTECTED";
        privateVar = "PRIVATE";
    }
    
    // This can be called from B, but not C
    void defaultMethod(){
        IO.println("From Default Method");
    }
    
    // This can be called from B and C
    public void publicMethod(){
        IO.println("From Public Method");
    }
    
    // This can be called from B, but not C
    protected void protectedMethod(){
        IO.println("From Public Method");
    }
    
    // This can only be accessed from this class alone
    private void privateMethod(){
        IO.println("From Private Method");
    }
    
    // This is the wrapper needed to call the private method and variable since this class can only access them
    public void wrapper(){
        privateMethod();
        IO.println(this.privateVar);
    }
    
}