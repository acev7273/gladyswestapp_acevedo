from location import Location
from gladysUserLogin import login
from gladysSatellite import readSat
from gladysCompute import gpsValue

def main():
    location = Location()

    while True:
        print("Menu:")
        print("Type c to set current position")
        print("Type d to set destination position")
        print("Type m to map – which tells the distance")
        print("Type t to run module tests")
        print("Type q to quit")

        choice = input("Enter a command: ")

        if choice == 'q':
            break
        elif choice == 'c':
            x = float(input("Enter current X position: "))
            y = float(input("Enter current Y position: "))
            location.set_current_position(x, y)
        elif choice == 'd':
            x = float(input("Enter destination X position: "))
            y = float(input("Enter destination Y position: "))
            location.set_destination_position(x, y)
        elif choice == 'm':
            print(location.calculate_distance())
        elif choice == 't':
            login()  # Call the login function from gladysUserLogin
            readSat()  # Call the readSat function from gladysSatellite
            a = 10  # Example values for gpsValue function
            b = 20
            sat = "GladysSatellite"  # Example satellite name
            result = gpsValue(a, b, sat)  # Call the gpsValue function from gladysCompute
            print("Result from gpsValue:", result)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

