# Book-Catalog-Generator

A Django web application to manage and generate a catalog of books. Users can add, edit, and delete books, as well as view their personal book catalog with a modern, responsive interface.

## Features

- User authentication and profile management
- Add, edit, and delete books
- Responsive UI with light/dark mode toggle
- Secure forms with CSRF protection
- SQLite database for easy setup

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Book-Catalog-Generator.git
   cd Book-Catalog-Generator
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
Book-Catalog-Generator/
├── catalog_generator/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   └── templates/
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

## Usage

- Register or log in to your account.
- Add new books using the form on your profile page.
- Edit or delete existing books.
- Toggle between light and dark mode for a comfortable viewing experience.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/)