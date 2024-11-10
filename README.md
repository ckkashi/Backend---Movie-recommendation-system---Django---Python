
# 🎬 Movie Recommendation System Backend - Django & Python

This project is a backend API service for a movie recommendation system, built with Django and Python. It provides various endpoints for user authentication, movie data retrieval, and favorite list management. The data is stored in a JSON file containing a list of movies.

## 🌟 Features

- **User Authentication**:
  - **Register**: Create a new user account.
  - **Login**: Authenticate existing users.

- **Movie APIs**:
  - **All Movies**: Retrieve the complete list of movies.
  - **Get Movie by ID**: Fetch specific movie details by movie ID.

- **Favorites**:
  - **Save Favorite Movie**: Users can add movies to their favorites list.
  - **Get User Favorites**: Retrieve a list of a user's favorite movies.

## 📂 Project Structure

```
backend-movie-recommendation/
├── data/
│   └── movies.json         # JSON file containing movie data
├── app/
│   ├── models.py           # Database models
│   ├── views.py            # API endpoints logic
│   ├── serializers.py      # Serializers for data formatting
│   └── urls.py             # URL routing for APIs
└── manage.py               # Django project management script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ckkashi/Backend---Movie-recommendation-system---Django---Python.git
   cd Backend---Movie-recommendation-system---Django---Python
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### API Endpoints

| Endpoint                    | Method | Description                   |
|-----------------------------|--------|-------------------------------|
| `/register`                 | POST   | Register a new user           |
| `/login`                    | POST   | User login                    |
| `/getMovies`                | GET    | Get all movies                |
| `/getMovieById?movie_id=1`  | GET    | Get movie by ID               |
| `/getFavMovies`             | GET    | Get user favorite movies      |
| `/addFavMovie`              | POST   | Add movie to user favorites   |

## 💻 Usage

To access the endpoints, use a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/). 

- **Register** a user to create an account.
- **Login** with your credentials to receive an authentication token.
- Use the token to access movie data and manage your favorites list.

## 📈 Future Enhancements

- Implement recommendation algorithms to suggest similar movies.
- Add additional filters and search functionality for movies.
- Enable pagination for large datasets.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or find bugs.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
