# write the classes to make it possible to add budget
# classes need to have attributes to add kategories
# create def that will add 
# create def that will search for specific values
# import Pandas and create funktions to add and read excel file
# export einer Excel file
# create GUI:
# create the field for input
# create the window for viewing info
# create the field for selecting the right file

def month-Calculatro():
    month= dattimeForMOnth
    turnus = 

class FixExpense():      # put those two definitions together and make one out of it
    FixExpense = {}

    def addFix(Kategorie, Amount, turnus): # I could also make the turnus more specific - starting month, repetition function. 
        FixExpense[turnus]={Kategorie:Amount}

class FixIncome():
    FixIncome = {}


class Categories(super):
    Kategories=[]
    
    def new_category(input): #the input comes from the user
        Kategories.append(input)

    def get_category():
        return Kategories    

feste_Ausgaben=[]
einmalige_Ausgaben= []


class Expenses:
    Expenses = {}
    def addExpenses(categorie, input):
        new_expense = #userinputFromGUI
        Kategories= get_category()
        if Expenses[categorie]:
            old_sum = Expenses[categorie]
            Expenses[categorie] = old_sum + input
        else:
            Expenses[categorie] = input

   

class Income:
    Income = {}
    def addIncome(categorie, input):
        new_income = #userinputFromGUI
        Kategories= get_category()
        if Income[categorie]:
            old_sum = Income[categorie]
            Income[categorie] = old_sum + input
        else:
            Income[categorie] = input



        

    def addFix(Kategorie, Amount, turnus):
        FixIncome[turnus]={Kategorie:Amount}        
              

class MonthlyOverview(self):
    def __init__(self):
        Monthly_Expenses = 0 # es braucht eine eigene Class für Ausgeben Kategorien
        Monthly_Income = 0 # braucht auch eine eigene Kategorie für die festen Einnahmen
        Summe = Ausgaben + Einnahmen

        def fixExpens(kategorie, amount):
            for item in FixExpense: #hier muss ich eine datetime einfügen - ich will, dass das Ding monatlich checked.
            Monthly_Expenses[kategorie}=amount

        def fixExpens(kategorie, amount):
            for item in FixExpense: #hier muss ich eine datetime einfügen - ich will, dass das Ding monatlich checked.
            Monthly_Expenses[kategorie}=amount





