from trajet_builder import TrajetBuilder
from mission import Mission

# Create Trajet instances using the builder
trajet1 = TrajetBuilder().set_start("City A").set_end("City B").set_departure_date("2024-01-01").set_arrival_date("2024-01-02").add_bon("bon1", 150).add_bon("bon2", 50).build()
trajet2 = TrajetBuilder().set_start("City B").set_end("City C").set_departure_date("2024-01-03").set_arrival_date("2024-01-04").add_bon("bon3", 120).add_bon("bon4", 80).build()

# Create a sub-mission
sub_mission = Mission("Sub-Mission 1")


sub_mission.add_element(trajet1)
sub_mission.add_element(trajet2)

# Create main mission
main_mission = Mission("Main Mission")
main_mission.add_element(sub_mission)

# Calculate and view details
print(f"Total Cost of Main Mission: {main_mission.calculerCout()}")
main_mission.view()
