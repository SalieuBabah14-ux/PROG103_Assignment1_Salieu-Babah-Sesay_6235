# COMMUNITY DATA PROCESSING SYSTEM

community_records = []

# Function to add resident data
def add_resident():
    print("\n===== ADD RESIDENT RECORD =====")

    name = input("Enter resident name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    occupation = input("Enter occupation: ")
    village = input("Enter village/community name: ")

    resident = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Occupation": occupation,
        "Village": village
    }

    community_records.append(resident)

    print("Resident record added successfully!")

# Function to display all records
def display_records():
    print("\n===== COMMUNITY RECORDS =====")

    if len(community_records) == 0:
        print("No records available.")
    else:
        for resident in community_records:
            print("\n----------------------------")
            print("Name:", resident["Name"])
            print("Age:", resident["Age"])
            print("Gender:", resident["Gender"])
            print("Occupation:", resident["Occupation"])
            print("Village:", resident["Village"])

# Function to search resident
def search_resident():
    search_name = input("\nEnter resident name to search: ")

    found = False

    for resident in community_records:
        if resident["Name"].lower() == search_name.lower():
            print("\n===== RESIDENT FOUND =====")
            print("Name:", resident["Name"])
            print("Age:", resident["Age"])
            print("Gender:", resident["Gender"])
            print("Occupation:", resident["Occupation"])
            print("Village:", resident["Village"])
            found = True
            break

    if not found:
        print("Resident not found.")

# Function to count residents
def count_residents():
    total = len(community_records)
    print("\nTotal Number of Residents:", total)

# Function to save records into file
def save_records():
    file = open("community_records.txt", "w")

    for resident in community_records:
        file.write(str(resident) + "\n")

    file.close()

    print("Records saved successfully!")

# Main Menu
while True:
    print("\n===== COMMUNITY DATA PROCESSING SYSTEM =====")
    print("1. Add Resident")
    print("2. Display Records")
    print("3. Search Resident")
    print("4. Count Residents")
    print("5. Save Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_resident()

    elif choice == "2":
        display_records()

    elif choice == "3":
        search_resident()

    elif choice == "4":
        count_residents()

    elif choice == "5":
        save_records()

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")