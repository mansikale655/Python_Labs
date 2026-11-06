
#variables Of Different Datatypes
train_name = "Rajdhani Express"
train_number = 12951
source_station = "Mumbai"
destination_station = "Delhi"
ticket_price = 2450.75

#print the defined Variables
print("Welcome to Indian Railway Reservation Systems")
print("Train Name :",train_name)
print("Train Number:",train_number)
print("Source Station:",source_station)
print("Destination Station:",destination_station)

#display the datatype of Variable
print(type(train_name))
print(type(train_number))
print(type(ticket_price))

#new Variables
passenger_name="Rahul Sharma"
seat_number="B2-45"
is_confirmed=True

#changing the datatype using Typecasting
ticket_price_integer=int(ticket_price)
print(type(ticket_price_integer))

train_number_string=str(train_number)
print(type(train_number_string))

#simulating ticket Confirmation message

confirmation_status="Confirmed"
print("------Railway Ticket-------")
print("Passenger Name :",passenger_name)
print("Seat Number : ",seat_number)
print("Ticket Status  : ",confirmation_status)
print("---------------------------")

