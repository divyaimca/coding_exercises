# he National University conducts an examination of  students in  subjects.
# Your task is to compute the average scores of each student.

# The format for the general mark sheet is:

# Student ID → ___1_____2_____3_____4_____5__               
# Subject 1   |  89    90    78    93    80
# Subject 2   |  90    91    85    88    86  
# Subject 3   |  91    92    83    89    90.5
#             |______________________________
# Average        90    91    82    90    85.5 
# Input Format

# The first line contains  and  separated by a space.
# The next  lines contains the space separated marks obtained by students in a particular subject.

# Constraints



# Output Format

# Print the averages of all students on separate lines.

# The averages must be correct up to  decimal place.

# Sample Input

# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5
# Sample Output

# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5       
# 
# 
import sys

def avg_scores(li1):
    
    stu_dict = {}
    
    for inpt in range(li1[1]):
        stu_dict[f'input_{inpt}'] = input().split()
    
    #print(stu_dict)
    
    # for item in stu_dict:
    #     print(stu_dict[item])
        
        
    
    scores = (list(zip(*stu_dict.values())))
    
    #print(scores)
    
    for x in scores:
        #print(x)
        sum = 0
        for y in x:
            #print(y)
            sum += float(y)
        print(sum/len(x))
    
        
    



if __name__ == '__main__':
    li1 = list(map(lambda item: int(item), input().split()))    
    
    if len(li1) != 2:
        print('wrong input, please enter valid input')
        sys.exit(-1)
    
    avg_scores(li1)
    