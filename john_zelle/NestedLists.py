def averages(grades_per_subject):
    """(list of list of numbers) => lift of floats

    Return a new list in which each item is the average of the grades
    in the inner list at the corresponding position of grades.

    >>> averages([[70,75,80],[70,80,90,100],[80,100]])
    [75.0, 85.0, 90.0]
    """

    averages_per_subject = []
    
    for grades_list in grades_per_subject:
        #calculate the avg of each list of grades
        
        total = 0
        
        for mark in grades_list:
            total = total + mark
            
        averages_per_subject.append(total/(len(grades_list)))
        
    return averages_per_subject
        
print(averages([[70,75,80],[70,80,90,100],[80,100]]))
  
