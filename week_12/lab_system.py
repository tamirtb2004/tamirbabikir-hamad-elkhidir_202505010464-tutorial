def check_computers():
    computers = []  # initial value

    for i in range(5):
        status = input(f"Computer {i + 1} Status (A/U/M): ").upper()
        computers.append(status)

    return computers


def count_available(computers):
    available = 0  # initial value

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========= LAB STATUS =========")

    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")

    print("---------------------------")
    print(f"Available Computers: {available}")
    print("===========================")