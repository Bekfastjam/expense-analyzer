import pandas as pd

def analyze_expenses(df: pd.DataFrame) -> None:
    """Generate spending insights."""
    # Calculate totals
    total = df['Amount'].sum()
    by_dept = df.groupby('Department')['Amount'].sum()
    
    # Calculate percentages
    dept_pct = (by_dept / total * 100).round(1)
    
    # Print results
    print(f"📊 Total Expenses: ${total:,}")
    
    print("\n💼 By Department:")
    print(by_dept.apply(lambda x: f"${x:,}"))
    
    print("\n📈 Percentage by Department:")
    print(dept_pct.apply(lambda x: f"{x}%"))
    
    print("\n⚠️ Top 5 Highest Expenses:")
    print(df.nlargest(5, 'Amount')[['Employee', 'Department', 'Amount']])