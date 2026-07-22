def display_ticket(ticket):
    name, student_id, issue, location, priority, technician, status = ticket

    print()
    print("========= HELPDESK TICKET =========")
    print(f"Student Name : {name}")
    print(f"Student ID   : {student_id}")
    print(f"Issue        : {issue}")
    print(f"Location     : {location}")
    print(f"Priority     : {priority}")
    print(f"Technician   : {technician}")
    print(f"Status       : {status}")
    print("====================================")