public class Main {

    public static void main(String[] args){

        for(int x = 1000; x < 1005; x++){
            int number = x;
            int tmp = number;
            int rev = 0;

            System.out.println("CASE: " + x);

            while(tmp != 0){
                int digit = tmp % 10;
                System.out.println("digit: "+ digit);

                rev = rev * 10 + digit;
                System.out.println("rev: "+rev);

                tmp /= 10;
                System.out.println("tmp: "+tmp);
            }
            
            System.out.println("Reversed Number is: " + rev);
            System.out.println("Original Number time 4 is: " + number * 4);
        }
    }
}
