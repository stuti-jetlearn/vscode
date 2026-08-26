# Program to find common hobbies between two friends using sets

# Input hobbies of Friend 1
friend1_hobbies = set(input("Enter hobbies of Friend 1 (comma-separated): ").split(','))

# Input hobbies of Friend 2
friend2_hobbies = set(input("Enter hobbies of Friend 2 (comma-separated): ").split(','))

# Remove any extra spaces
friend1_hobbies = {hobby.strip() for hobby in friend1_hobbies}
friend2_hobbies = {hobby.strip() for hobby in friend2_hobbies}

# Find common hobbies
common_hobbies = friend1_hobbies & friend2_hobbies  # Intersection

# Show result
print("\nFriend 1 hobbies:", friend1_hobbies)
print("Friend 2 hobbies:", friend2_hobbies)

if common_hobbies:
    print("✅ Common hobbies are:", common_hobbies)
else:
    print("❌ No common hobbies found.")
