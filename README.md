﻿# Look For Samples

This repository is for Look For Samples, allowing users to be recommended tracks based on their liking history.

The application was created using Flask and SQLite, and recommends tracks to users using content-based recommendation.

## Installation

Run all commands from the root directory

1. Clone this repository:

```sh
git clone https://github.com/musa-q/Music-Sample-Tinder.git
```

2. Create a virtual environment and activate it

```sh
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

4. Add the file `.env` to the `./app` folder, and populate the following variables:
(Visit [Discogs](https://www.discogs.com/developers) to get the relevant data)
    * `DISCOGS_CONSUMER_KEY`
    * `DISCOGS_CONSUMER_SECRET`
    * `DISCOGS_USER_AGENT=MusicTinderApp/0.1`

5. [Setup the database](#database)

6. Once the database has been popualted. You can run the Flask app using

```sh
python wsgi.py
```

7. Open your web browser and navigate to <http://localhost:5000>. You will be able to access the site through other devices by navigating to `http://{ip address}:5000`.

## Usage

To use the application, simply begin clicking the `Like` or `Dislike` buttons (or swiping left or right) and the application will recommend new songs.

There is also an option to `Skip` tracks, if needed (such as if a YouTube video is not working).

## Database

Use the following steps to set up the database:

1. Set-up the database

```sh
python .\app\__init__.py -s
```

2. Populate the database

```sh
python .\app\__init__.py -p
```

You can specify different parameters for which pages to extract data, for example:

```sh
python .\app\__init__.py -p -sp 5 -ep 10
```

Where `-sp` is the start page and `-ep` is the end page

### Commands

Use the following command for a list of all commands:

```sh
python .\app\__init__.py --help
```
