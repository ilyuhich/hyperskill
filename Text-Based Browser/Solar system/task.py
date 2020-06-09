# create the planets.txt
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
file = open("planets.txt", "w")
for planets in planets:
    file.writelines(f"{planets}\n")
file.close()
