# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry

if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        list1.append([name,score])
    
        
    
    list_scores = []  
    for item in list1:  list_scores.append(item[-1])
    

    second_down_score = list(sorted(set(list_scores)))[1]
   
    
    
    list2 = []
    for item in list1:
        if item[-1] == second_down_score:
            list2.append(item)
            
    #print(list2)
    
    for i in sorted(list(map(lambda item: item[0], list2))): print(i)