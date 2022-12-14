# pyGym

A full stack flask application to manage bookings for a gym.

- [The Project Brief](#the-project-brief)
  * [MVP](#mvp)
  * [Extensions](#extensions)
- [Project Restrictions](#project-restrictions)
- [Video Walkthrough](#video-walkthrough)
- [Planning](#planning)
  * [Diagrams](#diagrams)
  * [User Experience](#user-experience)
- [Lessons Learned](#lessons-learned)
- [Run Locally](#run-locally)
- [What's Next?](#what-s-next-)

 <br>

## The Project Brief
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

### MVP
The brief mandated the following minimum functionality:
- create and edit Members and Sessions
- book members on specific Sessions
- show a list of all upcoming Sessions
- show all members that are booked in for a particular Session

### Extensions
For this project's extensions, I decided to focus on infrastructure and building for future extensibility by implementing more classes and many-to-many database relationships:

- create and edit Staff Members, Rooms and Session Categories
- associate Sessions with a single Session Category 
- associate Staff Members and Rooms with multiple Session Categories
- assign and reassign suitable Staff Members and Rooms to individual Sessions.
- sessions have a max capacity and members can only be added if space available.
- members can have standard or premium membership

 <br>

## Project Restrictions

The project had to be built using  the following technologies:

- ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Use of following was not permitted:
- Javascript
- Use of Object Relational Mapping (eg ActiveRecord)
- Pre-built CSS Libraries (eg Bootstrap)
- Authentication

 <br>

## Video Walkthrough

https://user-images.githubusercontent.com/9053731/210601605-bdaa53e8-82b3-43d0-9959-12d164f791c8.mp4

 <br>

## Planning

As project time was limited to 6 days and I knew that my objectives were ambitious, I decided to take time to plan carefully!

### Diagrams

I created a [Class Diagram](/readme_imgs/classdiagram.png) as well as some Object Diagrams, which helped me to better visualise how different parts of the app would interact and how a database might be structured.    The diagrams also helped me plan my work, and I created a [Kanban style board](/readme_imgs/kanban.png) on Notion to keep organised.

### User Experience

I also drew up a basic [User Profile](/readme_imgs/persona.png), [User Sitemap](/readme_imgs/sitemap.png) and [User Needs Table](/readme_imgs/needstable.png), leading to the following design priorities:

- Functionality and reliability
- Accessibility
- Clarity of UI over fancy styling
- Likely primary use will be on PC, but should be fully responsive for future expansion or IT Failure.

Before I began building, I created some [wireframe/prototypes on Figma](/readme_imgs/wireframes), to give me something to work towards and allow me to add some basic styling as I went along.

 <br>


## Lessons Learned

- Consolidated learning from first weeks of CodeClan, especially CRUD and Many-to-Many database relationships.
- Visual Studio Code debugger is the best thing ever.
- Planning and UX consideration before starting is 100% worth it.
- Styling always takes longer than you think it will!
- 6 days is not much time and time flies when you are having fun! 

 <br>


## Run Locally

To run the project locally, you'll need Python3, PostgresSQL and Flask installed.

Run the following commands to create the database, seed with sample data and start the app:

```
createdb pyGym
psql -d pyGym -f db/pyGym.sql
python3 console.py
flask run
```

You can then visit http://127.0.0.1:4999/ to view the app and try it out!

<br>

 ## What's Next?

This repo is essentially in the same state as the project was presented after the initial 6 day period.  I plan to make a new repo, and work further on the project in future to practice my Flask/Python skills.  When I do, I will add a link here!

 <br>

