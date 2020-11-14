orders=[['34587', 'Learning Python', 'Mark Lutz', 4, 40.95], ['98762', 'Programming Python', 'Mark Lutz', 5, 56.80], ['77226', 'Head First Python', 'Paul Barry', 3, 32.95], ['88112', 'Einfuhrung in Python3', 'Bernd Klein', 3, 24.99]]
output = [[0]*2]*4 
for i in range (0, 4):
    output[i][0]=orders[i][0]
    output[i][1]=orders[i][3] * orders[i][4]
    if output[i][1] < 100 :
        output[i][1]= output[i][1]+10
    
print(output)