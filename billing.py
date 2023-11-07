#Irfan Salahuddin
# 10/30/23

# billing.py

from datetime import datetime

def display_bill(id, s_in_state, c_rosters, c_hours):
    # Tuition rates
    in_state_rate = 225.00  # per credit hour
    out_of_state_rate = 850.00  # per credit hour

    # Check if the student is in-state or out-of-state
    is_in_state = s_in_state.get(id, False)

    # Get the current date and time
    current_datetime = datetime.now().strftime("%b %d, %Y at %I:%M %p")

    print("Tuition Summary")
    print(f"Student: {id}, {'In-State' if is_in_state else 'Out-of-State'} Student")
    print(current_datetime)
    print("Course    Hours    Cost")
    print("------    -----    -----")

    total_cost = 0.0

    # Iterate through the courses to calculate and display the bill
    for course, hours in c_hours.items():
        # Calculate the course cost
        if is_in_state:
            course_cost = hours * in_state_rate
        else:
            course_cost = hours * out_of_state_rate

        # Update the total cost
        total_cost += course_cost

        # Display the course cost with aligned decimal points
        print(f"{course}        {hours}        ${course_cost:6.2f}")

    print("        -------    -------")
    print(f"Total        {sum(c_hours.values())}        ${total_cost:6.2f}")

# Example usage
if __name__ == "__main__":
    student_id = "1001"
    in_state_students = {
        "1001": True,
        "1002": False,
        "1003": True,
        "1004": False,
        "1005": False,
        "1006": True
    }
    course_hours = {
        "CSC101": 3,
        "CSC102": 4,
        "CSC103": 5,
        "CSC104": 3,
        "CSC105": 2
    }
    course_roster = {
        "CSC101": ["1004", "1003"],
        "CSC102": ["1001"],
        "CSC103": ["1002"],
        "CSC104": [],
        "CSC105": ["1005", "1002"]
    }
    display_bill(student_id, in_state_students, course_roster, course_hours)