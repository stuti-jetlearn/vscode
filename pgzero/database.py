#create an empty dictionary
countryDb={}
#infinite loop
while True:
    #print menu
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")
    #get user choice
    choice=int(input("Enter your choice(1-5)"))
    #if insert
    if choice==1:
        country=input("Enter country :").upper()
        capital=input("Enter capital :").upper()
        countryDb[country]=capital
    #to display all countries
    elif choice==2:
        print(list(countryDb.keys()))
    #to display all capitals
    elif choice==3:
        print(list(countryDb.values()))
    #to display capital of a specific country
    elif choice==4:
        country=input("Enter country").upper()
        #print(countryDb[country])
        print(countryDb.get(country))
    #to delete entry of a specific country
    elif choice==5:
        country=input("Enter country :").upper()
        del countryDb[country]
    #if none of the above option
    else:
        break
        