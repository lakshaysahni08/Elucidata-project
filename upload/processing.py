import pandas as pd
import sys

class Processor:

    def __init__(self,file_path):
        self.file_path = file_path


    def _file_loader(self):
        file = pd.ExcelFile(r'{}'.format(self.file_path))
        df = pd.read_excel(file)
        df = df.fillna("none")
        return df

    # task 1
    def filter_compound_id(self):
        df = self._file_loader()

        df_LPC  = df.loc[df['Accepted Compound ID'].str[-3:] == 'LPC']
        df_LPC.to_excel("./media/output_lpc.xlsx") 

        df_PC  = df.loc[(df['Accepted Compound ID'].str[-2:] == 'PC') & (df['Accepted Compound ID'].str[-3:] != 'LPC')]
        df_PC.to_excel("./media/output_pc.xlsx") 

        df_plasmalogen  = df.loc[df['Accepted Compound ID'].str[-11:] == 'plasmalogen']
        df_plasmalogen.to_excel("./media/output_plasmalogen.xlsx") 

    # task 2 
    # adding coloumn for round off
    def round_retention_time(self):
        df = self._file_loader()
        df["Retention Time Roundoff (in mins)"] = pd.Series(round(df['Retention time (min)']))
        df["Retention Time Roundoff (in mins)"] = df["Retention Time Roundoff (in mins)"].astype(int)
        df.to_excel('./media/output_rounded.xlsx')
        return df


    ## task 3
    def group_mean_finder(self):
        
        df = self.round_retention_time()

        df_mean = df[df.columns[3:]]
        df_mean = df_mean.groupby(["Retention Time Roundoff (in mins)"]).mean()
        df_mean['mean'] = df_mean[df_mean.columns[1:]].mean(axis=1)
        df_mean.to_excel('./media/output_mean.xlsx')





