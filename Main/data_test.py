import sqlite3

connection = sqlite3.connect('data_base.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(username TEXT, password TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bankaccounts(
bankname TEXT, branchname TEXT, personname TEXT, amount INTEGER)""")

# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'krisia', 14000)")

# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'peyra', 726380)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'kotia', 4262700)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'lachlia', 590482)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'eissen', 29002)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'drayan', 482941)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'janna', 10000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'xandyr', 227100)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'rikia', 48230)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'balanagar', 'frey', 727380)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'brayan swalies', 17270)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'whitelaw whitley', 7280)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'octavio brent', 47820)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'alcot townsend', 276380)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'spence sydney', 67000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'boza melton', 129000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'kastor hornsby', 472850)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'claudde bentham', 18745980)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'chityal', 'darin chatham', 54190)")
#
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'rodney', 208027)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'verdell', 206702)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'nikolas', 2868206)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'chadwick', 393005)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'tibault', 85689)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'blankley', 25724670)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'wolter', 46770)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('sbi', 'karimnagar', 'jermias withers', 1367257)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'lavernia luxford', 134104)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'bobby', 134010)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'clementina', 1639410)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'silvette', 184130)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'hidie', 31690)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'garan', 30184174)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'hidie harrington', 1310170)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'hyderguda', 'dania chatham', 63491)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'giso smit', 8310)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'parkley lester', 3164518)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'jarvey hastings', 865481)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'roland myercough', 3185483)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'germain brent', 13845184)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'harri smither', 238483740)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'harland alden', 11824790)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'eartha birenhead', 176190)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('hdfc', 'koti', 'edukia braxton', 2138210)")
#
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'willi rodeny', 243310)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'willi per', 643190)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'spence', 878590)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'alcot', 1861930)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'octavio brent', 2949360)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'spence', 28210)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'caludde', 38140)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'silvertre', 36571)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'jermias', 1718920)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'himayatnagar', 'garfield', 124690)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'timothy', 28576290)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'ashton', 425929)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'ronald', 247562950)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'johnson ashley', 4765920)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'germone brookes', 4205750)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'durant sheldon', 252075)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'beal ward', 3788)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'beal ridley', 37610)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'shaw ridley', 28532)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('icici', 'begumpet', 'paulus altham', 8345819)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'jarvey hasghing', 315490)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'kayle churilles', 2135410)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'lavarnia', 2471760)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'kendall', 3748140)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'lemdall', 19000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'parkley lester', 315490)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'jagger', 151000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'enes sydeny', 382900)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'bodil denholm', 89000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'bowenpally', 'jean luca', 100000)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'eartha', 13741940)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'beardsley brown', 1746140)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'pauals althham', 374900)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'durant brookes', 1881900)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'sgwissy', 237746)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'shaw ward', 658901)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'chesley mildenhall', 2961040)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'edukorias', 27346190)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'sofia stonebridge', 345190)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('union', 'chikkadapally', 'cindy', 8134591)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'chotia', 234591)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'makenzie', 4581490)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'kendhyall', 17463140)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'garna cohly', 394610)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'sadduique', 348739862)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'sofiea', 84679140)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'trines', 364020)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'elem keats', 89000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'kukatpally', 'harri', 420000)")
#
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'antony', 20000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'unnai', 51839)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'sachine', 3478190)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'jeffy', 35200)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'wunart', 1631000)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'michael', 316500)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'hojan', 18365910)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'kiav', 873610)")
# cursor.execute("INSERT INTO bankaccounts VALUES ('axis', 'ramkote', 'knallies', 1853910)")


cursor.execute("SELECT * FROM bankaccounts")
print(cursor.fetchall())

cursor.execute("SELECT * FROM accounts")
print("Accounts")
print(cursor.fetchall())

connection.commit()

connection.close()