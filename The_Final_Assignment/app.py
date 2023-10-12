import pyodbc as db
from db_utils import result_as_dict

def main():
    driver = '{ODBC Driver 18 for SQL Server}'
    server = 'localhost'
    database = 'final_assignment_db'
    encrypt = 'no'
    trusted_connections = 'yes'

    connection_string = f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        Trusted_Connection={trusted_connections};
        ENCRYPT={encrypt};
    '''
    exit_terms = ['quit', 'exit', 'bye']

    with db.connect(connection_string) as connection:
        cursor = connection.cursor()
        while(True):
            input_val = input('db> ').split()

            if(input_val[0] in exit_terms): break

            params = get_params(input_val)
            cursor.execute(f'EXEC {input_val[0]} {params}')
            result = result_as_dict(cursor)

            print_table(result)

def print_table(dict_list):

    for column_name in dict_list[0]:
        print(column_name.ljust(40), end='')
    print()

    for row in dict_list:
        for value in row.values():
            print(str(value).ljust(40), end='')
        print()
        


def get_params(input_list):
    val_size = len(input_list)

    params = ''
    for i in range(1, val_size):
        if not input_list[i].isdigit():
            params += f"'{input_list[i]}' "
        else:
            params += f'{input_list[i]} '
        if i < val_size-1:
            params += ','
    
    return params

   
if __name__ == '__main__':
    main()