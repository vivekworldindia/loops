# print("meow")
# print("meow")
# print("meow")

# while loops
# i = 0
# while i <3:
#     print("meow")
#     i += 1 

# for and list uses
# for i in [0,1,2]:

# range function 

# for _ in range(10):
#     print("meow")
    
    # 
# print("meow\n"*3 ,end="")


# while true function 

# while True :
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


# function 
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's number? "))
        if n>0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")
main()