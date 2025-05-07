from pydantic import BaseModel, Field
from typing import Optional

class ExpenseReceipt(BaseModel):
    vendor_name: str=Field(default=None,description="A field which captures the Vendor Name from the Text")
    transaction_date: str=Field(description="Check-in date,Transaction Date on which the transaction happened or sale happened")
    Food:Optional[list[float]]=Field(default=None,description="A list which captures the summarized expense amounts related to Food and related items category.Alchohol Beverages expenses like Beer, Whiskey are excluded")
    Hotel:Optional[list[float]]=Field(default=None,description="A list which captures the summarized expense amounts related to Hotel category like Accomdation,Room, Suites etc")
    Tax:Optional[list[float]]=Field(deault=None,description="A list which captures the summarized expense amounts related to Tax category i.e. Locality, State, Federal taxes")
    Travel:Optional[list[float]]=Field(default=None,description="A list which captures the summarized expense amounts related to Travel category like Airline tickets, Uber, taxi and Bus tickets")
    Liquor:Optional[list[float]]=Field(default=None,description="A list which captures the summarized expense amounts related to Liquor category like Beer, Wine, Tequila,Vodka,Whiskey, Cocktails etc")
    Other:Optional[list[float]]=Field(default=None,description="A list which captures the summarized expense types related to items which are not  Food related, Liquor related ,Tax related, Travel,Accomdation category etc")
    Total_Amount:Optional[int]=Field(default=None,description="Total Amount of the travel which is Food + Hotel + Tax + Travel + Liquor + Other")