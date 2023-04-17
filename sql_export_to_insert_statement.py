import json

table_name = "invoicer.invoices"
sql = f"INSERT INTO {table_name} ("

with open("/Users/jozefmankovecky/Documents/invoices.json", "r") as f:
    data = json.loads(f.read())

    columns = []
    for k, _ in data[0].items():
        columns.append(k)

    sql += f"{', '.join(columns)})\nVALUES "

    all_values = []
    for invoice in data:
        to_insert = []
        for k, v in invoice.items():
            if isinstance(v, str):
                to_insert.append(f'"{v}"')
            else:
                to_insert.append(str(v))
        all_values.append(f"{', '.join(to_insert)}")

    sql += f"({'), ('.join(all_values)});"
    
with open("/Users/jozefmankovecky/Documents/insert_sql.sql", "w") as f:
    f.write(sql)