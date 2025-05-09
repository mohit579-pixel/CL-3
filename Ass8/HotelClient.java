import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelServiceInterface hotelService = (HotelServiceInterface) Naming.lookup("rmi://localhost/HotelService");
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. Exit");
                System.out.print("Enter your choice: ");

                int choice = scanner.nextInt();
                scanner.nextLine(); // consume newline

                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String guestName = scanner.nextLine();

                        System.out.print("Enter room number: ");
                        int roomNumber = scanner.nextInt();
                        boolean booked = hotelService.bookRoom(guestName, roomNumber);
                        System.out.println(booked ? "Room booked successfully!" : "Room booking failed.");
                        break;

                    case 2:
                        System.out.print("Enter guest name for cancellation: ");
                        String cancelName = scanner.nextLine();
                        boolean canceled = hotelService.cancelBooking(cancelName);
                        System.out.println(canceled ? "Booking canceled successfully!" : "Booking cancellation failed.");
                        break;

                    case 3:
                        System.out.println("Exiting the client application.");
                        System.exit(0);

                    default:
                        System.out.println("Invalid choice.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
