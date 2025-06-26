# Cinema Management System

Cinema is a Django-based platform for running a movie theater. It provides administrative tools for managing movies and screenings while allowing customers to book tickets online and track their loyalty points.

## Features for Administrators
- Manage movies, halls, sessions and tickets through the Django admin interface
- View sales analytics with charts and KPI metrics
- Export analytics data to PDF or Excel
- Control user accounts and reviews

## Features for Users
- Browse the movie catalogue and session schedule
- Book seats and purchase tickets using bonus points
- Store favorites and leave reviews
- Download purchased tickets as PDF with QR codes
- Maintain profile information and view bonus history in a personal dashboard

## Repository Layout
The main Django project is under the `cinema_project/` directory:

```
cinema_project/
├── manage.py
├── cinema/              # Main app with models, views and templates
├── cinema_project/      # Project settings
├── static/              # Static assets
├── media/               # Uploaded content
├── requirements.txt
└── README.md            # Details on setup and running the project
```

## 📦 Installation

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Further Setup

### Configure environment variables
Create a `.env` file next to `manage.py` and specify values for the settings used in
`cinema_project/settings.py`:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your_database
DB_USER=db_user
DB_PASSWORD=db_password
# Optional overrides
DB_HOST=localhost
DB_PORT=3306
```

These variables can also be exported in your shell environment. They are loaded
via `python-decouple` when Django starts.

### Run migrations
After installing the requirements, apply database migrations with:

```bash
python manage.py migrate
```

### Start the development server
Launch the local server using:

```bash
python manage.py runserver
```

## 🧪 Sample Admin Login

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📈 Analytics & Reports

Sales data can be accessed by administrators. The analytics dashboard provides:

* Movie-based KPIs
* Revenue breakdown per session/hall
* Export to PDF or Excel


## 🧪 Sample Data

> Demo data is not included in the repo but can be prepared on request.

## 🛠️ Technologies Used

| Category | Stack                                   |
| -------- | --------------------------------------- |
| Backend  | Django 4.x, Python 3.10+                |
| Database | SQLite / MySQL / PostgreSQL             |
| Frontend | Django Templates + Bootstrap (optional) |
| Exports  | ReportLab (PDF), OpenPyXL (Excel)       |
| Auth     | Django default auth + Superusers        |

## 🚫 Known Limitations

* No payment integration (e.g., Stripe/PayPal)
* PDF export assumes default page format

## 💬 Contact

For questions or contributions, contact [nonamemars777@gmail.com](mailto:nonamemars777@gmail.com) or open an issue.
