from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ushasri3110"

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default="resident") 
class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="open") 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Signup Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        role = request.form.get("role", "resident")  

        # Password validation
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("signup"))

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please login.", "warning")
            return redirect(url_for("login"))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = User(name=name, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Store user info in session
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_role"] = user.role

            flash(f"Welcome back, {user.name} ({user.role})!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

# Dashboard Route
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        name=session.get("user_name"),
        role=session.get("user_role"),
    )

# Logout Route
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# Complaint Route
@app.route("/complaints", methods=["GET", "POST"])
@app.route("/complaints", methods=["GET", "POST"])
def complaints():
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    role = session["user_role"]

    # Admin: show all complaints
    if role == "admin":
        all_complaints = Complaint.query.order_by(Complaint.created_at.desc()).all()
        return render_template("complaints_admin.html", complaints=all_complaints)

    # Resident: handle complaint submission
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        new_complaint = Complaint(user_id=user_id, title=title, description=description)
        db.session.add(new_complaint)
        db.session.commit()
        flash("Complaint submitted successfully!", "success")
        return redirect(url_for("complaints"))

    # Resident: show their own complaints
    user_complaints = Complaint.query.filter_by(user_id=user_id).order_by(Complaint.created_at.desc()).all()
    return render_template("complaints_resident.html", complaints=user_complaints)

# Admin action to close complaint
@app.route("/complaint/close/<int:id>")
def close_complaint(id):
    if "user_id" not in session or session["user_role"] != "admin":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("login"))

    complaint = Complaint.query.get_or_404(id)
    complaint.status = "closed"
    db.session.commit()
    flash("Complaint closed successfully!", "success")
    return redirect(url_for("complaints"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
