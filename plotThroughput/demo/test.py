import sys

def hello(a,b):
    print 'hello and thats your sum:'
    sum=a+b
    print sum

if __name__ == "__main__":
    hello(int(sys.argv[1]), int(sys.argv[2]))
