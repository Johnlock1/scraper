from cs50 import SQL
# import sqlite3
import xlsxwriter

def export(table):
    db = SQL("sqlite:///database.db")
    # conn = sqlite3.connect("database.db")
    # db = conn.cursor

    workbook = xlsxwriter.Workbook("cars.xlsx")
    worksheet = workbook.add_worksheet()

    querry = db.execute("SELECT * FROM :table", table=table)

    row = 1
    col = 0

    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Car_Id', bold)
    worksheet.write('B1', 'Make', bold)
    worksheet.write('C1', 'Model', bold)
    worksheet.write('D1', 'Year', bold)
    worksheet.write('E1', 'Price', bold)
    worksheet.write('F1', 'Phone', bold)
    worksheet.write('G1', 'Link', bold)

    for i, entry in enumerate(querry):
        for key in entry.keys():
            value = entry[key]
            worksheet.write(row, col, value)
            col += 1
        value = "http://car.gr/{}".format(entry['car_id'])
        worksheet.write(row, col, value)
        row += 1
        col = 0

    workbook.close()