def adding_flight_data(dic_flights):
    print("Bienvenido al menu de registro de datos\n")
    flight_option = str(input("Ingresa ('Y' o 'y') para registrar nuevos vuelos"))

    if flight_option == 'y' or  flight_option == 'Y':
        dic_flights[ID+plate] = Flight(ID,plate,origin,destiny,departure,arriving,status,departure_gate,take_off_track,arriving_gate,landing_track,pilot,copilot,attendant)
        new_id = str(input("Introduce el id que deseas registrarp\n"))
        dic_flights[ID+plate].ID = new_id

        new_plate = str(input("Introduce el plate del vuelo"))
        dic_flights[ID+plate].plate = new_plate

        new_origin = str(input("Introduce el origen del vuelo"))
        dic_flights[ID+plate].origin = new_origin

        new_destiny = str(input("Introduce el destino del vuelo"))
        dic_flights[ID+plate].destiny = new_destiny

        new_departure = str(input("Introduce la salida del vuelo"))
        dic_flights[ID+plate].departure = new_departure

        new_arriving = str(input("Introduce la llegada del vuelo"))
        dic_flights[ID+plate].arriving = new_arriving

        new_status = str(input("Introduce el estatus del vuelo"))
        dic_flights[ID+plate].status = new_status

        new_departure_gate = str(input("Introduce la puerta de salida del vuelo"))
        dic_flights[ID+plate].departure_gate = new_departure

        new_take_off_track = str(input("Introduce la pista de despegue del vuelo"))
        dic_flights[ID+plate].take_off_track = new_take_off_track

        new_arriving_gate = str(input("Introduce la puerta de llegada del vuelo"))
        dic_flights[ID+plate].arriving_gate = new_arriving_gate

        new_landing_track = str(input("Introduce la pista de aterriaje del vuelo"))
        dic_flights[ID+plate].landing_track = new_landing_track

        new_pilot = str(input("Introduce el piloto de vuelo asignado"))
        dic_flights[ID+plate].pilot = new_pilot

        new_copilot = str(input("Introduce el copiloto de vuelo asignado"))
        dic_flights[ID+plate].copilot = new_copilot

        new_attendant = str(input("Introduce a los asistentes de vuelo asignados"))
        dic_flights[ID+plate].attendant = new_attendant
    else:
        pass

    
       
