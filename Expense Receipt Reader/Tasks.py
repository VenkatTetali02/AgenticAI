from crewai import Task
from models import ExpenseReceipt

class ExpenseReceiptTasks:

    def __init__(self):
         self.Task_Read_Expense=None
         self.Task_Summarize_Expense=None
            
    def Task_Read_Expense_Receipt(self,file_path:str,agent):
             self.Task_Read_Expense= Task(description=f"Read the file in the in the file path {file_path} and return the contents as a string",
             expected_output="An output string containing the data of the file",
             agent=agent
             )
             return self.Task_Read_Expense
    
    def Task_Summarize_Expenses(self,agent):
             self.Task_Summarize_Expense=Task(description="Read the expense data received as context and summarize the data into different categories",
             expected_output="A JSON string with summarized totals by category",
             agent=agent,
             context=[self.Task_Read_Expense],
            #  output_json=ExpenseReceipt
             )
             return self.Task_Summarize_Expense

    def Task_Insert_Expenses(self,agent):
             Task_Insert_Expenses=Task(description="Insert the json data received as context and insert into database.Auto Increment the seq no in the table if one exists.Please stop if there is no json data",
             expected_output="Return the final status of the transaction as True or false. If there is an error return the error along with the status",
             agent=agent,
             context=[self.Task_Summarize_Expense]
             )
             return Task_Insert_Expenses
            