from datetime import datetime
from random import randrange, shuffle, choice


def title():
    # genera el titulo del historial / generates the history's title
    now = str(datetime.now())
    file_name = "history.txt"
    file = open(file_name, "a")
    file.write("\n\n\n\n SANTIAGO WAR BOT VERSION 1.4 - Developed by @patricknaoj & @alesxme\n\n")
    file.write("Generated in {}\n Listed from oldest to newest.\n\n ".format(now))
    file.close()

    # muestra texto al ejecutar / display an introduction in screen
    print("\CHILE WAR BOT 2023 VERSION 1.4 - Desarrollado por @patricknaoj & @alesxme\n")
    print("Surge una guerra civil en Chile. El pánico inunda las calles de sus comunas. El futuro es incierto.")
    print("Este bot generará batallas y alianzas entre provincias de nuestro pais"
          " y escogerá un ganador basado entre\n el azar y el poderío de sus poblaciones. \n")
    input("Presione la tecla Enter para comenzar..\n")


def import_town_list():
    # lista de comunas: el primer valor es la comuna/municipio y el resto de valores son sus vecinos
    # town list: first value is the main town, others values are their neighbours
    town_list = [['Arica', 'Parinacota', 'Tamarugal'],
    ['Parinacota', 'Arica', 'Tamarugal'],
    ['Iquique', 'Tamarugal', 'Tocopilla'],
    ['Tamarugal', 'Tocopilla', 'El Loa', 'Arica', 'Parinacota', 'Iquique'],
    ['Antofagasta', 'Chañaral', 'El Loa', 'Tocopilla'],
    ['El Loa', 'Tamarugal', 'Tocopilla', 'Antofagasta'],
    ['Tocopilla', 'Tamarugal', 'El Loa', 'Iquique', 'Antofagasta'],
    ['Chañaral', 'Copiapó', 'Antofagasta'],
    ['Copiapó', 'Huasco', 'Chañaral'],
    ['Huasco', 'Copiapó', 'Elqui'],
    ['Choapa', 'Limarí', 'Petorca', 'San Felipe'],
    ['Limarí', 'Elqui', 'Choapa'],
    ['Elqui', 'Huasco', 'Limarí'],
    ['Los Andes', 'San Felipe', 'Santiago', 'Chacabuco', 'Cordillera'],
    ['San Felipe', 'Los Andes', 'Petorca', 'Quillota', 'Chacabuco'],
    ['Petorca', 'Quillota', 'San Felipe', 'Choapa', 'Valparaíso'],
    ['Quillota', 'San Felipe', 'Petorca', 'Chacabuco', 'Valparaíso', 'Marga Marga'],
    ['Valparaíso', 'Petorca', 'Marga Marga', 'Quillota', 'San Antonio', 'Melipilla', 'Isla de Pascua'],
    ['Santiago', 'Chacabuco', 'Cordillera', 'Los Andes', 'Melipilla', 'Maipo', 'Talagante'],
    ['Chacabuco', 'Los Andes', 'Melipilla', 'Santiago', 'Quillota', 'San Felipe', 'Marga Marga'],
    ['Marga Marga', 'Quillota', 'Chacabuco', 'Melipilla', 'Valparaíso'],
    ['Cordillera', 'Cachapoal', 'Maipo', 'Santiago', 'Los Andes'],
    ['Talagante', 'Maipo', 'Melipilla', 'Santiago'],
    ['Maipo', 'Cordillera', 'Cachapoal', 'Talagante', 'Melipilla', 'Santiago'],
    ['Melipilla', 'Cardenal Caro', 'Cachapoal', 'Talagante', 'Maipo', 'Santiago', 'Chacabuco', 'San Antonio', 'Marga Marga', 'Valparaíso'],
    ['San Antonio', 'Valparaíso', 'Melipilla', 'Cardenal Caro'],
    ['Isla de Pascua', 'Valparaíso'],
    ['Cachapoal', 'Melipilla', 'Maipo', 'Cordillera', 'Cardenal Caro', 'Colchagua'],
    ['Cardenal Caro', 'Colchagua', 'Curicó', 'Cachapoal', 'Melipilla', 'San Antonio'],
    ['Colchagua', 'Cardenal Caro', 'Cachapoal', 'Curicó'],
    ['Curicó', 'Colchagua', 'Cardenal Caro', 'Talca'],
    ['Talca', 'Curicó', 'Linares', 'Cauquenes'],
    ['Cauquenes', 'Talca', 'Linares', 'Punilla', 'Itata'],
    ['Punilla', 'Itata', 'Linares', 'Cauquenes', 'Diguillín'],
    ['Linares', 'Cauquenes', 'Talca', 'Punilla'],
    ['Diguillín', 'Punilla', 'Itata', 'Concepción'],
    ['Itata', 'Punilla', 'Diguillín', 'Cauquenes', 'Concepción'],
    ['Concepción', 'Itata', 'Diguillín', 'Bio-bío', 'Arauco'],
    ['Arauco', 'Bio-bío', 'Malleco', 'Concepción', 'Cautín'],
    ['Bio-bío', 'Diguillín', 'Malleco', 'Arauco', 'Concepción'],
    ['Malleco', 'Bio-bío', 'Arauco', 'Cautín'],
    ['Cautín', 'Arauco', 'Malleco', 'Valdivia'],
    ['Valdivia', 'Cautín', 'Ranco'],
    ['Ranco', 'Valdivia', 'Osorno'],
    ['Llanquihue', 'Osorno', 'Chiloé', 'Palena'],
    ['Chiloé', 'Llanquihue', 'Palena'],
    ['Osorno', 'Ranco', 'Llanquihue'],
    ['Palena', 'Chiloé', 'Llanquihue', 'Aysén', 'Coyhaique'],
    ['Aysén', 'Coyhaique', 'Palena', 'General Carrera', 'Capitán Prat'],
    ['Capitán Prat', 'Aysén', 'General Carrera', 'Ultima Esperanza'],
    ['General Carrera', 'Coyhaique', 'Aysén', 'Capitán Prat'],
    ['Coyhaique', 'Palena', 'Aysén', 'General Carrera'],
    ['Magallanes', 'Tierra del Fuego', 'Ultima Esperanza', 'Antártica Chilena'],
    ['Ultima Esperanza', 'Magallanes', 'Capitán Prat'],
    ['Tierra del Fuego', 'Antártica Chilena', 'Magallanes'],
    ['Antártica Chilena', 'Magallanes', 'Tierra del Fuego']]
    return town_list

town_list = import_town_list()


def import_population():
    # lista de habitantes por comuna segun ine 2020, mismo orden que lista de comunas
    # inhabitants list per town in the same order that town list
    pop_list = []
    list_file2 = "population.txt"
    try:
        with open(list_file2, "r") as file:
            pop_list = file.read().split("\n")
    except FileNotFoundError:
        print("\n Error: population.txt file not found\n Error: poblacion de comunas no encontrada")

    return pop_list


population_list = import_population()


def save(movement):
    # guarda cada movimiento en el archivo / saves every single movement in the file
    file_name = "history.txt"
    file = open(file_name, "a")
    file.write("\n" + movement)
    file.close()


def battle():
    team1_number = randrange(0, len(town_list))  # elige un equipo y a su vecino / choose random team and neighbour
    team1 = town_list[team1_number][0]
    team2 = town_list[team1_number][randrange(1, len(town_list[team1_number]))]

    # buscar el numero del equipo 2 en la town_list / finds second team's number in town_list
    team2_number = None
    for town in town_list:
        if town[0] == team2:
            team2_number = town_list.index(town)

    team1_population = int(int(population_list[team1_number]))
    team2_population = int(int(population_list[team2_number]))

    if (team1_population / team2_population) > 1:
        diff_between_teams = (team1_population / team2_population)
    elif (team1_population / team2_population) < 1:
        diff_between_teams = -1 * (team2_population / team1_population)
    
    luck_list = [-2, -1, 0, 1, 2]
    moral = choice(luck_list)
    
   
    print (abs(diff_between_teams))
    if 1.0 < abs(diff_between_teams) < 1.5 :
            diff_between_teams = diff_between_teams / (25 + moral)
    elif 1.5 < abs(diff_between_teams) < 2.0 :
            diff_between_teams = diff_between_teams / (20 + moral)
    elif 2.0 < abs(diff_between_teams) < 3.5 :
            diff_between_teams = diff_between_teams / (21 + moral)
    elif 2.0 < abs(diff_between_teams) < 5.0 :
            diff_between_teams = diff_between_teams / (16 + moral)    
    elif 5.0 < abs(diff_between_teams) < 10.0 :
            diff_between_teams = diff_between_teams / (20 + moral)  
            
    if "Santiago" in team1 or "Santiago" in team2:
        if 1.0 < abs(diff_between_teams) < 2.0 :
            diff_between_teams = diff_between_teams / (17 + moral)
        if 2.0 < abs(diff_between_teams) < 5.0 :
            diff_between_teams = diff_between_teams / (16 + moral)    
        if 5.0 < abs(diff_between_teams) < 10.0 :
            diff_between_teams = diff_between_teams / (26 + moral)        

    prob_team1 = 0.5 + diff_between_teams
    
    if prob_team1 > 0.95:
        prob_team1 = 0.95
    elif prob_team1 < 0.05:
        prob_team1 = 0.05       


    q = 10000
    probabilities = [team1] * int(prob_team1 * q) + [team2] * int((1 - prob_team1) * q)
    final_winner = choice(probabilities)

    results = {team1: 0, team2: 0}
    for i in range(100000):
        results[choice(probabilities)] += 1
    prob_team1 = (100 * results[team1]) / (results[team2] + results[team1])

    if team1 == final_winner:
        winner = team1
        winner_number = team1_number
        loser = team2
        loser_number = team2_number
    else:
        winner = team2
        winner_number = team2_number
        loser = team1
        loser_number = team1_number


    print("Los combatientes son {} y {}.  \n".format(team1.title(), team2.title()))

    
    if moral == -2:
        print("{} se preparó estrategicamente y fue a la ofensiva.".format(team1.title()))
    elif moral == -1:
        print("La gente de {} se encontraba optimista.".format(team1.title()))
    elif moral == 1:
        print("{} se encontraba en mala forma.".format(team1.title()))
    elif moral == 2:
        print("{} no vio venir al enemigo hasta que fue muy tarde.".format(team1.title()))
    
    print("La probabilidad de ganar para {0} era de un {1}%.".format(team1.title(), prob_team1))
    
    if "Alianza" in loser:
        print("La falta de organización de la alianza no permitió sobrellevar la batalla y optó por rendirse")
    
    print("Finalmente, el ganador fue {}.".format(winner.title()))

    # esto se escribe en el historial / this is written in the save function
    movement = "Los combatientes son {} y {}. El ganador es: {}".format(team1.title(),
                                                                        team2.title(), winner.title())

    return loser, loser_number, winner, winner_number, movement


def battle_consequences(loser, loser_number  , winner, winner_number):
    for neighbour in town_list[loser_number]:  # añadir los vecinos de la comuna perdedora a la ganadora
        if neighbour not in town_list[winner_number]:  # transfer loser's neighbours to the winner
            town_list[winner_number].append(neighbour)

    # añadir el nombre el ganadora a los vecindarios que antes tenian al perdedor
    # append the winner's name to the lists that had the loser
    for neighbourhood in town_list:
        if winner not in neighbourhood:
            if loser in neighbourhood:
                neighbourhood.append(winner)

    for town in town_list:  # elimina el nombre del perdedor de todas las listas
        try:  # deletes loser's name from all lists
            town.remove(loser)
        except ValueError:
            pass

    town_list.pop(loser_number)  # borra la lista del perdedor de la lista de comunas / delete the loser's list

    winner_population = int(population_list[winner_number])
    loser_population = int(population_list[loser_number])

    population_list.pop(winner_number)  # añade poblacion  del perdedor al ganador/adds loser's population to the winner
    if "Santiago" in winner:
        winner_population = winner_population + (loser_population / 3)
        
    else:
        winner_population = winner_population + (loser_population / 1.5)
    
    population_list.insert(winner_number, str(int(winner_population)))

    population_list.pop(loser_number)  # borra la lista del perdedor de la lista de poblacion / delete the loser's list

    #print("Las perdidas ascienden a {} personas.".format(int(((loser_population / 3) * 2) / 10)))
    print("{} comunas restantes...\n".format(len(town_list)))
    # if len(town_list) > 2:
    # print("Los vecindarios actuales son{}\n".format(town_list))


def alliance():
    random_number = randrange(0, len(town_list))  # elige un equipo y a su vecino / choose random team and neighbour
    team1 = town_list[random_number][0]
    team2 = town_list[random_number][randrange(1, len(town_list[random_number]))]

    teams_shuffled = [team1, team2]
    shuffle(teams_shuffled)  # hace que sean mostrados en orden aleatorio / make them appear randomly in display

    # arregla el nombre de las alianzas para que no se repita la palabra / fixes the alliances names
    if "alianza" in team1 or team2:
        alliance_name = "alianza " + team1.replace("alianza ", "") + " - " + team2.replace("alianza ", "")
    else:
        alliance_name = "alianza " + team1 + " - " + team2

    print("Se ha formado una alianza entre {} y {}".format(teams_shuffled[0].title(), teams_shuffled[1].title()))
    print("Han decidido llamarse: {}".format(alliance_name.title()))

    # esto se escribe en el historial / this is written in the save function
    movement = "Se ha formado una alianza entre {} y {}. Han decidido llamarse {}".format(teams_shuffled[0].title(),
                                                                                          teams_shuffled[1].title(),
                                                                                          alliance_name.title())

    # buscar el numero de la comuna ganadora en la town_list / finds winner's number in town_list
    winner_number = None
    for town in town_list:
        if town[0] == team2:
            winner_number = town_list.index(town)

    return team1, random_number, team2, winner_number, alliance_name, movement


def alliance_consequences(loser, loser_number, winner, winner_number, alliance_name):
    # usamos los valores loser para referirnos al team 1 y winner para team 2
    # we used loser and winner values to refer to team 1 and team 2 respectively

    # reemplaza el nombre del ganador por el de la alianza / replace team's 2 name with alliance's name
    town_list[winner_number].pop(0)
    town_list[winner_number].insert(0, alliance_name)

    for neighbour in town_list[loser_number]:  # añadir los vecinos del team 1 a la alianza
        if neighbour not in town_list[winner_number]:  # transfer team's 1 neighbours to alliance
            town_list[winner_number].append(neighbour)

    # añadir el nombre de la alianza a los vecindarios que tenian al team 1 como vecino
    # append the alliance's name to the lists that had team 1 as neighbour
    for neighbourhood in town_list:
        if alliance_name not in neighbourhood:
            if winner not in neighbourhood:
                if loser in neighbourhood:
                    neighbourhood.append(alliance_name)

    # añadir el nombre de la alianza a los vecindarios que tenian al team 2 como vecino
    # append the alliance's name to the lists that had team 2 as neighbour
    for neighbourhood in town_list:
        if alliance_name not in neighbourhood:
            if winner in neighbourhood:
                neighbourhood.append(alliance_name)

    for town in town_list:  # elimina el nombre del team 1 de todas las listas
        try:  # remove team's 1 name from all lists
            town.remove(loser)
        except ValueError:
            pass

    for town in town_list:  # elimina el nombre del team 2 de todas las listas
        try:  # remove team's 2 name from all lists
            town.remove(winner)
        except ValueError:
            pass

    town_list.pop(loser_number)  # borra la lista del perdedor de la lista de comunas

    winner_population = int(population_list[winner_number])
    loser_population = int(population_list[loser_number])
    new_soldiers = int(loser_population / 20)

    population_list.pop(winner_number)  # añade poblacion  del perdedor al ganador/adds loser's population to the winner
    winner_population = winner_population + loser_population * 0.70
    population_list.insert(winner_number, str(int(winner_population)))

    population_list.pop(loser_number)  # borra la lista del perdedor de la lista de poblacion / delete the loser's list

    # removes team's 1 list from town's list
    print("La alianza ha permitido el desarrollo de {} nuevos soldados.".format(new_soldiers))
    print("{} comunas restantes...\n".format(len(town_list)))
    # if len(town_list) > 2:
    # print("Los vecindarios actuales son{}\n".format(town_list))


def end_screen():
    # imprime el ultimo en pie / prints the last town standing
    last_standing = town_list[0][0]
    last_inhabitants = population_list[0]
    print("\nLa última comuna en pie es {}.".format(last_standing.title()))
    print("Numero de habitantes: {}".format(last_inhabitants))
    input("Partida guardada. Presione la tecla Enter dos veces para salir.\n")
    input()


def main():
    title()
    # mientras queden comunas/municipios en pie / while there are still towns standing
    while len(town_list) != 1:
        # ventanas de turnos con alianzas permitidas / alliance's are allowed only during those turns
        if 52 < len(town_list) < 56 or 25 < len(town_list) < 29 or 10 < len(town_list) < 14 or 2 < len(town_list) < 5:

            flip_coin = (randrange(0, 2))

            if flip_coin == 0:  # ocurre una batalla / a battle occurs
                loser_and_number = battle()
                battle_consequences(loser_and_number[0], loser_and_number[1], loser_and_number[2], loser_and_number[3])
                save(loser_and_number[4])

            elif flip_coin == 1:  # ocurre una alianza / an alliance occurs
                alliance_and_number = alliance()
                alliance_consequences(alliance_and_number[0], alliance_and_number[1], alliance_and_number[2],
                                      alliance_and_number[3], alliance_and_number[4])
                save(alliance_and_number[5])

        else:  # ocurre una batalla / a battle occurs
            loser_and_number = battle()
            battle_consequences(loser_and_number[0], loser_and_number[1], loser_and_number[2], loser_and_number[3])
            save(loser_and_number[4])

        input("Presione la tecla Enter para continuar...\n")

    end_screen()


if __name__ == '__main__':
    main()
