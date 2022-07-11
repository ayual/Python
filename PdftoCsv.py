# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:51:29 2022

@author: alana
"""

import tabula as tab

pdf_path="Prüfungen2022.pdf" 


"""
##Only working for one Table in one page !
#
#
dfs = tab.read_pdf(pdf_path,pages=1)
dfs[0].to_csv("first_table2.csv")
"""

"""
##for more Tables in one Page 
#
#
dfs = tab.read_pdf(pdf_path,pages='1')
#print(len(dfs))

for i in range(len(dfs)):
    dfs[i].to_csv(f"Tabel_{i}.csv")
    
"""

##for all Tables in all Pages 
#
#    
dfs = tab.read_pdf(pdf_path,pages='all')
for i in range(len(dfs)):
    dfs[i].to_csv(f"Tabel_{i}.csv")