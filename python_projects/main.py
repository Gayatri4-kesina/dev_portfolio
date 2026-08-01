"""class LinuxUser:
 def __init__(self):
    self.__username=None
    self.__uid=None
    self.__groups=None

 @property
 def username(self):
    return self.__username
 @property
 def groups(self):
    return self.__groups
 @property
 def uid(self):
    return self.__uid


 def is_valid_uid(self,uid):
  return isinstance(uid,int) and uid >= 0


 def add_users(self,username,uid,groups):
    if not self.is_valid_uid(uid):
        raise ValueError(f"Enter valid UID. Should be greater than zero")
    self.__username=username
    self.__uid=uid
    self.__groups=groups

 def add_groups(self,g_name):
   self.__groups.append(g_name)

 def rm_groups(self,group):
   if group in self.__groups:
      self.__groups.remove(group)
   else:
      print(f"group '{group} doesn't exist")

 def info(self):
   print(self.__username)
   print(self.__uid)
   print(self.__groups)

 def __str__(self):
   return f"user:{self.__username},uid:{self.__uid},groups:{self.__groups}"


user1=LinuxUser()
print(user1)
"""

class LinuxUser:
    def __init__(self):
        self.__username = None
        self.__uid = None
        self.__groups = None

    @property
    def username(self):
        return self.__username

    @property
    def groups(self):
        return self.__groups

    @property
    def uid(self):
        return self.__uid

    def is_valid_uid(self, uid):
        return isinstance(uid, int) and uid >= 0

    def add_users(self, username, uid, groups):
        if not self.is_valid_uid(uid):
            raise ValueError(f"Enter valid UID. Should be greater than zero")
        self.__username = username
        self.__uid = uid
        self.__groups = groups

    def add_groups(self, g_name):
        self.__groups.append(g_name)

    def rm_groups(self, group):
        if group in self.__groups:
            self.__groups.remove(group)
        else:
            print(f"group '{group}' doesn't exist")

    def __str__(self):
        return f"user:{self.__username},uid:{self.__uid},groups:{self.__groups}"
