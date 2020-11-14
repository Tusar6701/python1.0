salary = input("Enter your salary [eg.: $500,000] : ")
#cleaning
length = len(salary)
salary_1 = salary[1:length]
spl_str = salary_1.split(',')
fnl_str = ''.join(spl_str)
cln_salary = int(fnl_str)

print(cln_salary)