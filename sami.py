Wage = input("What is your Average Hourly Rate")
Living_Time = input("How many months of living do you want on savings at $150 a week")
Initial_Expenses = input("How much do you want to spend on initial expenses")

Total_Savings = float(Initial_Expenses) + float(Living_Time*4)
Hours = ((Total_Savings / float(Wage) / 46))
Hours_Reasonable = int(Hours)

print("Hence, you must save a total of: " + str(Total_Savings))
print("Hence, you must work a total of  " + str(Hours_Reasonable) + " hours per week considering you work for 46 weeks")
