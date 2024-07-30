import spacy
nlp = spacy.load('en_core_web_sm')

def generate_narrative(df):
    company_name = df['Name'][0]
    pe_ratio = df['P/E Ratio'][0]
    debt_equity_ratio = df['Debt/Equity Ratio'][0]
    narrative = f"{company_name} has a P/E ratio of {pe_ratio:.2f} and a debt-to-equity ratio of {debt_equity_ratio:.2f}. "
    if pe_ratio > 20:
        narrative += "The company appears to be overvalued. "
    else:
        narrative += "The company appears to be fairly valued. "
    if debt_equity_ratio > 1:
        narrative += "The company has a high level of debt compared to its equity."
    else:
        narrative += "The company has a manageable level of debt."
    return narrative

if __name__ == "__main__":
    df = pd.read_csv('data/sample_data.csv')
    narrative = generate_narrative(df)
    print(narrative)
