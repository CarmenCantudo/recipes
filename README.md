# Fill your belly, feed your soul

![Responsive web image](assets/testing/am-i-responsive.png)

The Live Website can be accessed [HERE!](https://fillyourbelly.herokuapp.com/)

This is a recipe website that is open to everyone who loves cooking and wants to explore new recipes. The site’s main purpose is to allow users to browse and view recipes whether they are registered or not. Registered users can also add, update and delete their own recipes on the app, like or dislike recipes, and leave comments that can be updated or deleted by the user.




## Table of Contents
- [Fill your belly, feed your soul](#fill-your-belly-feed-your-soul)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Home Page](#home-page)
      - [Recipes Page](#recipes-page)
      - [Add Recipes Page](#add-recipes-page)
      - [Recipe Details Page](#recipe-details-page)
      - [Edit Recipe Page](#edit-recipe-page)
      - [Delete Recipe Page](#delete-recipe-page)
      - [Admin Control](#admin-control)
    - [Future Features](#future-features)
  - [UX](#ux)
    - [Site Purpose](#site-purpose)
    - [Agile Methodology](#agile-methodology)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Flow Diagram](#flow-diagram)
  - [Testing](#testing)
    - [Bugs Fixed](#bugs-fixed)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
    - [Using Heroku](#using-heroku)
    - [How to Fork it](#how-to-fork-it)
    - [How to Clone it](#how-to-clone-it)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)
  - [Gitpod Reminders](#gitpod-reminders)
  - [Release History](#release-history)
  - [FAQ about the uptime script](#faq-about-the-uptime-script)


## Features
### Existing Features
#### Home Page

![Home page](static/testing/home.png)

#### Recipes Page

![Recipe page](static/testing/recipes.png)

#### Add Recipes Page

![Add Recipe](static/testing/add_recipe.png)

#### Recipe Details Page

![Recipe Detail](static/testing/recipe_detail.png)

#### Edit Recipe Page

![Edit Recipe](static/testing/edit_recipe.png)

#### Delete Recipe Page

![Delete Recipe](static/testing/delete_recipe.png)


<details>
  <summary>#### Comments section</summary>

![Comment section](static/testing/comments.png)

- Leave a comment

![Leave a comment](static/testing/leave_comment.png)

- Comment Approval

![Comment approval](static/testing/comment_approval.png)

- Edit Comment Page

![Edit Comment](static/testing/edit_comment.png)

- Delete Comment Page

![Delete Comment](static/testing/delete_comment.png)

</details>



<details>
  <summary>#### User Account Pages</summary>

- Register page

![Register page](static/testing/register.png)

- Login page
  
![Login page](static/testing/login.png)

- Logout page

![Logout page](static/testing/logout.png)

</details>

#### Admin Control

![Admin Control page](static/testing/admin.png)


[Back to top](#fill-your-belly-feed-your-soul)

### Future Features

- 
- 

[Back to top](#fill-your-belly-feed-your-soul)

## UX
### Site Purpose
- To make the app user-friendly and aesthetically pleasing while still meeting the needs of the user. 
- The app is designed for anyone who enjoys cooking and wants to find recipes and cooking tips.
- To have a website where you can view recipes and choose one to cook.
- To make sure that everyone who visits our website finds recipes they'll love, so we've put together a list of great food-related ideas.
- This app allows you to create, update, and delete your recipes.
- To allow users to approve, update and delete their recipes.
- To give the admin user the power to approve, update, and delete recipes.
- To respond to user inputs and actions in a clear and accurate way.


### Agile Methodology

The Agile Methodology was used to plan and manage this project. Issues were created on Github so that tasks could be assigned and prioritised usign the Project Board. A User Story was created for each task, with specific requirements and deadlines.

### User Stories

- USER STORY: View recipe list
  
  As a Site User I can view a list of recipes so that I can select one to read.

- USER STORY: Manage recipes
  
  As a Site User / Admin I can create, read, update and delete recipes so that I can manage recipes.

- USER STORY: Likes
  
  As a Site User / Admin I can like / unlike recipes so that anybody can see which is the most popular.

- USER STORY: Update / Delete Comments
  
  As a Site User I can update and delete comments on a recipe so that I can edit or remove any comments I've posted

- USER STORY: View / Leave Comments
  
  As a Site User I can view and leave comments on a recipe so that I can learn more about the recipe and participate in the conversation.

- USER STORY: Account Registration / Login
  
  As a Site User I can register and log into an account so that I can add recipes, comment on them and like them.

- USER STORY: Create drafts
  
  As a Site User I can create draft recipes so that I can finish writing the content later.

- USER STORY: Open a recipe
  
  As a Site User I can open a recipe so that I can read the recipe's steps, ingredients and comments.

- USER STORY: Search recipes
  
  As a Site User I can search for recipes so that I can select one to read.

- USER STORY: Site pagination

  As a Site User I can view a paginated list of recipes so that I can easily select a recipe to view.


[Back to top](#fill-your-belly-feed-your-soul)

## Design

### Flow Diagram

![Flow diagram](static/testing/Database_ER_diagram.jpeg)

The flow chart above, created with the website [Lucidchart](https://lucid.app/), provides a simplified overview of what I was trying to accomplish.

## Testing

- The application was constantly tested during development.
- To validate the code, the [PEP8 online validation tool](http://pep8online.com/) was used.
- Lighthouse was used to test the app for Performance, Accessibility and Best Practices:
  
  ![Lighthouse Performance](assets/testing/lighthouse.png)


### Bugs Fixed
During the creation of the while loops with the nested if statements, I had some problems and had to research and learn how to use it properly making each if, elif, else break or call the right function to continue with the next part of the story.


[Back to top](#fill-your-belly-feed-your-soul)

## Technologies Used

- HTML: Used to structure all the templates on the site.
- CSS: To provide extra styling to the site.
- Python: To provide the functionality to the site. Packages used in the project can be found in requirements.txt.
- Django: Python framework used in the project.
- Javascript: Minimum javascript was used to fade out alerts.
- Bootstrap 4: To create layouts and styles for the website.
- [GitHub](https://github.com/): Used to store my repository for submission.
- [Gitpod](https://gitpod.io/): Used to develop the application.
- GitBash: Used to push the repository to Github.
- [Heroku](https://www.heroku.com/): Used to deploy the website.
- [ElephantSQL](https://www.elephantsql.com/): Used for the database during development and deployment.
- [Cloudinary](https://cloudinary.com/): To host Static files for the site.
- [Lucidchart](https://www.lucidchart.com/): Used to make a flow diagram to help with the logic & flow of the code.
- [Balsamiq](https://balsamiq.com/): To create wireframes for the project.
- [Am I Responsive?](https://ui.dev/amiresponsive): To ensure the project looked good across all devices.
- [Favicon](https://favicon.io/favicon-converter/) - To create the favicon icon.


[Back to top](#fill-your-belly-feed-your-soul)

## Deployment

### Using Heroku
1. Use [Heroku](https://www.heroku.com/) to create a new app.
2. In Settings, add two buildpacks in the following order:
   - Python
   - NodeJS
3. Link the new app to the appropriate repository after granting Heroku access to GitHub.
4. Make the decision to enable Automatic Deploys or not. If enabled, each push to GitHub will result in an automatic update of the deployed app.
5. Click Deploy.

### How to Fork it
1. On GitHub, go to [CarmenCantudo/recipes]( https://github.com/CarmenCantudo/recipes).
2. In the top right, click "Fork".

### How to Clone it
1. Go to the main page of the repository.
3. Above the file list, click "Code".
4. Select HTTPS, SSH, or GitHub CLI and then click copy to clone it.
5. Open Git Bash.
6. Change the location of your cloned repository.
7. Type `git clone` and then paste the URL you copied.
8. Press “Enter” to create your clone.

### Making a Local Clone
1. Locate the [Repository]( https://github.com/CarmenCantudo/recipes).
2. Click "Code".
3. Click Clone or Download.
4. Copy the Git URL from the dialogue box.
5. Open a terminal window in your choosen directory using your preferred development editor.
6. Change the location to where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL you copied.
8. Press Enter, and your local clone will be created.

[Back to top](#fill-your-belly-feed-your-soul)

## Credits

Resources used in the process of the "Lost Dragon's Quest" website design and build:
- [Create A Simple Django Blog | Codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
- [ASCII Generator](https://ascii-generator.site/)
- [StackOverFlow](https://stackoverflow.com/): Help with general questions
- I think therefore I blog Code Institute project.
- [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) provided by Code Institute

[Back to top](#fill-your-belly-feed-your-soul)




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Carmen,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
