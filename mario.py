# 

def main():
    print_square(3)
    # print_row(4)
#     print_column(3)
    
 
# def print_column(height):
#     # for _ in range(height):
#         print("#\n"*height,end="")   

# def print_row(width):
#     print("?"*width)
   
   
def print_square(size):
    
    ###For each row in square
    for i in range(size):
        
         #### For each brick in row
    #     for j in range(size):
            
             #### print brick
    #         print("#",end="")
    
     
        print("#"*size) 
main()