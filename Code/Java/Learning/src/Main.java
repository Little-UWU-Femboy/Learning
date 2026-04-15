class Main{
    static int add(){
        return 1 + 1;
    }
    
    static int add(int x){
        return x + 1;
    }
    
    static String add(String x){
        return x+".";
    }
    
    public static void main(String[] args){
        System.out.println(add());
        System.out.println(add(3));
        System.out.println(add("Hello, friend"));
    }
}