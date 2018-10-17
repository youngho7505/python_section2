import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class userInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------------")
        print(self.name)
        print(self.phone)
        print("------------------")

    def __del__(self):
        print("Deleted!")


user1 = userInfo("kim", "010-4389-2505")
user2 = userInfo("park", "019-732-4994")

print(id(user1))
print(id(user2))

#user1.set_info("kim", "010-4389-2505")
#user2.set_info("park", "019-732-4994")

user1.print_info()
user2.print_info()


print(user1.__dict__)
print(user2.__dict__)

print(user1.name, user1.phone)
print(user2.name, user2.phone)

