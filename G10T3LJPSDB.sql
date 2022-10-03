

INSERT INTO role (id,role_name) VALUES
(001,'Admin'),
(002,'User'),
(003,'Manager');

INSERT INTO staff (id,staff_fname,staff_lname,dept,email,role_id,password) VALUES
(1,'admin','staff','HR','admin@gmail.com',002,'password1') ,
(2,'admin','staff','HR','admin@gmail.com',001,'password2'),
(3,'user','staff','Product','user@gmail.com',002,'password3') ,
(4,'manager','staff','Operations','manager@gmail.com',002,'password4'),
(5,'manager','staff','Operations','manager@gmail.com',003,'password5'),
(6,'jerry','tom','HR','jerry@gmail.com',002,'password6'),
(7,'jerry','tom','HR','jerry@gmail.com',001,'password7'),
(8,'spongebob','sqaurepants','Finance','spongebob@gmail.com',002,'password8'),
(9,'spongebob','sqaurepants','Finance','spongebob@gmail.com',003,'password9');


INSERT INTO course (id,course_name,course_desc,course_status,course_type,course_category) VALUES

(1,'Budgeting','Finance Budgeting and Cost Control are important activities for companies and business.','Retired','External','Finance'),
(2,'Financial Management','Finance Managment are important activities for companies and business.','Active','Internal','Finance'),
(3,'Acquisition 101','This course introduces students to the legal principles that underlie mergers and acquisitions','Retired','Internal','Finance'),
(4,'Python Basics','Python is an easy to learn, powerful programming language. It has efficient high-level data structures.','Retired','Internal','Technical'),
(5,'HTML & CSS 101','HTML and CSS are the beginning of everything you need to know to make your first web page!','Active','External','Technical'),
(6,'Statistics Essentials','A self-paced course that helps you to understand the various Statistical Techniques from the very basics and how each technique is employed on a real world','Active','Internal','Technical'),
(7,'Microeconomics','In this course, students will study the price system, market structures, and consumer theory.','Active','Internal','Business'),
(8,'Strategic Management','The course will cover strategy analysis, formulation of strategies at different levels of the organization, and strategy implementation.','Active','External','Business'),
(9,'Mass Communication','This course is a survey of the history, structure, functions, and responsibilities of mass media','Retired','Internal','HR'),
(10,'Organisational Behaviour','This course provides an overview and analysis of various behavioral concepts affecting human behaviour in business organisations','Active','Internal','HR'),
(11,'SQL Fundamentals','It is a core element of IT infrastructure and is also the key to success for businesses of all shapes and sizes.','Retired','Internal','Technical'),
(12,'Blockchain technology','Distributed Ledger Technology (DLT) is the secret behind the management of Blockchain.','Retired','External','Technical'),
(13,'Investment Management','Make Smart Investment Decisions in a Global World. Learn how a wealth-generating investment portfolio functions in practice.','Active','Internal','HR'),
(14,'Portfolio Management','Build a Winning Investment Portfolio. Improve your investment strategies with real-world skills, insights, and analytical tools.','Active','Retired','Finance'),
(15,'Fundamentals of Marketing','This one-day course aims to provide an understanding of what innovative marketing is all about. ','Active','Internal','HR'),
(16,'Business Management','This discipline focuses on core business principles and strategies, and is designed to prepare you for a wide range of careers in business and management.','Retired','Internal','Business');


INSERT INTO skill (Skill_ID,Skill_Name,Deleted) VALUES
(1,'Web Design',FALSE),
(2,'Marketing',FALSE),
(3,'Analysis',FALSE),
(4,'Accounting',FALSE),
(5,'Statistics',FALSE),
(6,'Recruiting',FALSE),
(7,'Communication',FALSE),
(8,'Planning',FALSE),
(9,'Administration',FALSE),
(10,'Programming',FALSE)
;