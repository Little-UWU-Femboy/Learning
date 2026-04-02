package FolderOne;

public class B{
    void main(){
        A a = new A();
        
        a.defaultMethod();
        a.protectedMethod();
        a.publicMethod();
        
        System.out.println(a.defaultVar);
        System.out.println(a.protectedVar);
        System.out.println(a.publicVar);
    }
}