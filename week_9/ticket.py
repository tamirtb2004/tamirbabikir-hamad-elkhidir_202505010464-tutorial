def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    name = input("Student Name : ")
    student_id = input("Student ID : ")
    issue = input("Issue : ")
    location = input("Location : ")
    priority = input("Priority (High/Medium/Low): ")

    # Normalize input so "high", "HIGH", "High" all work the same
    priority = priority.strip().capitalize()

    if priority == "High":
        technician = "Ahmad"
    elif priority == "Medium":
        technician = "Siti"
    elif priority == "Low":
        technician = "Ali"
    else:
        technician = "Unassigned"

    status = "Pending"

    # Return everything as a tuple so main.py/display.py can use it
    return (name, student_id, issue, location, priority, technician, status)