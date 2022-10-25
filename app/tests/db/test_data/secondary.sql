PRAGMA foreign_keys = ON;

INSERT INTO course_learningjourney (learningjourney_id,course_id) VALUES
(1,'COR001'),
(2,'COR002')
;

INSERT INTO course_skill (skill_id,course_id) VALUES
(1,'COR001'),
(2,'SAL003'),
(3,'FIN001'),
(4,'FIN002'),
(6,'MGT001')
;

INSERT INTO jobrole_skill (jobrole_id,skill_id) VALUES
(01,01)
;