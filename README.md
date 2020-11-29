
#### Awwards

#### A Django CRUD web app that rates projects.
#### Landing Page
Currently deployed at heroku and working.

![alt text](app.png)

#### Mobile support
The WebApp is compatible with devices of all sizes and all OS's, and consistent improvements are being made.



#### Get Live link here : [USAGE](https://jumaawardsapp.herokuapp.com/)

## Description
This web app  allows users to submit their websites or projects and have them reviewed based on design,usability and content.Users has the ability to rate other peoples projects.




## Running the process
* . myvirtual/bin/activate
* To open local server run python3 manage.py runserver
* To run the test,run python manage.py test Awwards

## User Story
         As a user, you can:
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View your profile page

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/HASSAN1A/Awwards.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Awwards
  pip install -r requirements.txt
  ```
3. Set up your database
    ```bash
    psql
    ```
4. Running the application
  ```bash
  python manage.py runserver
  ```
5. Testing the application
  ```bash
  python manage.py test pics
  ```
Open the application on your browser `127.0.0.1:8000`.


## Behavior Driven Development

| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |
|User visits and clicks submit button            | User wants to submit a site             | Site is uploaded and displays the site on the site homepage     |
| Then click on the website image           | User wants to view the website descriptions | Website descriptions are displayed         |
| User hovers on website image and click rate button                  | User wants to rate a project  |  User is redirect to site and rate form shown |
| User clicks profile button | User wants to view their profile  | User is redirected to my profile page |
| User clicks edit profile button  | User wants to update their profile   |  Update profile modal pop up to edit profile details |
| User navigate to api endpoints provided below | User wants to use awwards api | List reesources according to endpoint accessed |

## Features

Here are the summary:

- A landing page showing users and their prifile pictures.
- Clickable users which direct the user to a page with their highlights from the particular post.


## Requirements

- This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)

##### Contribution

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request




## API-Endpoints
* https://jumaawardsapp.herokuapp.com//api/profiles  -  List profiles registered with awwards
* https://jumaawardsapp.herokuapp.com//api/projects  -  Returns information pertaining to all the projects posted in awwards

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)


## Installation and Set-up
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`https://github.com/HASSAN1A/Awwards.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and  create a virtual environment. Run the following commands respectively:
    * **`python3.8 -m venv --without-pip virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** :  Download the latest version of pip in virtual our environment.   
    * **`curl https://bootstrap.pypa.io/get-pip.py | python`**  

* **Step 5** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 6** : Create the Database
    * - psql
    * - CREATE DATABASE awwards;
* **Step 7** : .env file
    * Create .env file and paste paste the following filling where appropriate:

    * - SECRET_KEY = '<Secret_key>'
    * - DBNAME = '<DB_NAME>'
    * - USER = '<USER_>'
    * - PASSWORD = '<Password>'
    * - DEBUG = True
* **Step 8** : Run initial Migration
    * python3 manage.py makemigrations
    * python3 manage.py migrate
* **Step 10** : Create admin credentials
    * python3 manage.py createsuperuser
  
* **Step 11** : Run application
    * python3 manage.py runserver
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:8000/**.


### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/HASSAN1A/Awwards/issues/new) by including your search query and the expected result.
If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/HASSAN1A/Awwards). Please include sample queries and their corresponding results.

## Built with

1. [Python 3.8.5](https://www.python.org/doc/) : Programming language.
2. [Django; Python framework used.](https://flask.palletsprojects.com/en/1.1.x/):Framework used.
3. [HTML](https://www.w3schools.com/html/) : Layout.
4. [CSS](https://www.w3schools.com/css/) : Styling.
5. [Bootstrap](https://mdbootstrap.com/) : For responsive websites.
6. [posgreSQL](https://www.postgresql.org/) : Database language.
7. [psycopg2](https://pypi.org/project/psycopg2/) : Database driver.
8. [Javascript](https://www.w3schools.com/js/DEFAULT.asp) : often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.[7] JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.
9. [Google Font API](https://dillinger.io/fonts.google.com) : For prettier fonts Making the web more beautiful, fast, and open through great typography..
10. [Quotes Api](http://quotes.stormconsultancy.co.uk/random.json) : For requesting
11. [Font Awesome](fontawesome.com) : The world's most popular and easiest to use icon set just got an upgrade. More icons. More styles.
12. [jQuery 3](https://jquery.com/) : For special effects.
13. [Figma](https://www.figma.com/file/iTndFXbWHuGkZ1ak60bXr2h/Awwards?node-id=0%3A1) - Blueprint for designing the web app.

## TEAM

[Hassan Juma ](https://github.com/HASSAN1A)



## [License](https://github.com/HASSAN1A/Awwards/blob/master/LICENSE.md)

[MIT](https://github.com/HASSAN1A/Awwards/blob/master/LICENSE.md) © [Hassan Juma](https://github.com/HASSAN1A)
