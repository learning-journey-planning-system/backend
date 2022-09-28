CREATE SCHEMA IF NOT EXISTS G10T3LJPS;

CREATE TABLE course(
Course_ID varchar(20) PRIMARY KEY,
Course_Name varchar(50) not null,
Course_Desc varchar(255),
Course_Status varchar(15), -- Active/Retired
Course_Type varchar(10), -- Internal / External
Course_Category varchar(50), -- Classification
Deleted bool
);

-- ------- INSERT COURSE DB ------ --

INSERT INTO course (Course_ID,Course_Name,Course_Desc,Course_Status,Course_Type,Course_Category,Deleted) VALUES

('FIN-001','Budgeting','Finance Budgeting and Cost Control are important activities for companies and business.','Retired','External','Finance',FALSE),
('FIN-002','Financial Management','Finance Managment are important activities for companies and business.','Active','Internal','Finance',FALSE),
('FIN-003','Acquisition 101','This course introduces students to the legal principles that underlie mergers and acquisitions','Retired','Internal','Finance',FALSE),
('IS-001','Python Basics','Python is an easy to learn, powerful programming language. It has efficient high-level data structures.','Retired','Internal','Technical',FALSE),
('IS-002','HTML & CSS 101','HTML and CSS are the beginning of everything you need to know to make your first web page!','Active','External','Technical',FALSE),
('IS-003','Statistics Essentials','A self-paced course that helps you to understand the various Statistical Techniques from the very basics and how each technique is employed on a real world','Active','Internal','Technical',FALSE),
('BUS-001','Microeconomics','In this course, students will study the price system, market structures, and consumer theory.','Active','Internal','Business',FALSE),
('BUS-002','Strategic Management','The course will cover strategy analysis, formulation of strategies at different levels of the organization, and strategy implementation.','Active','External','Business',FALSE),
('HR-001','Mass Communication','This course is a survey of the history, structure, functions, and responsibilities of mass media','Retired','Internal','HR',FALSE),
('HR-002','Organisational Behaviour','This course provides an overview and analysis of various behavioral concepts affecting human behaviour in business organisations','Active','Internal','HR',FALSE),
('IS-004','SQL Fundamentals','It is a core element of IT infrastructure and is also the key to success for businesses of all shapes and sizes.','Retired','Internal','Technical',FALSE),
('IS-005','Blockchain technology','Distributed Ledger Technology (DLT) is the secret behind the management of Blockchain.','Retired','External','Technical',FALSE),
('FIN-004','Investment Management','Make Smart Investment Decisions in a Global World. Learn how a wealth-generating investment portfolio functions in practice.','Active','Internal','HR',FALSE),
('FIN-005','Portfolio Management','Build a Winning Investment Portfolio. Improve your investment strategies with real-world skills, insights, and analytical tools.','Active','Retired','Finance',FALSE),
('BUS-003','Fundamentals of Marketing','This one-day course aims to provide an understanding of what innovative marketing is all about. ','Active','Internal','HR',FALSE),
('BUS-004','Business Management','This discipline focuses on core business principles and strategies, and is designed to prepare you for a wide range of careers in business and management.','Retired','Internal','Business',FALSE);

-- --------------------------------- --

CREATE TABLE role(
Role_ID int PRIMARY KEY,
Role_Name varchar(20) not null
);

-- ------- INSERT ROLE DB TO BE CONFIRM------ --

INSERT INTO role (Role_ID,Role_Name) VALUES
-- ROLES --
(001,'Admin'),
(002,'User'),
(003,'Manager')
;
-- --------------------------------- --


CREATE TABLE staff(
Staff_ID int not null PRIMARY KEY,
Staff_FName varchar(50) not null,
Staff_LName varchar(50) not null,
Dept varchar(50) not null,
Email varchar(50) not null,
Role int,
password varchar(20) not null,
constraint staff_fk FOREIGN KEY (role) references role(Role_ID));

-- ------- INSERT STAFF DB ------ --
-- 1-Admin, 2-User, 3-Manager

INSERT INTO staff (Staff_ID,Staff_FName,Staff_LName,Dept,Email,Role,password) VALUES
-- Admin & User
(1,'admin','staff','HR','admin@gmail.com',002,'password1') ,
(2,'admin','staff','HR','admin@gmail.com',001,'password2'),

-- Staff
(3,'user','staff','Product','user@gmail.com',002,'password3') ,

-- Manager & User
(4,'manager','staff','Operations','manager@gmail.com',002,'password4'),
(5,'manager','staff','Operations','manager@gmail.com',003,'password5'),

-- -- more test -- -- 
-- Admin & User
(6,'jerry','tom','HR','jerry@gmail.com',002,'password6'),
(7,'jerry','tom','HR','jerry@gmail.com',001,'password7'),

-- Manager & User
(8,'spongebob','sqaurepants','Finance','spongebob@gmail.com',002,'password8'),
(9,'spongebob','sqaurepants','Finance','spongebob@gmail.com',003,'password9')
;

-- --------------------------------- --

CREATE TABLE registration(
Reg_ID int not null PRIMARY KEY,
Course_ID varchar(20) not null,
Staff_ID int not null,
Reg_Status varchar(20) not null,
Completion_Status varchar(20) not null,
constraint registration_fk1 FOREIGN KEY (Course_ID) references course(Course_ID),
constraint registration_fk2 FOREIGN KEY (Staff_ID) references staff(Staff_ID)
);

-- ------- INSERT REGISTRATION DB ------ --

INSERT INTO registration (Reg_ID,Course_ID,Staff_ID,Reg_Status,Completion_Status) VALUES
(101, 'FIN-003', 1,'Registered','Completed'), 
(102, 'IS-002', 1,'Registered','In Progress'), 

(103, 'IS-003', 4,'Rejected','Not Completed'), 


(104, 'IS-002', 3,'Waitlist','Not Completed'),  
(105, 'IS-003', 3, 'Registered','Completed')
;

-- --------------------------------- --

CREATE TABLE job_role(
JobRole_ID int PRIMARY KEY,
JobRole_Name varchar(20) not null,
Deleted bool
);

-- ------- INSERT JOBROLE DB ------ --
INSERT INTO job_role (JobRole_ID,JobRole_Name,Deleted) VALUES
(01,'Operations Executive',FALSE),
(02,'Business Analyst',FALSE),
(03,'CEO',FALSE),
(04,'COO',FALSE),
(05,'Software Engineering',FALSE),
(06,'Product Manager',FALSE),
(07,'Accountant',FALSE),
(08,'Human Resource',FALSE),
(09,'Business Admin',FALSE),
(10,'PR Executive',FALSE)
;

-- --------------------------------- --


CREATE TABLE learning_journey(
LJ_ID varchar(20) PRIMARY KEY,
Staff_ID int not null,
JobRole_ID int not null,
constraint learning_journey_fk1 FOREIGN KEY (Staff_ID) references staff(Staff_ID),
constraint learning_journey_fk2 FOREIGN KEY (JobRole_ID) references job_role(JobRole_ID)
);


-- ------- INSERT LEARNING JOURNEY DB TO BE CONFIRM------ --

INSERT INTO learning_journey (LJ_ID,Staff_ID,JobRole_ID) VALUES
(201,1,01),
(202,1,02),
(203,4,05),
(204,3,10),
(205,3,09)

;

-- --------------------------------- --


CREATE TABLE selection(
LJ_ID varchar(20),
Course_ID varchar(20),
constraint selection_pk PRIMARY KEY (LJ_ID, Course_ID),
constraint selection_fk1 FOREIGN KEY (LJ_ID) references learning_journey(LJ_ID),
constraint selection_fk2 FOREIGN KEY (Course_ID) references course(Course_ID)
);

-- ------- INSERT SELECTION DB ------ --

INSERT INTO selection (LJ_ID,Course_ID) VALUES
(201,'FIN-003'),
(201,'FIN-002'),

(202,'IS-002'),
(202,'FIN-002'),

(203,'IS-003'),

(204,'IS-002'),

(205,'IS-003')
;

-- --------------------------------- --



CREATE TABLE skill(
Skill_ID varchar(20) PRIMARY KEY,
Skill_Name varchar(50),
Deleted bool
);

-- ------- INSERT SELECTION DB ------ --

INSERT INTO skill (Skill_ID,Skill_Name,Deleted) VALUES
('SK-01','Web Design',FALSE),
('SK-02','Marketing',FALSE),
('SK-03','Analysis',FALSE),
('SK-04','Accounting',FALSE),
('SK-05','Statistics',FALSE),
('SK-06','Recruiting',FALSE),
('SK-07','Communication',FALSE),
('SK-08','Planning',FALSE),
('SK-09','Administration',FALSE),
('SK-10','Programming',FALSE)
;
-- --------------------------------- --


CREATE TABLE jobroleskill(
JobRole_ID int,
Skill_ID varchar(20),
constraint roleskill_fk1 FOREIGN KEY (JobRole_ID) references job_role(JobRole_ID),
constraint roleskill_fk2 FOREIGN KEY (Skill_ID) references skill(Skill_ID),
constraint roleskill_pk PRIMARY KEY (JobRole_ID, Skill_ID)
);

-- ------- INSERT ROLESKILL DB ------ --

INSERT INTO jobroleskill (JobRole_ID,Skill_ID) VALUES
(01,'SK-08'),
(01,'SK-05'),

(02,'SK-03'),
(02,'SK-05'),


(03,'SK-09'),


(04,'SK-08'),
(04,'SK-05'),


(05,'SK-10'),

(06,'SK-08'),

(07,'SK-04'),

(08,'SK-06'),

(09,'SK-09'),

(10,'SK-07');
-- --------------------------------- --


CREATE TABLE courseskill(
Skill_ID varchar(20),
Course_ID varchar(20),
constraint courseskill_pk PRIMARY KEY (Skill_ID, Course_ID),
constraint courseskill_fk1 FOREIGN KEY (Skill_ID) references skill(Skill_ID),
constraint courseskill_fk2 FOREIGN KEY (Course_ID) references course(Course_ID)
);

-- ------- INSERT COURSESKILL DB ------ --

INSERT INTO courseskill (Skill_ID,Course_ID) VALUES
('SK-01','IS-001'),
('SK-01','IS-002'),


('SK-02','HR-002'),
('SK-02','FIN-003'),

('SK-03','HR-002'),
('SK-03','IS-003'),

('SK-04','FIN-002'),
('SK-04','FIN-001'),

('SK-05','IS-003'),

('SK-06','BUS-001'),

('SK-07','HR-001'),

('SK-08','BUS-002'),


('SK-09','IS-003'),
('SK-10','IS-002')
;
-- --------------------------------- --