

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