from Tasks import ExpenseReceiptTasks
from Agents import ExpenseReceiptAgents
from crewai import Crew,Process

file_path="Hotel_Receipt.pdf"

#get the agents
ExpenseAgents=ExpenseReceiptAgents()
Agent_Expense_Receipt_Reader=ExpenseAgents.Expense_Receipt_Reader(file_path)
Agent_Expenses_Categorizer=ExpenseAgents.Expenses_Categorizer()
Agent_Database=ExpenseAgents.Expenses_Insert()

#get the tasks
ExpenseTasks=ExpenseReceiptTasks()
Task_Read_Expense_Receipt=ExpenseTasks.Task_Read_Expense_Receipt(file_path,Agent_Expense_Receipt_Reader)
Task_Summarize_Expenses=ExpenseTasks.Task_Summarize_Expenses(Agent_Expenses_Categorizer)
Task_Insert_Expenses=ExpenseTasks.Task_Insert_Expenses(Agent_Database)

#kick of the crew
crew=Crew(agents=[Agent_Expense_Receipt_Reader,Agent_Expenses_Categorizer,Agent_Database],tasks=[Task_Read_Expense_Receipt,Task_Summarize_Expenses,Task_Insert_Expenses],process=Process.sequential,share_crew=False)
res=crew.kickoff()
print(f"result is {res}")
print(f"task output is {Task_Summarize_Expenses.output}")
