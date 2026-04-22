# =========================
# Pharmacy Management System
# =========================

# ----------- Data Storage -----------
users = {"customer1": "pass123"}
medicines = {
    1: {"name": "Paracetamol", "price": 10, "quantity": 50},
    2: {"name": "Ibuprofen", "price": 15, "quantity": 30}
}
orders = []
notifications = []
bills = []


# ----------- Authentication Module -----------
def login(username, password):
    if username in users and users[username] == password:
        return True
    return False


# ----------- Inventory Module -----------
def check_availability(medicine_id, quantity):
    if medicine_id in medicines:
        return medicines[medicine_id]["quantity"] >= quantity
    return False


def update_stock(medicine_id, quantity):
    if medicine_id in medicines:
        medicines[medicine_id]["quantity"] -= quantity
        return True
    return False


# ----------- Prescription Module -----------
def verify_prescription(required):
    if not required:
        return True
    # Simulated verification
    return True


# ----------- Order Module -----------
def create_order(user, medicine_id, quantity, prescription_required):
    if not check_availability(medicine_id, quantity):
        return "Medicine not available"

    if not verify_prescription(prescription_required):
        return "Prescription invalid"

    update_stock(medicine_id, quantity)

    order = {
        "user": user,
        "medicine": medicines[medicine_id]["name"],
        "quantity": quantity,
        "status": "Processed"
    }

    orders.append(order)
    send_notification(user, "Order processed successfully")

    bill = generate_bill(medicine_id, quantity)
    return order, bill

# ----------- Billing Module -----------
def generate_bill(medicine_id, quantity):
    total = medicines[medicine_id]["price"] * quantity
    bill = {"medicine": medicines[medicine_id]["name"], "total": total}
    bills.append(bill)
    return bill


# ----------- Notification Module -----------
def send_notification(user, message):
    notifications.append({"user": user, "message": message})


# ----------- Sample Run -----------
if __name__ == "__main__":
    if login("customer1", "pass123"):
        order, bill = create_order("customer1", 1, 2, True)
        print("Order:", order)
        print("Bill:", bill)
    else:
        print("Login Failed")