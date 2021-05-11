#!/usr/bin/env python3

import pandas as pd


def main():

    excel_file = 'movies.xls'
    movies0 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    movies1 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    movies2 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    all_movies = pd.concat([movies0, movies1, movies2])
    print(all_movies.shape)

    sorted_by_gross = all_movies.sort_values(["Gross Earnings"], ascending=False)
    print(sorted_by_gross)


    sorted_by_budget = all_movies.sort_values(["Budget"], ascending=False)
    print(sorted_by_budget)


main()
