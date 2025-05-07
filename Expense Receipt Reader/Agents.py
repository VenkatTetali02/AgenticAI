from crewai import Agent
from Tools import pdf_file_reader,image_reader,list_tables,tables_schema,execute_sql,check_sql
from llm import llm

class ExpenseReceiptAgents:

    def Expense_Receipt_Reader(self,file_path):
        Agent_Expense_Receipt_Reader=Agent(role="Expense Receipt Reader Agent",goal="Read the Expense Receipt specified by the file path and return the contents as a string. Select the appropriate tool depending on the file format",
                       backstory=f"You are an expert reader in reading Expense Receipt files provided by file path {file_path} and returning the content in a String format",
                       tools=[pdf_file_reader,image_reader],
                       llm=llm,
                       verbose=True)
        return Agent_Expense_Receipt_Reader
    
    def Expenses_Categorizer(self):
        Agent_Expenses_Categorizer=Agent(role="Expense Categorizer Agent",goal="Categorize the Expense data provided as String into Food, Hotel,Travel,Other,Taxes,Fees,Liquor,Misc categories",
                       backstory="""You are an expert reader in reading text and categorizing the information.Produce only the output and no other supplemental information.
            1. Extract the different expense types and amounts from the below text and classify them into Food, Hotel,Travel,Other,Taxes,Fees,Liquor,Misc categories only by the rules given below
                Liquor should not be included in the Food category
                If a item does not belong to any category as per the above mentioned categories put it in Misc Category
                Put Services like Spa,Gym and booking charges into Other category
                All alchoholic drinks like Beer, Wine, Whiskey, Tequila, Cocktails and hard liquor should be categorized as Liquor and not as Food
            2. Once the groups are identified go through individual items in each group and sum up the amounts to calculate the group total.
            3. Calculate the Total amount by adding up the group totals of Food,Liquor,Other,Hotel,Travel,Taxes and Misc categories.
            4. Override the Total Amount with the Total Amount calculated above and output it to Total_Amount key and show detailed calculation for this field
            5. Output the group totals in a JSON format and provide the output if and only if the categorization was done without errors.
            6. Add emp_id as key to the output json with value of "12345".
           """,
                       llm=llm,
                       verbose=True)
        return Agent_Expenses_Categorizer
    
    def Expenses_Insert(self):
        Agent_Database=Agent(role='Database Agent',
                    goal="Insert the data provided in JSON format to the appropriate database table",
                    backstory="""
                    An expert in inserting the data provided in JSON format to sqlite database. Only insert one row of data per json and no new table should be created during the process. 
                    Dont create any new tables in the process or dont alter any table structures
                    Also insert 0 for Number type fields if no value was found or retrieved and Space for String fields and NULL for date type fields.
                    """,
                    tools=[list_tables,tables_schema,check_sql,execute_sql],
                    llm=llm,
                    verbose=True)
        
        return Agent_Database