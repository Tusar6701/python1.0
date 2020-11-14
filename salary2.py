salaries=['$876,001', '$543,903', '$2453,896']
for i in range(0, 3):
    n=salaries[i]
    length = len(n)
    salary_1 = n[1:length]
    spl_str = salary_1.split(',')
    fnl_str = ''.join(spl_str)
    cln_salary = int(fnl_str)
    salaries[i]=cln_salary
    print(salaries[i])
    
