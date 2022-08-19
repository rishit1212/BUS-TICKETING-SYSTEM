# Bus-Ticketing-System
A minimalistic project to book Bus Tickets using Python as Front-End and the Back-end, using MySQL as the DBMS.

This is a simple program, which may be used for high school projects. The program connects to your MySQL DBMS, and performs operations on it. One can create a default database using the "create database" option (THE ADMIN PASSWORD IS AT THE TOP OF THE CODE FILE). MAKE SURE TO CHANGE THE PASSWORD, HOST, ETC. IN THE CODE ACCORDING TO YOUR DATABASE NEEDS.

The operations include booking tickets, cancelling booked tickets, and modifying the buses list.

The names of the tables are Bus_List (Bus_ID int(6) primary key, Point_Of_Departure char(20), Destination char(20), Date_Of_Departure date, Time_Of_Departure varchar(10), Seats_Available int(2), Fare_In_Rs int(4))") and Passenger_Info (Name char(25), Username char(15) primary key, Password char(15), Boarded_Bus_ID int(6) references Bus_List (Bus_ID), Number_Of_Seats_Reserved int(3), Total_Cost_In_Rs int(6))

It is recommended that one has their MySQL command line open while running the code, and use SQL queries to see the changes being made to the tables for their own personal understanding.
