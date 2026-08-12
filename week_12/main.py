from lab_system import check_computers, count_available, display_status

again = "Y"

while again == "Y":
    computers = check_computers()
    available = count_available(computers)
    display_status(computers, available)

    again = input("\nPerform another monitoring cycle? (Y/N): ").upper()

print("\nMonitoring stopped. Goodbye!")