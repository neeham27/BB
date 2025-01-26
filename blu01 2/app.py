from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the login page
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

# Route for the registration page
@app.route("/register")
def register():
    return render_template("register.html")

# Route for the reservation page
@app.route("/reserve", methods=["GET", "POST"])
def reserve():
    if request.method == "POST":
        # Handle seat reservation logic here
        data = request.form
        return jsonify({"message": "Reservation successful!"})
    return render_template("reserve.html")

# Route for the employee dashboard
@app.route("/dashboard")
def dashboard():
    # Replace with real data from your database
    bookings = [{"date": "2025-01-01", "time": "12:00 PM", "seat": "2-seater"}]
    return render_template("dashboard.html", bookings=bookings)

# Route for the manager dashboard
@app.route("/manager_dashboard")
def manager_dashboard():
    # Replace with real analytics data
    analytics = {
        "total_fee": 5000,
        "employee_bookings": [{"employee": "John Doe", "bookings": 3}]
    }
    return render_template("manager_dashboard.html", analytics=analytics)

# Route for the confirmation page
@app.route("/confirmation/<reservation_id>")
def confirmation(reservation_id):
    # Replace with real reservation details
    return render_template("confirmation.html", reservation_id=reservation_id)

if __name__ == "__main__":
    app.run(debug=True)
