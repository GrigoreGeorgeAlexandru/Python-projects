public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }
     public static void main(String[] args) {
        Calculator calculator = new Calculator();
        System.out.println("Add: " + calculator.add(3, 5));
        System.out.println("Subtract: " + calculator.subtract(10, 4));
    }
}