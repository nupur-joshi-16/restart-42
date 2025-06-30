
public class Main {
    public static void main(String[] args) {
        int age = 21;
        int year = 2025;
        int quantity = 1;

        System.out.println("The year is " + year);

        double price = 1999.99;
        double gpa = 3.5;
        double temperature = -12.5;

        System.out.println("$" + price);

        char grade = 'A';
        char symbol = '!';
        char currency = '$';

        System.out.println(grade);

        boolean isStudent = true;
        boolean forSale = false;
        boolean isOnline = true;

        System.out.println(isStudent);

        if (isStudent) {
            System.out.println("You are a student");
        }
        else{
            System.out.println("You are not a student");
        }

        String name = "Nupur J.";
        String food = "Pizza";
        String email = "fake123@gmail.com";
        String car = "Mustang";
        String color = "red";
        System.out.println("Your favourite food is " + food);
        System.out.println("You are " + age + " years old");
        System.out.println("Yous gpa is " + gpa);
        System.out.println("Your average letter grade is " + grade);

        System.out.println("Your choice is a " + color + " " + year + " " + car);
        System.out.println("The price is: " + currency + price);

        if(forSale) {
            System.out.println("There is a " + car + " for sale");
        }
        else{
            System.out.println("There is a " + car + " not for sale");
        }

        //Exercise
        String studentName = "Nupur";
        int gta = 6;
        double pi = 3.14159;
        char gender = 'M';
        boolean isProgrammer = true;
    }
}


