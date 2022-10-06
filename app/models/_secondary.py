from sqlalchemy import Table, Column, ForeignKey, String, Integer
from app.db.base_class import Base

course_skill = Table('course_skill', Base.metadata,
    Column('skill_id', String(20),ForeignKey("skill.id"), primary_key=True),
    Column('course_id', String(20), ForeignKey("course.id"), primary_key=True)
)

jobrole_skill = Table('jobrole_skill', Base.metadata,
    Column('jobrole_id', Integer, ForeignKey("jobrole.id"), primary_key=True),
    Column('skill_id', String(20), ForeignKey("skill.id"), primary_key=True)
)

course_learningjourney = Table('course_learningjourney', Base.metadata,
    Column('learningjourney_id', Integer, ForeignKey("learningjourney.id"), primary_key=True),
    Column('course_id', String(20), ForeignKey("course.id"), primary_key=True)
)
