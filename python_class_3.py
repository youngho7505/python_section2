import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수
class wareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        wareHouse.stock_num += 1

    def __del__(self):
        wareHouse.stock_num -= 1

user1 = wareHouse("kim")
user2 = wareHouse("lee")

print(wareHouse.__dict__)
print(user1.__dict__)
print(user2.__dict__)

print(user1.name)
print(user2.name)

print(wareHouse.stock_num)
print(user1.stock_num)  #인스턴스의 네임스페이스 (x) -> 클래스의 네임스페이스, 클래스 변수는 각 인스턴스에 공유
print(user2.stock_num)

user1.__del__()
print(wareHouse.stock_num)