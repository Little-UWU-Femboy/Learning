import java.util.Date;
import java.time.LocalDate;

public class Main{
    public static void main(String[] args){
        IO.println("Starting");
        Date timer = new Date();
        LocalDate date = LocalDate.now();

        IO.println(timer);
        IO.println(date.getMonth());
    }
}
