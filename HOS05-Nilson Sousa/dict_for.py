# Combine multiple dictionaries into a list and loop through them

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    for key, value in alien.items():
        print(f"{key}: {value}")
    print("---")
