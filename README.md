
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
   
### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Basic knowledge of the command line.


To set up the project locally, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/elabidine/django-article-project.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd django-article-project
   ```

3. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build -d
   ```
4. **Apply migrations**:
   Once the containers are running, open a new terminal and run:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application**:
   - Open your browser and navigate to: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Local Development Setup (Optional)

If you prefer not to use Docker, you can set up the project manually:

1. Install Python.

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   ```bash
   python manage.py runserver
   ```

---

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