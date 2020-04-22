import requests
import cs50 as cs
import csv
from bs4 import BeautifulSoup

#def main():
#    info = get_digikey(input("URL: "))
#    db_file = input("Database: ")
    # xls_file = input("Export as: ")     # FOR EXCEL EXPORT
    # create_database(file_name)          # ONLY IF DATABASE NOT CREATED
#    add_info(info, db_file)
#    delete_duplicate(db_file)             # VERIFICATION FOR DUPLICATES
    # export_xls(db_file, xls_file)       # ONLY IF EXPORT TO EXCEL WANTED

class database():
    def __init__(self):
        self.info = ''

    def delete_duplicate(self,db_file):
        if db_file.find('.db') == -1:
            db_file += '.db'
        database = cs.SQL("sqlite:///" + db_file)
        database.execute("DELETE FROM components WHERE id NOT IN (SELECT MIN(id) FROM components GROUP BY part_number)")


    def get_digikey(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Uses html tag and unique (class, id, itemprop, etc.) to retrieve info
        site_number = soup.find('td', id="reportPartNumber").get_text().strip()
        manufacturer = soup.find('span', itemprop="name").get_text().strip()
        part_number = soup.find('h1', itemprop="model").get_text().strip()
        description = soup.find('td', itemprop="description").get_text().strip()
        price = soup.find('span', itemprop="price").get_text().strip()
        datasheet = soup.find('a', class_="lnkDatasheet").get('href').strip()
        categorie = soup.find('td', class_="attributes-td-categories-link").get_text().strip()

        info = [categorie, site_number, part_number, price, description, manufacturer, datasheet]

        return info


    def create_database(self,db_file):
        # Creates db file.
        open(db_file + ".db", "w").close()

        # Instance of SQL object
        database = cs.SQL("sqlite:///" + db_file + ".db")

        # Creates new table in db.
        database.execute("CREATE TABLE components (id TEXT, categorie TEXT, name TEXT, "
                         "part_number TEXT, price TEXT, description TEXT, manufacturer TEXT, datasheet TEXT)")


    def add_info(self,info, db_file):
        # Instance of SQL object
        if db_file.find('.db') == -1:
            db_file += '.db'
        database = cs.SQL("sqlite:///" + db_file)

        # Extracts unique id
        db_id = database.execute("SELECT id FROM components ORDER BY id DESC")

        if not db_id:
            number = "-1"
        else:
            seq_type = type(str(db_id[0]))
            number = seq_type().join(filter(seq_type.isdigit, str(db_id[0])))
        number = str(int(number) + 1)
        number = str(number).zfill(5 - len(number))
        part_id = "E-" + number

        # Inserts new value in db.
        database.execute("INSERT INTO components (id, categorie, name, part_number, price, description, manufacturer, "
                         "datasheet) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", part_id, info[0], info[1], info[2], info[3], info[4],
                         info[5], info[6])


    def export_xls(self,db_file, xls_file):
        # Instance of SQL object
        database = cs.SQL("sqlite:///" + db_file + ".db")

        # Gets result from SQL query
        result = database.execute("SELECT id, categorie, name, part_number, price, description, "
                                  "manufacturer, datasheet FROM components")

        # Creates or open file in append mode
        with open(xls_file + ".csv", "a") as xls:
            writer = csv.writer(xls)

            # Creates columns names for each row
            writer.writerow(["id", "categorie", "name", "part_number", "price", "description", "manufacturer", "datasheet"])

            # Adds db row to excel.
            for row in result:
                writer.writerow(
                    [row["id"], row["categorie"], row["name"], row["part_number"], row["price"], row["description"],
                     row["manufacturer"], row["datasheet"]])

