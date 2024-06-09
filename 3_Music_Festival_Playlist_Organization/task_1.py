# Define the list of artist names with duplicates
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# Initialize an empty set to store unique artist names
unique_artists = set()

# Use a loop to add each artist to the set
for artist in artist_names:
    unique_artists.add(artist)

# Display the unique artist lineup
print("Unique artist lineup:", unique_artists)
