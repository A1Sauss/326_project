PLEASE SEE *submission_final.pdf* for full document with images

**Title:** A1Sauss 

**Subtitle:** Classdoor

**Semester:** Fall 2018 

**Overview:**
There are many factors which are important when picking a class, and our application aims to simplify searching for courses by creating a platform of aggregate reviews. We choose the name “Classdoor” as an homage to Glassdoor.com, a popular job-search site meant to match people with the “perfect job.” Our platform is built around user reviews, allowing people to get objective opinions about prospective courses. Users can view a star rating, average grades in classes, the title / text of a review as well as keywords or “tags” associated with each class. The motivation behind this was so that users can search for something such as “Easy Bio Gen-Ed” and get results based on a mix of tags and class names. Classdoor is a one stop shop for all students needs when looking for a class. 

**Team Members:**
Nathan Blue
Spencer Rendano
Zander Bobronnikov
Zihang Zhou
Amine Kebichi
Matthew Dahl

**User Interface:**
*Home/Landing Page*: This is the landing page for the app. It allows you to search for classes by name or university

*Login Page*: You can login on this page

*Feed Page*: This is the feed of all courses. You can browse through courses, see featured reviews or even filter(This only currently works if you have all attributes selected)

*Class Page*: This is the page for a specific class. You can view the description, tags that apply, star rating and past reviews. You can also leave a review from this page.

*Review Page*: This is the page where you are able to review a specific class. You are able to rate the class, leave a text review and input the grade you received (anonymously) as well as any tags that apply

*Profile Page*: This page is the user profile. It shows user information as well as recommended classes and past reviews that user has left

**Data Model:**

Class Course has all attributes relating to a course. It connects to class University, class Subject and class Teacher where a course will be classified into different universities, subjects and teachers. The class Reviews is where users can write reviews for courses. Class Tag marks the user and the review that user wrote. Class User stores all personal information of a user and reviews that user has written. 

**URL Routes/Mappings: **
/		Home page - Permission: Open to everyone
/admin		Admin page - Permission: Must log in as an admin to access
/class/<int:id>		Individual class page showing the information and reviews about the class - Permission: Open to everyone
/feed		List of classes and their rating - Permission: Open to everyone
/profile		Profile page of the logged in user with their description - Permission: Must be logged in to see their own profile
/profile/edit		The page to edit the profile information of the logged in user - Permission: Must be logged in as a user to be able to edit their own profile.
/review/<int:id>		Page to review a specific class given by the id - Permission: Must be logged in as a user to be able to write a review for a class
/accounts/login		Page to login as a user - Permission: Open to everyone


**Authentication/Authorization: **
First we have authentication working with the ability for a user to log in and log out at will and while they are logged in they can view their unique profile page with information specifically tailored to them. You can also only leave a review if you are authenticated.

**Team Choice:**
We created search functions for our website where people can search courses by either typing course name or university name or using search bar in the feed page. Typing course name will return all courses that match the criteria from all universities. Typing university name will return all courses a certain university offers. In feed page, there’s a search bar at the top of the page where a user can search a course with more specific criterias. One thing needs to pay attention is that in order to use the search bar, a user must fill out all sections to search.

**Conclusion:**
This project was unlike any other in our college experiences. Normally you will have a project in a class that is a small part of overall theme of the class but to have this be the center focus in this class was awesome! We had to balance out our time throughout the semester and had to stay focused. Some things we learned were mainly centered around web design and how to implement a django framework. The things that we learned were not just specific to creating the best class searching app in the world but were things we could take and implement anywhere for any application. Such as user authentication and data models. 
Some difficulties were getting the pages that needed to dynamically show different things depending on what user was logged in or what class needed to be displayed. We also took a little time to get in the habit of using github correctly. Some things I think we would have liked to known would have been the time commitment for some of the aspects of the project. 
Overall we had such a great time and would not trade this class for anything!  