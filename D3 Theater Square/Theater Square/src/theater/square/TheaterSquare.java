package theater.square;

import java.util.Scanner;

public class TheaterSquare {

    public static void main(String[] args) {
        
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int a = scanner.nextInt();
            
            long counter1 = (m % a) == 0 ? (m / a) : (m / a) + 1;
            long counter2 = (n % a) == 0 ? (n / a) : (n / a) + 1;
            
            System.out.println(counter1 * counter2);
        }
    }
    
}
