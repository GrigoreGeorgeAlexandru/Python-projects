import java.util.Scanner;

public class Calculator {

    // Method to calculate the sum of the digits of a number
    public static int sumOfDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    // Method to check if a number is prime
    public static boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the first number
        System.out.print("Enter the first number (100-999): ");
        int num1 = scanner.nextInt();
        if (num1 < 100 || num1 > 999) {
            System.out.println("Number must be between 100 and 999.");
            return;
        }

        // Input the second number
        System.out.print("Enter the second number (100-999): ");
        int num2 = scanner.nextInt();
        if (num2 < 100 || num2 > 999) {
            System.out.println("Number must be between 100 and 999.");
            return;
        }

        // Calculate the sum of digits
        int sum1 = sumOfDigits(num1);
        int sum2 = sumOfDigits(num2);

        // Calculate the modulo
        int modulo = sum1 % sum2;

        // Check if the modulo is a prime number
        System.out.println("Sum of digits of " + num1 + " is: " + sum1);
        System.out.println("Sum of digits of " + num2 + " is: " + sum2);
        System.out.println("Modulo of the sums is: " + modulo);

        if (isPrime(modulo)) {
            System.out.println("The modulo is a prime number.");
        } else {
            System.out.println("The modulo is not a prime number.");
        }
    }
}
