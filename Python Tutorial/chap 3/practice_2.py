#write template given below with name and date
# letter = ''' dear <name>
#                 You are selected!
#                 <Date>'''

letter = '''Dear <|NAME|>
            You Are Selected
            Date : <|DATE|>
'''
name = input("Enter your name:  ")
date = input("Enter date:  ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)