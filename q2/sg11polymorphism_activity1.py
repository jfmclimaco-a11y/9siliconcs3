class Patient:
    # Parent class for patients
    def __init__(self, name, bill_amount):
        # initializes patient attributes
        self.__name = name
        # stores private name attribute
        self.__bill_amount = bill_amount
        # stores private bill amount attribute

    def get_name(self):
        # getter method for name
        return self.__name
        # returns the patient's name

    def set_name(self, name):
        # setter method for name
        self.__name = name
        # updates the patient's name

    def get_bill_amount(self):
        # getter method for bill amount
        return self.__bill_amount
        # returns the original bill amount

    def set_bill_amount(self, bill_amount):
        # setter method for bill amount
        self.__bill_amount = bill_amount
        # updates the bill amount

    def calculate_bill(self):
        # default method to calculate bill
        return self.__bill_amount
        # returns the full bill with no discount

    def display_patient_type(self):
        # default method to display patient type
        print("Patient Type: Regular Patient")
        # prints regular patient text


class SeniorPatient(Patient):
    # Child class for senior citizens
    def calculate_bill(self):
        # overrides calculate_bill for seniors
        return self.get_bill_amount() * 0.80
        # returns bill with 20% discount

    def display_patient_type(self):
        # overrides display_patient_type for seniors
        print("Patient Type: Senior Citizen")
        # prints senior citizen text


class PhilHealthPatient(Patient):
    # Child class for PhilHealth members
    def calculate_bill(self):
        # overrides calculate_bill for PhilHealth
        return self.get_bill_amount() * 0.85
        # Return bill with 15% discount

    def display_patient_type(self):
        # overrides display_patient_type for PhilHealth
        print("Patient Type: PhilHealth Member")
        # prints PhilHealth member text


regular_patient = Patient("Juan Dela Cruz", 15000)
# creates a regular patient object
senior_patient = SeniorPatient("Maria Santos", 15000)
# creates a senior patient object
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)
# creates a PhilHealth patient object

patients = [regular_patient, senior_patient, philhealth_patient]
# puts all patient objects in a list

print("Hospital Billing System\n")
# prints the system title
for patient in patients:
    # loops through each patient in the list
    print("Patient Name:", patient.get_name())
    # prints the patient's name
    patient.display_patient_type()
    # calls display_patient_type method
    print(f"Original Bill: P{patient.get_bill_amount():,.2f}")
    # prints the formatted original bill
    print(f"Final Bill: P{patient.calculate_bill():,.2f}\n")
    # prints the formatted final bill
