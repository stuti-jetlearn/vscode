def display_menu():
    print("\n----- SET OPERATIONS MENU -----")
    print("1. Union of two sets")
    print("2. Intersection of two sets")
    print("3. Difference of two sets")
    print("4. Symmetric Difference of two sets")
    print("5. Exit")

while True:
    display_menu()

    # Taking user choice
    choice = int(input("Enter your choice (1-5): "))

    if choice in [1, 2, 3, 4]:
        # Input for both sets
        set1 = set(input("Enter elements of the first set separated by space: ").split())
        set2 = set(input("Enter elements of the second set separated by space: ").split())

    if choice == 1:
        union_set = set1.union(set2)
        print("Union of sets:", union_set)

    elif choice == 2:
        intersection_set = set1.intersection(set2)
        print("Intersection of sets:", intersection_set)

    elif choice == 3:
        difference_set = set1.difference(set2)
        print("Difference of sets (Set1 - Set2):", difference_set)

    elif choice == 4:
        sym_diff_set = set1.symmetric_difference(set2)
        print("Symmetric difference of sets:", sym_diff_set)

    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
