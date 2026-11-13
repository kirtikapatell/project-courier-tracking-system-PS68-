# Courier Tracking System in Python 3
# PS-68

import copy

# Global Data
parcels = {}
tracking_counter = 1001

STATUS_FLOW = [
    "Booked",
    "Picked Up",
    "In Transit",
    "Out for Delivery",
    "Delivered"
]


# 1. Generate Unique Tracking ID
def generate_tracking_id():
    global tracking_counter

    tid = f"CT{tracking_counter}"

    while tid in parcels:
        tracking_counter += 1
        tid = f"CT{tracking_counter}"

    tracking_counter += 1
    return tid


# 2. Get Valid Input
def get_valid_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


# 3. Book Parcel
def book_parcel(sender=None, receiver=None, destination=None):

    if sender is None:
        sender = get_valid_input("Enter Sender Name: ")

    if receiver is None:
        receiver = get_valid_input("Enter Receiver Name: ")

    if destination is None:
        destination = get_valid_input("Enter Destination: ")

    sender = sender.strip()
    receiver = receiver.strip()
    destination = destination.strip()

    if not sender or not receiver or not destination:
        print("Error: All parcel details are required.")
        return None

    tid = generate_tracking_id()

    parcels[tid] = {
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "history": ["Booked"]
    }

    print("Parcel booked successfully!")
    print(f"Tracking ID: {tid} | Status: Booked")

    return tid


# 4. Update Parcel Status
def update_status(tid=None):

    if tid is None:
        tid = input("Enter Tracking ID: ").strip()

    if tid not in parcels:
        print(f"Tracking ID {tid} not found.")
        return

    current_history = parcels[tid]["history"]
    current_status = current_history[-1]

    if current_status == "Delivered":
        print(
            f"Parcel {tid} is already delivered. "
            "No further updates allowed."
        )
        return

    current_index = STATUS_FLOW.index(current_status)
    next_status = STATUS_FLOW[current_index + 1]

    current_history.append(next_status)

    print(f"Status updated: {current_status} -> {next_status}")


# 5. Track Parcel Details
def track_parcel_details(tid=None):

    if tid is None:
        tid = input("Enter Tracking ID: ").strip()

    if tid not in parcels:
        print(f"Tracking ID {tid} not found.")
        return

    p = parcels[tid]

    current_status = p["history"][-1]
    history_str = " -> ".join(p["history"])

    print("\n----- PARCEL DETAILS -----")
    print(f"Tracking ID: {tid}")
    print(f"Sender: {p['sender']}")
    print(f"Receiver: {p['receiver']}")
    print(f"Destination: {p['destination']}")
    print(f"History: {history_str}")
    print(f"Current Status: {current_status}")


# 6. Search Parcel By Receiver
def search_by_receiver(name=None):

    if name is None:
        name = get_valid_input("Enter Receiver Name to search: ")

    name = name.strip()

    if not name:
        print("Receiver name cannot be empty.")
        return

    found = False

    for tid, p in parcels.items():

        if p["receiver"].lower() == name.lower():

            print(
                f"Tracking ID: {tid} | "
                f"Destination: {p['destination']} | "
                f"Status: {p['history'][-1]}"
            )

            found = True

    if not found:
        print(f"No parcels found for receiver: {name}")


# 7. Run All Four Test Cases
def run_test_cases():

    global parcels, tracking_counter

    original_parcels = copy.deepcopy(parcels)
    original_counter = tracking_counter

    try:
        parcels = {}
        tracking_counter = 1001

        # Test Case 1: Normal Input
        print("\n--- TEST CASE 1: NORMAL INPUT ---")

        tid1 = book_parcel("Neha", "Karan", "Nagpur")

        # Test Case 2: Boundary / Minimum Input
        print("\n--- TEST CASE 2: BOUNDARY / MINIMUM INPUT ---")

        update_status(tid1)

        # Test Case 3: Invalid Input
        print("\n--- TEST CASE 3: INVALID INPUT ---")

        print("\n(a) Track invalid ID CT9999:")
        track_parcel_details("CT9999")

        print("\n(b) Create delivered parcel CT1002:")

        tid2 = book_parcel("Aman", "Priya", "Delhi")

        for i in range(4):
            update_status(tid2)

        print("\nTrying to update delivered parcel:")
        update_status(tid2)

        # Test Case 4: Different Valid Scenario
        print("\n--- TEST CASE 4: DIFFERENT VALID SCENARIO ---")

        print("\n(a) Update status CT1001:")
        update_status(tid1)

        print("\n(b) Track parcel CT1001:")
        track_parcel_details(tid1)

        print("\nAll four test cases completed successfully.")

    finally:
        parcels = original_parcels
        tracking_counter = original_counter


# 8. Main Menu
def main():

    while True:

        print("\n==============================")
        print("     COURIER TRACKING SYSTEM")
        print("==============================")

        print("1. Book Parcel")
        print("2. Update Status")
        print("3. Track Parcel")
        print("4. Search by Receiver")
        print("5. Run Test Cases")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            book_parcel()

        elif choice == '2':
            update_status()

        elif choice == '3':
            track_parcel_details()

        elif choice == '4':
            search_by_receiver()

        elif choice == '5':
            run_test_cases()

        elif choice == '6':
            print("Exiting Courier Tracking System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Program Execution
if __name__ == "__main__":
    main()