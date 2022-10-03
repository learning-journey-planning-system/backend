

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

