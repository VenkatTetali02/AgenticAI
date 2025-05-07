from crewai.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_community.tools import ListSQLDatabaseTool,InfoSQLDatabaseTool,QuerySQLDataBaseTool,QuerySQLCheckerTool
from langchain_community.document_loaders import PyPDFLoader
from PIL import Image
import pytesseract
import sqlite3
from llm import llm

db = SQLDatabase.from_uri("sqlite:///employee.db")
print(f'usable table names are {db.get_usable_table_names()}')

@tool("PDF File Reader")
def pdf_file_reader(file_path:str):
    """
    Input is a string which consists of file path.Read the PDF file provided in the path file_path and return the contents in String format.
    """
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    content=[doc.page_content for doc in docs]
    final_content=" ".join(content)
    return final_content

@tool("Image Reader")
def image_reader(file_path:str):
    """
    Input is a path to the Image File. Read the Image, extract the text and return the text in String format.
    """
    img=Image.open(file_path)
    # img.show()
    text=pytesseract.image_to_string(img)
    return text


@tool("list_tables")
def list_tables() -> str:
    """List the available tables in the database"""
    return ListSQLDatabaseTool(db=db).invoke("")

@tool("tables_schema")
def tables_schema(tables: str) -> str:
    """
    Input is a comma-separated list of tables, output is the schema and sample rows
    for those tables. Be sure that the tables actually exist by calling `list_tables` first!
    Example Input: table1, table2, table3
    """
    tool = InfoSQLDatabaseTool(db=db)
    return tool.invoke(tables)

@tool("execute_sql")
def execute_sql(sql_query: str) -> str:
    """Execute a SQL query against the database. Returns the result"""
    return QuerySQLDataBaseTool(db=db).invoke(sql_query)

@tool("check_sql")
def check_sql(sql_query: str) -> str:
    """
    Use this tool to double check if your query is correct before executing it. Always use this
    tool before executing a query with `execute_sql`.
    """
    return QuerySQLCheckerTool(db=db, llm=llm).invoke({"query": sql_query})
