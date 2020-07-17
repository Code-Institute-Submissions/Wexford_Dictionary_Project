# *Wexford Slang Dictionary*
## MilestoneProject3 - Data Centric Development Milestone Project


Application Demo [Wexford Slang Dictionary](https://wexforddictionaryproject.herokuapp.com/)

## Table Of Contents
1. [Description](#Description)
2. [UX](#UX)
3. [UserStories](#UserStories)
4. [Wireframes](#Wireframes)
5. [Features](#Features)
6. [FutureFeatures](#FutureFeatures)
7. [Pages](#Pages)
8. [Testing](#Testing)
9. [Deployment](#Deployment)
10. [Technologies](#Technologies)
11. [ViewProject](#ViewProject)
12. [Acknowledgements](#Acknowledgements)
13. [Disclaimer](#Disclaimer)


## Description

This application is designed to allow its users to create, view, edit and delete slang/jargon and on a smaller scale than sites like urban dictionary.
The application will store slang/jargon the users create and display these in accordion style lists for other users to view and add their own definitions.
During the testing phase of this application I have found many users enjoying the definitions and prompting an "All Ireland Slang Dictionary".


## UX

The site has been designed with minimalism in mind, to allow users of all ages and levels of computer literacy to enjoy. The site also represents the Wexford County colours purple and gold. The UI is easy to navigate and users can view, add and edit slang words with ease. 
During my research of jargon glossaries I found out that by adding images/photos to slang dictionaries you open up pathways to online bullying so I took the decision to leave the site as text and colours only.


## UserStories

- Users will be able to View Slang Words to the site
- Users will be able to Add Slang Words to the site
- Users will be able to Edit Slang words on the site
- Users will be able to Delete Slang words off the site
- Users will be able to browse through all existing Slang words
- Users will be able to apply a filter to make searching through slang words easier
- Users will be able to register themselves as a user with some additional metadata for future use
- Users will be able to log on and usernames will be stores for future use when developing the site further
- Users will be able to easily click and view the Slang descriptions without being redirected to another screen
- Users will be able to easily click and view the Slang names without being redirected to another screen
- Users will be able to easily click and view the Slang examples without being redirected to another screen
- Users will be able to log out of the site


## Wireframes

1. Registration Desktop Screen [here](libraries/wireframes/registerdesktop.JPG)
2. Registration Mobile Screen [here](libraries/wireframes/registermobile.JPG)
3. Login Desktop Screen [here](libraries/wireframes/logindesktop.JPG)
4. Login Mobile Screen [here](libraries/wireframes/loginmobile.JPG)
5. Add/Edit Slang Desktop Screen [here](libraries/wireframes/addeditslangdesktop.JPG)
6. Add/Edit Slang Mobile Screen [here](libraries/wireframes/addeditslangmobile.JPG)
7. Browse Desktop Screen [here](libraries/wireframes/browsedesktop.JPG)
8. Browse Mobile Screen [here](libraries/wireframes/browsemobile.JPG)
9. Home Desktop Screen [here](libraries/wireframes/homedesktop.JPG)
10. Home Mobile Screen [here](libraries/wireframes/homemobile.JPG)



## Features

- User Registration: allows users to register themselves on the site
- User Login: allows users to log on to the site 
- View Slang: allows users to view the slang on the site
- Add Slang: allows users to add their own slang to the site
- Edit Slang: allows users to edit slang on the site
- Delete Slang: allows users to delete slang on the site
- Browse Slang: allows users to browse slang on the site
- Filter Slang: allows users to filter through the different categories of slang words on the site
- User logout: allows users to logout of the site



## Future Features

Unfortunately my work life was heavily impacted by Covid19 during the course of this project and my worklife balance was greatly affected. 
As a result I did not get the same amount of time as past projects to implement a lot of the features I would have liked. 
The below are features I would like to include in the future:

- Pagination
- Search based on full / partial name
- Search based on description full/partial
- Views/Likes Functionality
- Analytics on most upvoted & from what countries
- Analytics on most views & from what countries
- Count Page visits
- Errors when incorrect/blank usernames are added
- Add ownership & usernames to each of the added slang Words
- Add an administrative section to approve submitted slang words before being displayed.
- Smoother refreshing when filtering categories

## Pages

1. addslangwords.html: screen to add slangs to mongoDB and display them on screen
2. base.html: contains NAV bars, Block content and relevant JS
3. editslangwords.html: screen to edit slangs in mongoDB and display the changes on screen
4. home.html: main drop page, greets user with options
5. login.html: Login page & allows user to click and register
6. register.html: Register page & allows users to click and login
7. slangs.html: browse the list of slang words on the site


## Testing

Test | Outcome
------------ | -------------
W3C HTML validation for addslangwords.html | Passed - Errors only on python elements
W3C HTML validation for base.html| Passed - Errors only on python elements
W3C HTML validation for editslangwords.html | Passed - Errors only on python elements
W3C HTML validation for home.html | Passed - Errors only on python elements
W3C HTML validation for login.html | Passed - Errors only on python elements
W3C HTML validation for register.html | Passed - Errors only on python elements
W3C HTML validation for slangs.html | Passed - Errors only on python elements
W3C CSS validation for All | Passed
JSHint Javascript Test | Passed
Chrome developer tools (debugging and responsiveness testing -including all devices available) | Passed
Samsung A50 | Passed - some forms were not clicking/tapping properly on mobile devices when testing from github - problem resolved when app tested through Heroku deployment
Iphone 7 | Passed - some forms were not clicking/tapping properly on mobile devices when testing from github - problem resolved when app tested through Heroku deployment
Iphone X | Passed - some forms were not clicking/tapping properly on mobile devices when testing from github - problem resolved when app tested through Heroku deployment
Friends & Family Testing | Passed - Family & Friend suggested enhancements to develop further to an All Ireland App but enjoyed the concept of the Wexford Slang Dictionary
Responsive Design| Passed
Githubs Debug Log | Passed


Browser Test | Outcome
------------ | -------------
 Chrome | Passed
 Edge/IE | Passed
 Firefox | Passed
 Opera | Passed
 Safari | Passed



 On Screen Tests | Outcome
------------ | -------------
 Home screen | Passed
 Home screen (add slang) | Passed
 Home screen (browse all) | Passed
 Home screen (hyperlinks) | Passed
 Browse screen | Passed
 Browse screen (refresh list) | Passed
 Browse screen (filter) | Passed
 Browse screen (delete) | Passed
 Browse screen (edit) | Passed
 Browse screen (expand) | Passed
 Browse screen (hyperlinks) | Passed
 Add Slang | Passed
 Add Slang (select category) | Passed
 Add Slang (required slang word) | Passed
 Add Slang (description) | Passed
 Add Slang (example) | Passed
 Add Slang (submit) | Passed
 Add Slang (hyperlinks) | Passed
 Edit Slang | Passed
 Edit Slang (select category) | Passed
 Edit Slang (required slang word) | Passed
 Edit Slang (description) | Passed
 Edit Slang (example) | Passed
 Edit Slang (submit) | Passed
 Edit Slang (hyperlinks) | Passed
 Delete Slang | Passed
 Logout | Passed
 Login screen | Passed
 Login screen (username required & feedback) | Passed
 Login screen (register redirect) | Passed
 Login screen (submit) | Passed
 Register screen | Passed



## Deployment

GitHub was used to develop the project, store code in the repository and maintain the version control of this project. 
The live demo has been deployed using Heroku and all versions pushed to the master branch on github are automatically deployed the Heroku Master.

The following steps were used to deploy the Wexford Slang Dictionary on Heroku:

1. Created an App Name
2. Logged into Heroku using $ heroku login creating a connection between Github and the Heroku application
3. Checked Heroku Apps to make sure my project was available
4. Created a new Git repository using git init
5. Added my files to the repositary and associated my Heroku application as my master branch(remote master branch)
6. Created my requirements.txt file
7. Created my ProcFile
8. Added both files to github and pushed to Heroku Master
9. Ran my application using $ heroke ps:scale web=1 to scale dynos
10. Logged into Heroku and set up the Config Variables in the settings > config variables section (IP & PORT)
11. Application Deployed
12. The link generated can be used instantly. The link generated for this site as: https://wexforddictionaryproject.herokuapp.com/
13. I connected my Heroku App to github to automatically deploy from the master branch, I managed the build through github then would test the app through heroku every few commits/pushes. 


N.B. my application was failing in Heroku due to an error in my requirements.txt file not finding PyMongo. Troubleshooted many issues using the Heroku logs functionality which was very useful in locating the error. 

## Technologies

The project is built using Python, HTML, CSS and Jquery as its main components.

The following are the other Technologies used throughout the build process:
* [JQuery](https://jquery.com)
    - Used to create more robust functionalities in forms and filters 
* [Materialize](https://materializecss.com/)
    - Used for developing a modern responsive front-end framework based on Material Design
* [Material Icons](https://material.io/resources/icons/?style=baseline)
    - Used for useful icons to provide more intuitive UI.
* [GitHub](https://github.com/)
    - Used to develop, store and share code & Pushed to Heroku master.
* [Balsamiq](https://balsamiq.com/)
    - Used to create the original wireframes for the project.
* [Dev Tools](https://www.google.com/chrome/)
    - Used continuously when building the application & debugging any HTML, CSS & JS issues.
* [CSS Validator](https://jigsaw.w3.org/css-validator/validator)
    - Used to validate CSS code.
* [HTML Validator](https://validator.w3.org/)
    - Used to validate HTML code.
* [Javascript Validator](https://jshint.com/)
    - Used to validate Javascript code.
* [MongoDB](https://www.mongodb.com/)
    - Used to create the database for CRUD operations
* [Heroku](https://dashboard.heroku.com/apps)
    - Used to build, run, and operate my application
* [Flask](https://dashboard.heroku.com/apps)
    - Provided useful tools and features making the application more resourceful e.g. flash messaging


## View Project

* The code used to develop this slang dictionary application can be viewed [here](https://github.com/Murphj99/Wexford_Dictionary_Project)
* The live version of the application was deployed using [Heroku](https://dashboard.heroku.com/apps/wexforddictionaryproject) and can be viewed here [WexfordDictionary](https://wexforddictionaryproject.herokuapp.com/)


## Acknowledgements
* I got the idea to create a Jargon/Slang Dictionary application from [Code Institute](https://www.codeinstitute.net).


## Disclaimer
* This project was created for educational purposes only.