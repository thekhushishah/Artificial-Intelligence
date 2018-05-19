f = open("input.txt","r")
lines = f.readlines()
group_count_line = lines[0].strip("\n")
group_count = int(group_count_line)
pot_count_line = lines[1].strip("\n")
pot_count = int(pot_count_line)
pots_division=[]
my_dictionary = {}
for i in range(0, pot_count):
    pots_division.append(lines[i+2].replace("\n", "").split(","))
teams_confederation = []
continents_list = []
cont_country = {c: 0 for c in ['UEFA', 'OFC', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC']}
for i in range(0,6):
    teams_confederation_continent = lines[i+2+pot_count].replace("\n","").split(":")
    continents_list.append(teams_confederation_continent[0])
    teams_confederation_countries = teams_confederation_continent[1].split(",")
    cont_country[teams_confederation_continent[0]]=teams_confederation_countries
    if teams_confederation_countries != "None":
        teams_confederation.append(teams_confederation_countries)
country_list = []
for t1 in teams_confederation:
    for t2 in t1:
        if t2 != 'None':
            country_list.append(t2)

rr = 0
for aa in range(0, pot_count):
    if len(pots_division[aa]) > rr:
        rr = len(pots_division[aa])
f.close()

assignment = [['0' for x in range(3*pot_count)] for y in range(group_count)]

def insert_by_pot(assignment, pot_taken, cont_country):
    rec_assignment=[row[:] for row in assignment]
    k = len(pot_taken)
    original = pot_taken[:]
    for z in range(0,k):
      if pot_taken[z] != 'Selected':
        country_considered = pot_taken[z]
        for i in continents_list:
            if country_considered in cont_country[i]:
                cont_name = i
        l = len(cont_country[cont_name])
        for i in range(0,group_count):
            C = 0
            P = 0
            if pot_taken[z] != 'Selected':
                for j in range(0, l):
                    if cont_country[cont_name][j] not in assignment[i]:
                        C = C + 1
                for j in range(0, k):
                    if original[j] not in assignment[i]:
                        P = P + 1
                if C == l and P == k and cont_name != 'UEFA':
                    assignment[i].append(country_considered)
                    pot_taken[z] = 'Selected'
                if (C == (l - 1) or C == l) and P == k and cont_name == 'UEFA':
                    assignment[i].append(country_considered)
                    pot_taken[z] = 'Selected'

    o = 0
    no_position = ['o']*k
    set = 0
    new_array = ['o']*k
    for z in range(0, k):
      set=0
      if pot_taken[z] != 'Selected':
          no_position[o] = pot_taken[z]
          set = 1
          o = o+1
      if set == 1:
          new_array[0] = original[k - 1]
          set = 0
          for z in range(0, k - 1):
              new_array[z + 1] = original[z]
          assignment = insert_by_pot(rec_assignment, new_array, cont_country)

    return assignment


final_assignment = ['' for x in range(group_count)]
fa = 1

for c in continents_list:
    l = len(cont_country[c])
    if c != 'UEFA':
        if l > group_count:
            fa = 0
    else:
        if l > 2 * group_count:
            fa = 0

if rr > group_count:
    fa = 0
elif fa == 1:
    for i in range(0, pot_count):
        assignment = insert_by_pot(assignment, pots_division[i], cont_country)

    for i in range(0, group_count):
         G = 0
         u = len(assignment[i])
         for j in range(0, u):

              if assignment[i][j] != '0':
                    final_assignment[i] = final_assignment[i]+assignment[i][j] + ','
              else:
                  G = G+1

         if G == len(assignment[i]):
              final_assignment[i] = 'None'
         else:
             final_assignment[i] = (final_assignment[i])[:-1]

out_file = open("output.txt", "w")
if fa == 0:
    out_file.write("No")
else:
    out_file.write("Yes")
    for i in range(0, group_count):
        out_file.write("\n")
        for j in range(0, len(final_assignment[i])):
                out_file.write(final_assignment[i][j])
out_file.close()