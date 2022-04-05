from enum import Flag
import pandas as pd 
import random


def main():
    
    df = pd.read_csv('emp.csv')
    df = df.drop(['Timestamp' , 'Score'], axis=1)

    def get_random_row():
        cols = df.columns
        new_row =  {}
        for col in cols:
            vals =  df[col].value_counts().to_dict()
            choice = random.choices([*vals.keys()] ,  weights=[*vals.values()])
            new_row[col] = choice[0]

        return new_row

    total_n = 350
    final_df  = []
    for i in range(total_n):
        row  = get_random_row()
        final_df.append(row)
    
    final_df = pd.DataFrame(final_df)
    final_df.to_csv("final.csv" , index=False)
    # final_df.to_excel("final.xlsx")
            
        
        

    



if __name__ == '__main__':
    main()
