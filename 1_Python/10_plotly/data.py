import pandas as pd
class Data:
    def __init__(self):
        self.df = pd.read_csv('./OnlineRetail.csv' , encoding='latin1')
    def get_data(self):
        return self.df
    def dropna(self):
        self.dropNa_df = self.df.copy()
        self.dropNa_df = self.dropNa_df.dropna(subset=["InvoiceDate","CustomerID"])
        return self.dropNa_df
    def non_cancelled_invoice(self):
        self.dropna()
        self.nonCancelled_df = self.dropNa_df.copy()
        self.nonCancelled_df = self.nonCancelled_df[~self.nonCancelled_df["InvoiceNo"].astype(str).str.startswith('C')]
        return self.nonCancelled_df
    def get_clean_data(self):
        self.clean_data = self.df.copy()
        self.clean_data = self.clean_data.dropna(subset=["InvoiceDate","CustomerID"])
        self.clean_data = self.clean_data[~self.clean_data["InvoiceNo"].astype(str).str.startswith('C')]
        self.clean_data = self.clean_data[(self.clean_data['Quantity']>0) & (self.clean_data['UnitPrice']>0)]
        # add new feature
        self.clean_data["Revenue"] = self.clean_data['Quantity'] * self.clean_data['UnitPrice']
        # convert to date-time
        self.clean_data["InvoiceDate"] = pd.to_datetime(self.clean_data["InvoiceDate"])
        # month column
        self.clean_data["Month"] = self.clean_data["InvoiceDate"].dt.to_period("M").astype(str)
        return self.clean_data
    def monthly_revenue(self):
        self.get_clean_data()
        self.monthly_revenue = self.clean_data.groupby("Month")["Revenue"].sum().sort_index()
        return self.monthly_revenue