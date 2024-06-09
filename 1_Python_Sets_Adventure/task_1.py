# Define the sets for our routes and competitor's routes
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Find destinations both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# Find destinations unique to our airline
unique_to_us = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_us)

# Assume all possible destinations for this example
all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SYD", "HND"}

# Combine both sets to see all destinations they cover together
all_routes = our_routes.union(competitor_routes)

# Check if there are any destinations neither airline shares
neither_share = all_possible_destinations.difference(all_routes)
print("Destinations neither airline flies to:", neither_share)
