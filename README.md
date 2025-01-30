# Scalpels and Hooks
#### Video Demo: https://www.youtube.com/watch?v=rr6QduXeu90
## Description:
Scalpels and Hooks is the name of my crochet business. The website is meant to showcase my work as well as let users buy the products. The website was made using HTML, CSS, Javascript, Flask and Jinja.

### static:
In the static folder, I added an /images folder where I stored all the images which would be required throught the website.

#### script.js:
This file has the Javascript code for having text appear while hovering over an image, and also for redirecting to another page on clicking on an image. Initially I was planning to display the image details next to each image, but then decided on adding the hover effect to make it look less cluttered and more dynamic. I added event listeners for the same.

#### styles.css:
This file has the CSS code for styling the website. I added a background to make it more personalised based on the theme of the website, which is crochet. I wanted a more artistic font, and hence I chose Lucida Handwriting and Papyrus. The colors for hovering text were also chosen based on the background, so that the text is clearly visible.

### app.py:
This file contains the python code for all the routes in the website. I have imported certain functions from cs50, flask, flask_session, werkzeug.security and functools. I have created a SQL database called crochet.db, where I have inserted two tables- users and orders. The difference routes which can be taken are index, amigurumi, decor, buy, login, register, logout, edit, orders and users. Login is required for the buy, edit and logout routes. Logging in from the admin account is required for orders and users routes.

#### /index:
This takes the user to the homepage.

#### /amigurumi:
This takes the user to the page showing the amigurumi items.

#### /decor:
This takes the user to the page showing the decor items.

#### /buy:
This takes the user to the buy page. It ensures all the required items are submitted, and adds the responses to the SQL table orders.

#### /login:
This takes the user to the login page. It ensures all fields are entered, the usernames and passwords match the profile of a registered user. Then it stores the session_id so that the user does not have to keep logging in.

#### /register:
This takes the user to the register page. It ensures all fields are entered, the username is unique and the password and confirmation match. It then creates a hash of the entered password and stores the details in the SQL table called users.

#### /logout:
This clears the session and redirects the user to the homepage.

#### /edit:
This lets the user change their password. It verifies that the current password entered is correct, ensures that the new password and confirmation match, and then changes the values in the SQL table users.

#### /orders:
This goes to the orders page only if the admin in logged in. It gets the orders data from the SQL table orders and displays it.

Scalpels and Hooks is the name of my crochet business. The website is meant to showcase my work as well as let users buy the products. The website was made using HTML, CSS, Javascript, Flask and Jinja.

### static:
In the static folder, I added an /images folder where I stored all the images which would be required throught the website.

#### script.js:
This file has the Javascript code for having text appear while hovering over an image, and also for redirecting to another page on clicking on an image. Initially I was planning to display the image details next to each image, but then decided on adding the hover effect to make it look less cluttered and more dynamic. I added event listeners for the same.

#### styles.css:
This file has the CSS code for styling the website. I added a background to make it more personalised based on the theme of the website, which is crochet. I wanted a more artistic font, and hence I chose Lucida Handwriting and Papyrus. The colors for hovering text were also chosen based on the background, so that the text is clearly visible.

### app.py:
This file contains the python code for all the routes in the website. I have imported certain functions from cs50, flask, flask_session, werkzeug.security and functools. I have created a SQL database called crochet.db, where I have inserted two tables- users and orders. The difference routes which can be taken are index, amigurumi, decor, buy, login, register, logout, edit, orders and users. Login is required for the buy, edit and logout routes. Logging in from the admin account is required for orders and users routes.
#### /index:
This takes the user to the homepage.
#### /amigurumi:
This takes the user to the page showing the amigurumi items.
#### /decor:
This takes the user to the page showing the decor items.
#### /buy:
This takes the user to the buy page. It ensures all the required items are submitted, and adds the responses to the SQL table orders.
#### /login:
This takes the user to the login page. It ensures all fields are entered, the usernames and passwords match the profile of a registered user. Then it stores the session_id so that the user does not have to keep logging in.
#### /register:
This takes the user to the register page. It ensures all fields are entered, the username is unique and the password and confirmation match. It then creates a hash of the entered password and stores the details in the SQL table called users.
#### /logout:
This clears the session and redirects the user to the homepage.
#### /edit:
This lets the user change their password. It verifies that the current password entered is correct, ensures that the new password and confirmation match, and then changes the values in the SQL table users.
#### /orders:
This goes to the orders page only if the admin in logged in. It gets the orders data from the SQL table orders and displays it.
#### /users:
This goes to the users page only if the admin in logged in. It gets the users data from the SQL table users and displays it.

### layout.html:
This file is the basic layout common to all the other routes, which extend this layout with added components. I have added the name of the business on top along with a logo to the left of it. There's a navigation bar below, the components of which change depending on whether the user is logged in or logged out. There is also Jinja code added to show flash messages below the page.

### amigurumi.html:
This file shows a catalogue of amigurumi items which I have made. It is completely made of images, with added elements for hover and click. The click option takes the user to the 'buy' route.

### decor.html:
This file shows a catalogue of decor items which I have made. It is completely made of images, with added elements for hover and click. The click option takes the user to the 'buy' route.

### buy.html:
This file contains a form which lets users place orders. There is a dropdown to choose between amigurumi and decor, and based on the chosen element the second dropdown gets populated and an option can be chosen. The user then has to select the quantity and press the button. Initially I was planning to just keep a text box for users to enter the name of the product, but that could lead to spelling mistakes and I would be expecting the users to type the entire names. For dropdown also, I was thinking of going with only one dropdown with everything, but the segregation made sense to make it more user-friendly. Once the user submits the form, the details are entered into a SQL database.

### login.html:
This file contains a form which enables the user to log in. It requires an username and password.

### orders.html:
This file creates a page which displays a table showing the orders, with three columns - username, product and quantity.

### register.html:
This file contains a form which enables the user to register. It requires username, password and password confirmation.

### users.html:
This file creates a page which displays a table showing the users, with two columns - user ID and username#### /users:
This goes to the users page only if the admin in logged in. It gets the users data from the SQL table users and displays it.

### layout.html:
This file is the basic layout common to all the other routes, which extend this layout with added components. I have added the name of the business on top along with a logo to the left of it. There's a navigation bar below, the components of which change depending on whether the user is logged in or logged out. There is also Jinja code added to show flash messages below the page.

### amigurumi.html:
This file shows a catalogue of amigurumi items which I have made. It is completely made of images, with added elements for hover and click. The click option takes the user to the 'buy' route.

### decor.html:
This file shows a catalogue of decor items which I have made. It is completely made of images, with added elements for hover and click. The click option takes the user to the 'buy' route.

### buy.html:
This file contains a form which lets users place orders. There is a dropdown to choose between amigurumi and decor, and based on the chosen element the second dropdown gets populated and an option can be chosen. The user then has to select the quantity and press the button. Initially I was planning to just keep a text box for users to enter the name of the product, but that could lead to spelling mistakes and I would be expecting the users to type the entire names. For dropdown also, I was thinking of going with only one dropdown with everything, but the segregation made sense to make it more user-friendly. Once the user submits the form, the details are entered into a SQL database.

### login.html:
This file contains a form which enables the user to log in. It requires an username and password.

### orders.html:
This file creates a page which displays a table showing the orders, with three columns - username, product and quantity.

### register.html:
This file contains a form which enables the user to register. It requires username, password and password confirmation.

### users.html:
This file creates a page which displays a table showing the users, with two columns - user ID and username
