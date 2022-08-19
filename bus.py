'''Importing the main MySQL module for the program.'''
import MySQLdb


'''The password required to modify tables and bus info.'''
Admin_Password="smartypants"


'''Code to create empty tables.'''
def create_empty_tables():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####",database="Bus_Ticket_Booking_Data")
    cur=db.cursor()
    cur.execute("create table Bus_List (Bus_ID int(6) primary key, Point_Of_Departure char(20), Destination char(20), Date_Of_Departure date, Time_Of_Departure varchar(10), Seats_Available int(2), Fare_In_Rs int(4))")
    cur.execute("create table Passenger_Info (Name char(25), Username char(15) primary key, Password char(15), Boarded_Bus_ID int(6) references Bus_List (Bus_ID), Number_Of_Seats_Reserved int(3),  Total_Cost_In_Rs int(6))")
    db.commit()


'''Code to create filled tables.'''
def create_filled_tables():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####",database="Bus_Ticket_Booking_Data")
    cur=db.cursor()


    '''Table of list of buses and related data.'''
    cur.execute("create table Bus_List (Bus_ID int(6) primary key, Point_Of_Departure char(20), Destination char(20), Date_Of_Departure date, Time_Of_Departure varchar(10), Seats_Available int(2), Fare_In_Rs int(4))")
    cur.execute("insert into Bus_List value(1001, 'Delhi', 'Jaipur', '2022-08-15', '11:00 PM', 50, 500)")
    cur.execute("insert into Bus_List value(1002, 'Jaipur', 'Delhi', '2022-10-26', '11:00 PM', 56, 500)")
    cur.execute("insert into Bus_List value(1003, 'Bengaluru', 'Chennai', '2022-08-15', '10:00 PM', 57, 450)")
    cur.execute("insert into Bus_List value(1004, 'Bengaluru', 'Vellore', '2022-08-16', '10:45 PM', 47, 300)")
    cur.execute("insert into Bus_List value(1005, 'Ajmer', 'Jaipur', '2022-08-07', '10:35 PM', 60, 200)")
    cur.execute("insert into Bus_List value(1006, 'Ajmer', 'Udaipur', '2022-08-09', '10:35 PM', 60, 200)")
    cur.execute("insert into Bus_List value(1007, 'Delhi', 'Ajmer', '2022-08-20', '09:00 PM', 55, 550)")
    cur.execute("insert into Bus_List value(1008, 'Delhi', 'Vrindavan', '2022-08-19', '09:30 PM', 40, 300)")
    cur.execute("insert into Bus_List value(1009, 'Jaipur', 'Ajmer', '2022-08-21', '08:45 PM', 40, 200)")
    cur.execute("insert into Bus_List value(1010, 'Vellore', 'Bengaluru', '2022-08-25', '10:30 PM', 54, 300)")

    '''Table of passenger info'''
    cur.execute("create table Passenger_Info (Name char(25), Username char(15) primary key, Password char(15), Boarded_Bus_ID int(6) references Bus_List (Bus_ID), Number_Of_Seats_Reserved int(3),  Total_Cost_In_Rs int(6))")
    cur.execute("insert into Passenger_Info value('Yuvraj Angi', 'erenislove', 'angi420', 1001, 5, 2500)")
    cur.execute("insert into Passenger_Info value('Sauhaard Batra', 'ladiesman', 'batra69', 1001, 5, 2500)")
    db.commit()


'''Code to create the database "Bus_Ticket_Booking_Data" in the user's MySQL server.'''
def create_database():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####")
    cur=db.cursor()
    cur.execute("select schema_name from information_schema.schemata where schema_name='Bus_Ticket_Booking_Data'")
    existing_db=cur.fetchall()
    if existing_db!=():
        option=int(input('''        A database named "Bus_Ticket_Booking_Data" already exists.
        Enter 1 to overwrite and create an empty database
        Enter 2 to overwrite and create a filled database
        Enter any other number to keep the current database-'''))
        if(option!=1 and option!=2):
            print("\n\n\n")
            return
            
        elif(option==1):
            cur.execute("drop database Bus_Ticket_Booking_Data")
            cur.execute("create database Bus_Ticket_Booking_Data")
            create_empty_tables()

        else:
            cur.execute("drop database Bus_Ticket_Booking_Data")
            cur.execute("create database Bus_Ticket_Booking_Data")
            create_filled_tables()
        print("     Database created.")
        print("\n\n\n")

    else:
        cur.execute("create database Bus_Ticket_Booking_Data")
        option=int(input('''        Enter 1 to create an empty database
        Enter any other number to create a filled database-'''))
        if(option==1):
            create_empty_tables()
        else:
            create_filled_tables()
        print("Database created.")
        print("Press Enter to continue.")
        print("\n\n\n")

    db.commit()


'''Code to book tickets.'''
def book():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####",database="Bus_Ticket_Booking_Data")
    cur=db.cursor()                                               
    start=input("Enter the name of your state-")                 
    dest=input("Enter your destination-")                         
    start.capitalize()
    dest.capitalize()                                             
    list_query=f"select * from Bus_List where Point_Of_Departure='{start}' and Destination='{dest}'"
    cur.execute(list_query)
    Available_buses_list=cur.fetchall()    

    if Available_buses_list==():
        print(f"No bus going from {start} to {dest} is available at the moment")

    else:
        #Print the data of the available bus.

        for field in Available_buses_list:
            if field[5]>0:
                print("Bus ID-", field[0])
                print("Point Of Departure-", field[1])
                print("Destination-", field[2])
                print("Date-", field[3])
                print("Time of Departure-", field[4])                  
                print("Seats Available-", field[5])
                print("Fare per head-", field[6],"Rs.")
                print("\n\n\n")

                x=input("Do you want to continue booking? (yes/no)-")
                if x=="yes":
                    num_seats=int(input("Enter the number of seats you want to book-"))
                    if field[5]>=num_seats:

                        #Input of passenger data.

                        name=input("Enter your name-")
                        username=input("Enter your username-")
                        cur.execute("Select username from Passenger_Info")
                        username_list=cur.fetchall()
                        while (username) in username_list:
                            username=input("This username is taken. Please choose another username-")
                        pwd=input("Enter your password-")
                        conf_pwd=input("Confirm your password-")
                        while(pwd!=conf_pwd):
                            print("The passwords do not match.")
                            pwd=input("Enter your password-")
                            conf_pwd=input("Confirm your password-")

                        #Updating the tables on successful booking

                        total_price=num_seats * Available_buses_list[0][6]
                        insert_query=f"insert into Passenger_Info values('{name}', '{username}', '{pwd}', {Available_buses_list[0][0]}, {num_seats}, {total_price})"
                        cur.execute(insert_query)
                        new_num_of_seats=Available_buses_list[0][5] - num_seats
                        update_query=f"update Bus_List set Seats_Available= {new_num_of_seats} where Bus_ID={Available_buses_list[0][0]}"
                        cur.execute(update_query)
                        db.commit()
                        print("Congratulations! Tickets booked successfully.")
                        input("Press Enter to continue.")


                    else:
                        print("Not enough seats")
                        input("Press Enter to continue.")

            else:
                print("No seats available at the moment.")           
                input("Press Enter to continue.")
    print("\n\n\n")


'''Code to cancel booking.'''
def cancel():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####",database="Bus_Ticket_Booking_Data")
    cur=db.cursor()
    username=input("Enter your username-")
    pwd=input("Enter your password-")
    check_query=f"select * from Passenger_Info where Username='{username}' and Password='{pwd}'"
    cur.execute(check_query)
    Result=cur.fetchall()

    if Result==():
        print("We don't have any entry with that username and password combination-")
        input("Press enter to continue")

    else:
        confirm=input("Do you really want to cancel your tickets? (yes/no)-")
        if confirm=="yes":
            cur.execute(f"select Boarded_Bus_ID,Number_Of_Seats_Reserved from Passenger_Info where Username='{username}' and Password='{pwd}'")
            seat_info=cur.fetchall()
            cur.execute(f"delete from Passenger_Info where Username='{username}' and Password='{pwd}'")
            cur.execute(f"select * from Bus_List where Bus_ID={seat_info[0][0]}")
            selected_bus=cur.fetchall()
            cur.execute(f"update Bus_List set Seats_Available={selected_bus[0][5] + seat_info[0][1]} where Bus_ID={seat_info[0][0]}")
            db.commit()
            print("Tickets cancelled successfully.")
            input("Press Enter to continue.")
    print("\n\n\n")
    

'''Code to modify bus_list table'''
def modify():
    db=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="####",database="Bus_Ticket_Booking_Data")
    cur=db.cursor()
    while True:
        print('''        1.Add a bus.
        2.Delete a bus.
        3.Manage number of seats.
        4.Manage price.
        5.Go back''')       
        num=int(input("Enter your option-"))

        #Code to add a bus.
        if num==1:
            bsid=input("Enter BusID of new bus-")
            pod=input("Enter point of departure-")
            des=input("Enter destination-")
            date=input("Enter date of departure-")
            time=input("Enter time of departure-")
            seat=input("Enter the number of seats-")
            fare=input("Enter price per head-")
            cur.execute("insert into Bus_List values("+bsid+",'"+pod.capitalize()+"','"+des.capitalize()+"','"+date+"','"+time+"','"+seat+"','"+fare+"')")
            db.commit()
            print("Bus added successfully.")
            print("\n\n\n")

        #Code to delete a bus and the passenger entries related to that bus.
        elif num==2:
            bsid=input("Enter BusID of the bus you want to remove-")
            cur.execute(f"delete from Bus_List where Bus_ID={bsid}")
            cur.execute(f"delete from Passenger_Info where Boarded_Bus_ID={bsid}")
            db.commit()
            print("Bus deleted successfully.")
            print("\n\n\n")
        
        #Code to update the number of seats in a bus.
        elif num==3:
            bsid=input("Enter BusID of the bus you want to update-")
            seat=input("Enter new number of seats-")
            cur.execute(f"update Bus_List set Seats_Available={seat} where Bus_ID={bsid}")
            db.commit()
            print("Number of seats updated successfully.")
            print("\n\n\n")

        #Code to update the price of a ticket of a bus.
        elif num==4:
            bsid=input("Enter BusID of the bus you want to update-")
            fare=input("Enter new price-")
            cur.execute(f"update Bus_List set Fare_In_Rs={fare} where Bus_ID={bsid}")
            db.commit()
            print("Fare updated successfully.")
            print("\n\n\n")

        elif num==5:
            print("\n\n\n")
            return


#The main function of the program.
def main_func():
    while True:
        num=int(input('''        Enter 0 to create the database
        Enter 1 to book tickets
        Enter 2 to cancel tickets
        Enter 3 to modify bus
        Enter 4 to exit-'''))
        print("\n\n\n")
        if num==0:
            input_password=input("Enter admin password- ")
            if(input_password==Admin_Password):
                create_database()
            else:
                print("Entered password was incorrect. \n\n\n")
        elif num==1:
            book()
        elif num==2:
            cancel()
        elif num==3:
            input_password=input("Enter admin password- ")
            if(input_password==Admin_Password):
                modify()
            else:
                print("Entered password was incorrect. \n\n\n")
        elif num==4:
            print("Thank you for using this service.\n\n\n")
            exit()


if __name__=="__main__":
    print("\nWelcome to bus ticket booking system.\n")
    main_func()
