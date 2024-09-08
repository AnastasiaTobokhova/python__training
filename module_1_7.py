grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,4,5,5]]
student = {'Johny','Bilbo','Steve','Khendrik','Aaron'}
#average_score = sum(grades[0])/len(grades[0])

average_score = {'Johny' : sum(grades[0])/len(grades[0]),
                 'Bilbo': sum(grades[1])/len(grades[1]),
                 'Steve' : sum(grades[2])/len(grades[2]),
                 'Khendrik' : sum(grades[3])/len(grades[3]),
                 'Aaron' : sum(grades[4])/len(grades[4])}
print(average_score)



