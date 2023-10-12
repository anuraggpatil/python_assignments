
def result_as_dict(cursor):
    columns=[column[0] for column in cursor.description]
    results=[]

    for row in cursor.fetchall():
        result=dict()
        for i in range(len(columns)):
            result[columns[i]]=row[i]
        results.append(result)
    return results