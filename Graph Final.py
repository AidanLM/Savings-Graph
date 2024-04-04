#RUN pip install matplotlib in cmd first!
import matplotlib.pyplot as plt
 
# Get user input
weekly_income = float(input("Enter your weekly income ($): "))
 
# Store costs with reasons
weekly_costs = []
while True:
    reason = input("Enter a reason for the cost or type 'done': ")
    if reason.lower() == 'done':
        break
    try:
        cost = float(input("Enter the cost amount ($): "))
        weekly_costs.append((reason, cost))  
    except ValueError:
        print("Invalid cost input. Please enter a number.")
 
# Weekly savings calculation
weekly_savings = [weekly_income - cost for reason, cost in weekly_costs]
 
# Initialize savings and loop variables
savings_goal = float(input("Enter your savings goal ($): "))
cumulative_savings = [weekly_income - weekly_costs[0][1]]  
weeks = 1  
 
# Plot the graph (partially modified - we'll plot at the end)
plt.figure(figsize=(6, 4))  
 
# Loop until goal is reached
while cumulative_savings[-1] < savings_goal:
    current_week_income = weekly_income
    if weeks < len(weekly_costs):
        current_week_cost = weekly_costs[weeks - 1][1]  
    else:
        current_week_cost = 0
    current_week_savings = current_week_income - current_week_cost
    cumulative_savings.append(cumulative_savings[-1] + current_week_savings)
    weeks += 1  
 
# Generate x-axis labels
week_labels = [f"Week {i+1}" for i in range(weeks)]
 
# Create the Table (Modified)
column_labels = ["Reason", "Cost", "Total Cost"]  # Added 'Total Cost' column
table_data = []
for reason, cost in weekly_costs:
    total_cost = weeks * cost  # Calculate total cost based on weeks
    table_data.append([reason, cost, total_cost])  # Include total cost
the_table = plt.table(cellText=table_data, colLabels=column_labels, loc='bottom')
 
# Create Graph
fig, ax = plt.subplots(figsize=(6, 6)) # Use a single subplot for graph and table
ax.plot(week_labels, cumulative_savings, label="Cumulative Savings")
ax.axhline(y=savings_goal, color='red', linestyle='--', label="Savings Goal")
ax.set_xlabel("Weeks")  
 
# Customize x-axis labels (simple numbers)
ax.set_xticks(range(weeks), [str(i+1) for i in range(weeks)])
 
# Customize y-axis labels (go up in increments of 500)
if cumulative_savings:  
    plt.yticks(range(0, int(max(cumulative_savings) + 500), 500), ["${}".format(y) for y in range(0, int(max(cumulative_savings) + 500), 500)])
else:
    plt.yticks(range(0, int(weekly_income + 500), 500), ["${}".format(y) for y in range(0, int(weekly_income + 500), 500)])  
 
# Set minimum y-axis value to 0
ax.set_ylim(ymin=0)
ax.legend()
ax.set_title("Weekly Savings")  
ax.grid(True)
 
# Add the table below - You might need to adjust bbox values
the_table = ax.table(cellText=table_data, colLabels=column_labels, loc='bottom', bbox=[0, -0.35, 1, 0.3])
 
fig.suptitle('Weekly Savings and Expenses')  
plt.tight_layout()  
plt.show()
 