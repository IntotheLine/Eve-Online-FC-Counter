#Eve fleet

fleet_killmail_count = str(0)
fleet_death_count = str(0)
fleet_isk_count = str(0)
fleet_lost_count = str(0)

print("Please enter amount of killmails")
while fleet_killmail_count <= str(0):
    fleet_killmail_count = input() + fleet_killmail_count
    if fleet_killmail_count >= str(0):

        print("please enter amount of death")
        while fleet_death_count <= str(0):
            fleet_death_count = input() + fleet_death_count
            if fleet_death_count >= str(0):
        

print("please enter amount of $-killed in million")
while fleet_isk_count <= str(0):
    fleet_isk_count = input() + fleet_isk_count
    if fleet_isk_count >= str(0):
        

print("please enter amount fo $-lost in million")
while fleet_lost_count <= str(0):
    fleet_lost_count = input() + fleet_lost_count
    if fleet_lost_count >= str(0):
        

print(fleet_killmail_count)
print(fleet_death_count)
print(fleet_isk_count)
print(fleet_lost_count)





