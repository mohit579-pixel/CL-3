import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {
    private Map<Integer, String> bookedRooms;

    public HotelServer() throws RemoteException {
        bookedRooms = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (!bookedRooms.containsKey(roomNumber)) {
            bookedRooms.put(roomNumber, guestName);
            System.out.println("Room " + roomNumber + " booked for guest: " + guestName);
            return true;
        } else {
            System.out.println("Room " + roomNumber + " is already booked.");
            return false;
        }
    }

    @Override
    public synchronized boolean cancelBooking(String guestName) throws RemoteException {
        for (Map.Entry<Integer, String> entry : bookedRooms.entrySet()) {
            if (entry.getValue().equals(guestName)) {
                bookedRooms.remove(entry.getKey());
                System.out.println("Booking for guest " + guestName + " canceled.");
                return true;
            }
        }
        System.out.println("No booking found for guest " + guestName);
        return false;
    }

    public static void main(String[] args) {
        try {
            HotelServer server = new HotelServer();
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            Naming.rebind("HotelService", server);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
