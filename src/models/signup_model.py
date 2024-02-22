'''
Author: Karen Vardanian (vkaren1777@icloud.com)
File Created: Thursday, 22nd February 2024 10:02:07 pm
Copyright © 2024 - Karen Vardanian
'''


from pydantic import BaseModel

class SignupModel(BaseModel):
    username: str
    password: str