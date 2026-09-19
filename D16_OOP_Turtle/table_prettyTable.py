from prettytable import PrettyTable
from prettytable import DEFAULT, MSWORD_FRIENDLY, PLAIN_COLUMNS, RANDOM, MARKDOWN, ORGMODE, DOUBLE_BORDER, SINGLE_BORDER

# prettyTable is a python library that allows you to print data in a tabular format. It is very useful for displaying data in a readable format.
table=PrettyTable()


# _______________________________________
# adding columns to the table
table.add_column("f_name",("arif","najm","uddin"))
table.add_column("f_name",("arif","najm","uddin"))
table.add_column("f_name",("arif","najm","uddin"))


# ___________________________________
# alignment of the columns
# table.align="l"
table.align="r"

# rename the columns
table.field_names=["First Name","Last Name","Age"]

# _________________________________
# adding rows to the table
table.add_row(["xyz","abc","mno"])

# ________________________________

# replace  the value of a cell in the  table
table.rows[0][0]="NAJMUDDIN"
table.rows[0][1]="ARIF"
table.rows[0][2]="syeed"

# ________________________________

# change table border style and fill color
# table.border=False
# table.header=False

# ___________________________
# table style change
table.set_style(DOUBLE_BORDER)


print(table)