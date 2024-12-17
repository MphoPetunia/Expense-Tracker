from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


EXCEL_FILE = 'expenses.xlsx'


if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = request.form['amount']

    df = pd.read_excel(EXCEL_FILE)

    # Create a new DataFrame for the new data
    new_data = pd.DataFrame([{
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': float(amount)
    }])

    # Use pd.concat to add the new data
    df = pd.concat([df, new_data], ignore_index=True)


    df.to_excel(EXCEL_FILE, index=False)

    return "Expense added successfully! <a href='/'>Go back</a>"
if __name__ == '__main__':
    app.run(debug=True)
