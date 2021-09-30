def main():
    names_listed = ['arvid', 'alex', 'mikael', 'fabian', 'simon', 'brian', 'arthalim']
    
    
    name_delete = input('Enter name: ')
    name_delete.lower()
    names_listed.remove(name_delete)
    
    
    for i in names_listed:
        print(i)
    print(name_delete)
    
    
    
    return names_listed, name_delete