# Kashta Knowledge Base

Kashta Knowledge Base is a web application for tech enthusiasts to explore various topics, read articles, and stay updated with the latest in technology.

## Features

- Browse latest topics and most viewed articles.
- Detailed view for each article.
- Search functionality to find specific articles.
- Responsive design for seamless use on different devices.

## Technologies Used

- Python
- Django
- Bootstrap
- SQLite
- ckediter

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/kashta.git
    cd kashta
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your web browser and go to `http://localhost:8000`.

## Project Structure

- `home`: Contains views for the home page and article details.
- `models.py`: Defines the database models for topics and articles.
- `templates`: Contains HTML templates for rendering the pages.
- `static`: Contains static files like CSS, JS, and images.

## Views and Templates

- **home**: Displays latest topics and most viewed articles.
- **article_detail**: Displays detailed information about a specific article.
- **article_list**: Displays a list of articles under a specific topic.
- **search**: Displays search results based on user queries.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

For any questions or suggestions, please contact [ahmedaltaif79@gmail.com](mailto:ahmedaltaif79@gmail.com).
