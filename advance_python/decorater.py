# Create a decorator that counts how many times a function has been called and prints the count.

def counter(fun):
    fun.count=0
    def wrapp(*args, **kwargs):
        print("running!!")
        fun.count+=1
        print(fun.count)      
        fun(*args, **kwargs)
        print("ended")
    return wrapp
        
@counter
def callfun():
    print(f"hrllo mehtab khan")
callfun()
callfun()
callfun()
