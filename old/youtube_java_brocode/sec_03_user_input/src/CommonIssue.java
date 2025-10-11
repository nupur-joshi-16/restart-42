import java.util.Scanner;

public class CommonIssue {
    public static void main(String[] args) {

        // Common issue

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age : ");
        int age = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter your favourite color : ");
        String color = scanner.nextLine();

        System.out.println("You are " + age + " years old");
        System.out.println("You like the color " + color);

//        Output issue:
//        Enter your age : 42
//        Enter your favourite color : You are 42 years old
//        You like the color


//        We can solve this issue using scanner.nextLine();

        scanner.close();

    }
}





