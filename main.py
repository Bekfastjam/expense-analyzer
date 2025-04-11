from data_loader import load_and_clean_data
from analyzer import analyze_expenses

def run():
    df = load_and_clean_data("data/expenses.csv")
    analyze_expenses(df)
    
if __name__ == "__main__":
    run()