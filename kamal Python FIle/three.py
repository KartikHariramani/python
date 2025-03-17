#The Logical operator is.....
A=1
B=0
#Truth Table of And.....
print("\tThe Truth Table For AND is ")
print(f"{A}^{B}    :  {A and B}")
print(f"{A}^{A}    :  {A and A}")
print(f"{B}^{A}    :  {B and A}")
print(f"{B}^{B}    :  {B and B}")
#The Table of Or.......
print("\tThe Truth Table For OR is ")
print(f"{A} or {B} : {A or B}")
print(f"{A} or {A} : {A or A}")
print(f"{B} or {A} : {B or A}")
print(f"{B} or {B} : {B or B}")
#The Truth Table of Not......
print("\tThe Truth Table For Not is ")
print(f"~{A}       : {not A}")
print(f"~{B}       : {not B}")