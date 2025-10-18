import java.util.Scanner;

public class Calculator {

    // Metoda pentru insumarea cifrelor
    public static int sumOfDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    // Metoda de verificare daca numarul e prim
    public static boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Citeste primul numar
        System.out.print("Introdu primul numar (100-999): ");
        int num1 = scanner.nextInt();
        if (num1 < 100 || num1 > 999) {
            System.out.println("Numarul trebuie sa fie intre 100 si 999.");
            return;
        }

        // Citeste al doilea numar
        System.out.print("Introdu al doilea numar (100-999): ");
        int num2 = scanner.nextInt();
        if (num2 < 100 || num2 > 999) {
            System.out.println("Numarul trebuie sa fie intre 100 si 999.");
            return;
        }

        // Calcueaza suma cifrelor
        int sum1 = sumOfDigits(num1);
        int sum2 = sumOfDigits(num2);

        // Calculeaza restul
        int modulo = sum1 % sum2;

        // Verifica daca restul este numar prim
        System.out.println("Suma cifrelor numarului " + num1 + " este: " + sum1);
        System.out.println("Suma cifrelor numarului " + num2 + " este: " + sum2);
        System.out.println("Restul impartirii este: " + modulo);

        if (isPrime(modulo)) {
            System.out.println("Restul este numar prim.");
        } else {
            System.out.println("Restul nu este numar prim.");
        }
    }
}
