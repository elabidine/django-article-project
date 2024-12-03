
# Article and Comment Management System

## Description

This project is a Django-based web application designed to manage articles and user-generated comments. It allows users to create, read, update, and delete articles, as well as post and manage comments on the articles. This system supports user authentication, access control for article management, and an editor interface for managing article content.

The application is structured to provide seamless interactions between authors and readers, with features such as article creation and deletion, as well as comment creation and deletion. It is ideal for content management systems (CMS) where users can publish and interact with articles dynamically.

## Features

- **User Authentication**: Secure login and registration for authors and readers.
- **Article Management**: Authors can create, update, and delete articles.
- **Comment Management**: Users can post comments on articles, and authors can manage those comments.
- **Editor Interface**: Special interface for article creators (authors) to manage their content.
- **Access Control**: Only the authors can edit or delete their articles and comments.

## Installation

To set up the project locally, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/elabidine/django-article-project.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd your-project-name
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to interact with the application.

## Usage

- Visit the home page to view a list of articles.
- Navigate to the article detail pages to view articles and post comments.
- Authors can access the article editor interface to create and manage articles.
- The admin panel allows for further management of users and content at `http://127.0.0.1:8000/admin/`.

## Contributing

If you'd like to contribute to this project, please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.


## Acknowledgements

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Bootstrap: Front-end framework for designing responsive and modern websites.