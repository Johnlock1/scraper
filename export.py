from cs50 import SQL
import xlsxwriter

def export(table, day):
    db = SQL("sqlite:///database.db")

    # create workbook
    workbook = xlsxwriter.Workbook("cars4.xlsx")
    worksheet = workbook.add_worksheet()

    # execute database query
    selection = ("SELECT * FROM {} WHERE date LIKE '{}'".format(table, day))
    query = db.execute(selection)

    row = 1
    col = 0

    # write file headers
    bold = workbook.add_format({'bold': True})

    for key in query[0].keys():
        worksheet.write(0, col, key, bold)
        col += 1
    worksheet.write(0, col, 'link', bold)
    col = 0

    # write all info from database
    for i, entry in enumerate(query):
        for key in entry.keys():
            value = entry[key]
            worksheet.write(row, col, value)
            col += 1
        value = "http://car.gr/{}".format(entry['car_id']) # create a link to the classified
        worksheet.write(row, col, value)
        row += 1
        col = 0

    workbook.close()