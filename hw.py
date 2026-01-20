import matplotlib.pyplot as plt

# Dataset
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [12, 15, 17, 14, 13, 12, 34]
customers = [50,15,22,1,2,3,4]
plt.plot(days, sales)
plt.title("Sales Over a Week")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()
plt.bar(days, customers)
plt.title("Number of Customers Per Day")
plt.xlabel("Days")
plt.ylabel("Customers")
plt.show()
plt.scatter(customers, sales)
plt.title("Customers vs Sales")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.show()
plt.hist(sales)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
plt.pie(sales, labels=days, autopct="%1.1f%%")
plt.title("Sales Contribution by Day")
plt.show()