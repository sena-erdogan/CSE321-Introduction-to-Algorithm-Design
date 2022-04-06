def courses(names, start, end):
    print("The courses are: ")
    max = 1
    i = 0
    print(names[i])
    
    for j in range(1,len(end)):
        if end[i] <= start[j]:
            max += 1
            print(names[j])
            i=j
            
    print("maximum number of courses: ", max)
    
courses(["English", "Mathematics", "Physics", "Chemistry", "Biology", "Geography"],[1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9])