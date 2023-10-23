# CRUDCo URL Shortener

## Requirements

- Users can submit a long URL.
- URLs are saved in a database.
- Unique IDs are generated for each URL.
- The short url is available via a list when a user logs in.

## Tech Stack

- PostgresSQL : Database
- Django + Django REST Framework + SimpleJWT : Backend
- React : Frontend

## Workflow

### Frontend
- User submits URL
- URL is shortened (How? What library?)
- Long and Short URL are saved with User ID associated
- User gets a list of URL Titles with link to short ver.

#### UI

- Require: Title and URL
- Optional: Short URL (limited characters), generated automatically if not provided


### Backend

- Short version is send to the API
    - API takes ID of short ver to find long ver
    - Site is redirected to the long URL after clicking the short URL link
  


## Data Models

### Tables

- Users
    - ID -> Primary Key (auto generated)
    - Username
    - Password
    - Token

- URLs
    - ID -> Primary Key (auto generated)
    - Title
    - Long URLs
    - Short Urls
    - User ID -> Foreign Key!

### Relationship

URLs (many) -> Users (one)

