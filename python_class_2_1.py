import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class selfTest:
    def function1():
        print("function1 Called!")

    def function2(self):
        print("function2 Called!")

f = selfTest()

print(dir(f))

selfTest.function1()
f.function2()


