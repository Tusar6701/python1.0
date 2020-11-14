dist = input("Enter the distance travelled by youto and fro in kms : ")
f_avg = input("Enter the fuel average in your area [km/litre]: ")
cost_of_diesel = input("Enter the cost of diesel [int INR]: ")
f_cons = float(dist) / float(f_avg)
cost = float(f_cons) * float(cost_of_diesel)

print("The cost of travel is : ", cost)
