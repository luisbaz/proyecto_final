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

    
def adding_traveller_data(dic_traveller):
    traveller_option = str(input("Ingresa ('Y' o 'y') para registrar nuevos viajeros"))
    if traveller_option == 'Y' or traveller_option == 'y':
        traveller_option[passport] = Traveller(passport,forename,surname,date_of_birth,country,gender,marital_status)
        print("Has decidido registrar un nuevo pasaporte\n")
        new_passport = str(input("Introduce el pasaporte"))
        dic_traveller[passport] = new_passport

        new_forename = str(input("Introduce el nombre"))
        dic_traveller[passport].forename = new_forename

        new_surname = str(input("Introduce el apellido"))
        dic_traveller[passport].surname = new_surname

        new_date_of_birth = str(input("Introduce la fecha de nacimiento"))
        dic_traveller[passport].date_of_birth = new_date_of_birth

        new_country = str(input("Introduce la ciudad"))
        dic_traveller[passport].country = new_country

        new_gender = str(input("Introduce el genero"))
        dic_traveller[passport].gender = new_gender

        new_marital_status = str(input("Introduce el estado marital"))
        dic_traveller[passport].marital_status = new_marital_status
    else:
        pass
