


INSERT INTO staff (id,staff_fname,staff_lname,dept,email,role_id) VALUES
(1,'admin','staff','HR','admin@gmail.com',002),
(2,'admin','staff','HR','admin@gmail.com',001),
(3,'user','staff','Product','user@gmail.com',002),
(4,'manager','staff','Operations','manager@gmail.com',002),
(5,'manager','staff','Operations','manager@gmail.com',003),
(6,'jerry','tom','HR','jerry@gmail.com',002),
(7,'jerry','tom','HR','jerry@gmail.com',001),
(8,'spongebob','sqaurepants','Finance','spongebob@gmail.com',002),
(9,'spongebob','sqaurepants','Finance','spongebob@gmail.com',003);

INSERT INTO jobrole (id,jobrole_name,deleted) VALUES
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


INSERT INTO course (id,course_name,course_desc,course_status,course_type,course_category) VALUES

('FIN-001','Budgeting','Finance Budgeting and Cost Control are important activities for companies and business.','Retired','External','Finance'),
('FIN-002','Financial Management','Finance Managment are important activities for companies and business.','Active','Internal','Finance'),
('FIN-003','Acquisition 101','This course introduces students to the legal principles that underlie mergers and acquisitions','Retired','Internal','Finance'),
('IS-001','Python Basics','Python is an easy to learn, powerful programming language. It has efficient high-level data structures.','Retired','Internal','Technical'),
('IS-002','HTML & CSS 101','HTML and CSS are the beginning of everything you need to know to make your first web page!','Active','External','Technical'),
('IS-003','Statistics Essentials','A self-paced course that helps you to understand the various Statistical Techniques from the very basics and how each technique is employed on a real world','Active','Internal','Technical'),
('BUS-001','Microeconomics','In this course, students will study the price system, market structures, and consumer theory.','Active','Internal','Business'),
('BUS-002','Strategic Management','The course will cover strategy analysis, formulation of strategies at different levels of the organization, and strategy implementation.','Active','External','Business'),
('HR-001','Mass Communication','This course is a survey of the history, structure, functions, and responsibilities of mass media','Retired','Internal','HR'),
('HR-002','Organisational Behaviour','This course provides an overview and analysis of various behavioral concepts affecting human behaviour in business organisations','Active','Internal','HR'),
('IS-004','SQL Fundamentals','It is a core element of IT infrastructure and is also the key to success for businesses of all shapes and sizes.','Retired','Internal','Technical'),
('IS-005','Blockchain technology','Distributed Ledger Technology (DLT) is the secret behind the management of Blockchain.','Retired','External','Technical'),
('FIN-004','Investment Management','Make Smart Investment Decisions in a Global World. Learn how a wealth-generating investment portfolio functions in practice.','Active','Internal','HR'),
('FIN-005','Portfolio Management','Build a Winning Investment Portfolio. Improve your investment strategies with real-world skills, insights, and analytical tools.','Active','Retired','Finance'),
('BUS-003','Fundamentals of Marketing','This one-day course aims to provide an understanding of what innovative marketing is all about. ','Active','Internal','HR'),
('BUS-004','Business Management','This discipline focuses on core business principles and strategies, and is designed to prepare you for a wide range of careers in business and management.','Retired','Internal','Business');

INSERT INTO skill (id,skill_name,deleted) VALUES
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

INSERT INTO registration (id,course_id,staff_id,reg_status,completion_status) VALUES
(100001, 'FIN-003', 1,'Registered','Completed'), 
(100002, 'IS-002', 1,'Registered','In Progress'), 
(100003, 'IS-003', 4,'Rejected','Not Completed'), 
(100004, 'IS-002', 3,'Waitlist','Not Completed'),  
(100005, 'IS-003', 3, 'Registered','Completed')
;

INSERT INTO learningjourney (id,staff_id,jobrole_id) VALUES
(201,1,01),
(202,1,02),
(203,4,05),
(204,3,10),
(205,3,09);

INSERT INTO course_learningjourney (learningjourney_id,course_id) VALUES
(201,'FIN-003'),
(201,'FIN-002'),
(202,'IS-002'),
(202,'FIN-002'),
(203,'IS-003'),
(204,'IS-002'),
(205,'IS-003')
;


INSERT INTO course_skill (skill_id,course_id) VALUES
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

INSERT INTO jobrole_skill (jobrole_id,skill_id) VALUES
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