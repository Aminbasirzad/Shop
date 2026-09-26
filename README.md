# 🛒 Shop

A modern e-commerce website built with Django, designed for selling digital products such as smartphones and laptops.

This project was developed as a Django portfolio project to demonstrate practical skills in building a complete e-commerce application.

## ✨ Features

* 🔐 User registration and login
* 🛡️ CAPTCHA protection
* 🛍️ Product listing and product details
* 🛒 Shopping cart
* ➕➖ Cart quantity management
* 💰 Product discounts and final price calculation
* 📦 Checkout and order creation
* 🧾 Order management
* 💳 Mock payment system
* ✅ Successful payment simulation
* ❌ Failed payment simulation
* 🔄 Retry failed payments
* 📩 Contact form
* 👤 Support for authenticated users and guest orders

## 🛠️ Technologies

* Python
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite
* Django Templates
* django-simple-captcha

## 💳 Payment System

This project uses a Mock Payment system instead of a real payment gateway.

The payment flow is:

text
Checkout
   ↓
Create Order
   ↓
Pending Payment
   ↓
Mock Payment
   ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Success         Failed
 │               │
 ▼               ▼
Paid            Failed
 │
 ▼
Clear Cart


No real financial transaction is performed.

## 🚀 Installation

Clone the repository:

bash
git clone https://github.com/Aminbasirzad/Shop.git
cd Shop


Create a virtual environment:

bash
python -m venv venv


Activate it on Windows:

bash
venv\Scripts\activate


Install the dependencies:

bash
pip install -r requirements.txt


Run migrations:

bash
python manage.py migrate


Start the development server:

bash
python manage.py runserver


Open the project in your browser:

text
http://127.0.0.1:8000/


## 📌 Project Status

Completed ✅

This project was created as a portfolio project to practice and demonstrate Django web development skills.

## 👨‍💻 Author

Amin Basirzad

GitHub: [Aminbasirzad](https://github.com/Aminbasirzad)