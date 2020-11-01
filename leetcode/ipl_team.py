Teams = []

for i in range(12):

    team = input().upper()

    if team == "Q":

        break

    else:

        Teams.append(team)

Matches = []

for i in range(len(Teams)):

    for j in range(i+1, len(Teams)):

        Matches.append(Teams[i]+"-VS-"+Teams[j])

print("TOTAL MATCHES: ", len(Matches))

for i in Matches:

    print(i)
