#!/usr/bin/env python

from user import User
knowledge =[]
class Student(User):
    def __init__(self, first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge = knowledge

    
    def learn(self,new_knowledge):
        self.knowledge.append(new_knowledge)
