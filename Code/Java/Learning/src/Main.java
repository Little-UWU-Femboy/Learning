public class Main{
    
    public static void main(String[] args){
    	enum Light {
    		RED,
    		Yellow,
    		GREEN
    	}
    	
    	Light signal = Light.GREEN;
    	
    	System.out.println(signal);
    	System.out.println(Light.RED);
    }
}
