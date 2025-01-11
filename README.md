

# 🛍️ **Django Marketplace Website**

🎯 A dynamic and scalable online marketplace built with **Django**, **HTML**, and **CSS**, designed to facilitate seamless buying and selling of products like hoodies 🧥, PlayStation 🎮, and more!

---

## 🚀 **Key Features**

- 🔑 **User Authentication:** Secure signup and login system  
- 📊 **Dashboard Management:** Intuitive dashboards for managing products and orders  
- 🛍️ **Product Listings:** Easy product creation, updating, and deletion  
- 💬 **Inbox Messaging:** Direct communication between buyers and sellers  
- 🔍 **Search and Filters:** Streamlined product search and categorization  

---

## 🏗️ **Project Structure**

```plaintext
Market-place/
├── dashboard/              # Handles user dashboards and management views
├── item/                    # App managing product listings and categories
│   ├── migrations/          # Database migrations for product models
│   ├── templates/           # Product page templates
│   └── models.py            # Product database models
├── media/                   # Stores uploaded item images
│   └── item_images/         # Directory for product images
├── sell/                    # Core Django application for the marketplace
│   ├── static/              # CSS, JavaScript, and static files
│   ├── templates/           # HTML templates for views
│   ├── __init__.py          # App initialization
│   ├── asgi.py              # ASGI configuration
│   ├── settings.py          # Application settings
│   ├── urls.py              # URL routing
│   ├── views.py             # View functions for the main site
│   └── wsgi.py              # WSGI configuration
├── staticfiles/             # Static file storage
├── db.sqlite3               # SQLite database for storing data
├── manage.py                # Django management script
└── requirements.txt         # Dependencies for the project
```

---

## ⚙️ **Getting Started**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Yabiti/Market-place.git
cd Market-place
```

### 2️⃣ **Set Up a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### 3️⃣ **Install Required Packages**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Apply Database Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Create a Superuser (Optional for Admin Access)**
```bash
python manage.py createsuperuser
```

### 6️⃣ **Run the Development Server**
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to explore your website 🌐.

---



## 🎯 **Future Enhancements**

- 📱 **Mobile-Friendly Design:** Improved responsiveness for mobile devices  
- 🔔 **Real-Time Notifications:** Instant alerts for user activities  
- 🤖 **AI Product Recommendations:** Personalized suggestions for users  
- 📢 **Social Media Sharing:** Share products directly from the platform  

---

## 🤝 **Contributing**

Contributions are welcome! Fork this repo and submit a pull request for any improvements or suggestions.

---

## 📜 **License**

This project is licensed under the MIT License.

