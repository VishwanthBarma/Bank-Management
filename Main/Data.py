from Classes import *
import pickle

# **********Bank Classes************
sbi_bank = Bank("State Bank Of India")
hdfc_bank = Bank("HDFC Bank Of India")
icici_bank = Bank("ICICI Bank")
union_bank = Bank("Union Bank Of India")
axis_bank = Bank("AXIS Bank")


# *********Branches of banks (5)*********
sbi_bank.add_branch("Balanagar")
sbi_bank.add_branch("Chityal")
sbi_bank.add_branch("KarimNagar")
sbi_bank.add_branch("Nalgonda")
sbi_bank.add_branch("Medchal")

hdfc_bank.add_branch("Hyderguda")
hdfc_bank.add_branch("Koti")
hdfc_bank.add_branch("Abids")
hdfc_bank.add_branch("Bazaarghat")
hdfc_bank.add_branch("Kachiguda")

icici_bank.add_branch("Himayat Nagar")
icici_bank.add_branch("Nampally")
icici_bank.add_branch("Begumpet")
icici_bank.add_branch("Badichowdi")
icici_bank.add_branch("Gachibowli")

union_bank.add_branch("Banjara Hills")
union_bank.add_branch("Bowenpally")
union_bank.add_branch("Chikkadapally")
union_bank.add_branch("Dilsukh Nagar")
union_bank.add_branch("Gayatri Nagar")

axis_bank.add_branch("Rudraram")
axis_bank.add_branch("Saifabad")
axis_bank.add_branch("Ramkote")
axis_bank.add_branch("Nuzividu")
axis_bank.add_branch("Kukatpally")

# ******* Customers for each and every branch(10) **********

# SBI Branches Customers
sbi_bank.add_customer("Balanagar", "Krisia", 14000)
sbi_bank.add_customer("Balanagar", "Peyra", 12500)
sbi_bank.add_customer("Balanagar", "Kotia", 8900)
sbi_bank.add_customer("Balanagar", "Lachlia", 27000)
sbi_bank.add_customer("Balanagar", "Eissen", 28400)
sbi_bank.add_customer("Balanagar", "Draya", 13600)
sbi_bank.add_customer("Balanagar", "Janna", 37600)
sbi_bank.add_customer("Balanagar", "Xandyr", 100780)
sbi_bank.add_customer("Balanagar", "Rikia", 45600)
sbi_bank.add_customer("Balanagar", "Frey", 23800)

sbi_bank.add_customer("Chityal", "Brayan Swailes", 28770)
sbi_bank.add_customer("Chityal", "Whitelaw Whitley", 67300)
sbi_bank.add_customer("Chityal", "Octavio Brent", 27044)
sbi_bank.add_customer("Chityal", "Alcot Townsend", 67300)
sbi_bank.add_customer("Chityal", "Spence Sydney", 276400)
sbi_bank.add_customer("Chityal", "Bozo Melton", 37600)
sbi_bank.add_customer("Chityal", "Kastor Hornsby", 28770)
sbi_bank.add_customer("Chityal", "Claudde Bentham", 56200)
sbi_bank.add_customer("Chityal", "Silvestre Harrison", 67400)
sbi_bank.add_customer("Chityal", "Darin Chatham", 6490)

sbi_bank.add_customer("KarimNagar", "Willi Rodney", 28900)
sbi_bank.add_customer("KarimNagar", "Verdell Barney", 78300)
sbi_bank.add_customer("KarimNagar", "Nikolas Bristol", 17800)
sbi_bank.add_customer("KarimNagar", "Chadwick Burbridge", 38700)
sbi_bank.add_customer("KarimNagar", "Tibault Chatham", 56000)
sbi_bank.add_customer("KarimNagar", "Per Blankley", 236500)
sbi_bank.add_customer("KarimNagar", "Wolter Altham", 78400)
sbi_bank.add_customer("KarimNagar", "Timothy Withers", 89302)
sbi_bank.add_customer("KarimNagar", "Jeremias Bush", 78400)
sbi_bank.add_customer("KarimNagar", "Stanmore Garfield", 12900)

sbi_bank.add_customer("Nalgonda", "Claudine Colby", 23670)
sbi_bank.add_customer("Nalgonda", "Silvina Byron", 78400)
sbi_bank.add_customer("Nalgonda", "Berty Bradshaw", 12789)
sbi_bank.add_customer("Nalgonda", "Lily Shelly", 45790)
sbi_bank.add_customer("Nalgonda", "Kunigunde Abram", 124780)
sbi_bank.add_customer("Nalgonda", "Dennise Hallewell", 23674)
sbi_bank.add_customer("Nalgonda", "Xavierra Hayden", 28750)
sbi_bank.add_customer("Nalgonda", "Silja Stansfield", 76590)
sbi_bank.add_customer("Nalgonda", "Friederika Lancaster", 59099)
sbi_bank.add_customer("Nalgonda", "Bryana Stanley", 78565)

sbi_bank.add_customer("Medchal", "Ashton Atterton", 470990)
sbi_bank.add_customer("Medchal", "Ronald Prescott", 54900)
sbi_bank.add_customer("Medchal", "Brenton Peddle", 34500)
sbi_bank.add_customer("Medchal", "Alphonsus Byron", 42900)
sbi_bank.add_customer("Medchal", "Tybalt Thorp", 27800)
sbi_bank.add_customer("Medchal", "Griswold Springfield", 67500)
sbi_bank.add_customer("Medchal", "Donovan Clark", 45670)
sbi_bank.add_customer("Medchal", "Jürgen Mendenhall", 376500)
sbi_bank.add_customer("Medchal", "Jarred Soames", 65790)
sbi_bank.add_customer("Medchal", "Vasco Kendall", 78560)

# HDFC Branches Customers **************************

hdfc_bank.add_customer("Hyderguda", "Branson", 99780)
hdfc_bank.add_customer("Hyderguda", "Kaylie Churchill", 54600)
hdfc_bank.add_customer("Hyderguda", "Bobby Watt", 34600)
hdfc_bank.add_customer("Hyderguda", "Cherine Outerbridge", 67500)
hdfc_bank.add_customer("Hyderguda", "Renee Lester", 87564)
hdfc_bank.add_customer("Hyderguda", "Lavernia Luxford", 789354)
hdfc_bank.add_customer("Hyderguda", "Clementina Soames ", 67300)
hdfc_bank.add_customer("Hyderguda", "Silvette Crompton", 36450)
hdfc_bank.add_customer("Hyderguda", "Hidie Harrington", 62350)
hdfc_bank.add_customer("Hyderguda", "Dania Chatham", 45630)

hdfc_bank.add_customer("Koti", "Creighton Goodwin", 23560)
hdfc_bank.add_customer("Koti", "Garan Colby", 654780)
hdfc_bank.add_customer("Koti", "Jagger Cromwell", 35460)
hdfc_bank.add_customer("Koti", "Enes Sydney", 456300)
hdfc_bank.add_customer("Koti", "Jean-Luca Williams", 26489)
hdfc_bank.add_customer("Koti", "Bodil Denholm", 65478)
hdfc_bank.add_customer("Koti", "Garlan Ramsay", 65490)
hdfc_bank.add_customer("Koti", "Fernando Lancaster", 675890)
hdfc_bank.add_customer("Koti", "Sadddique Currington", 35460)
hdfc_bank.add_customer("Koti", "Giso Smit", 65290)

hdfc_bank.add_customer("Abids", "Parkley Lester", 23560)
hdfc_bank.add_customer("Abids", "Jarvey Hastings", 56490)
hdfc_bank.add_customer("Abids", "Roland Myerscough", 25369)
hdfc_bank.add_customer("Abids", "Dorkas Smith", 536490)
hdfc_bank.add_customer("Abids", "Germain Brent", 564389)
hdfc_bank.add_customer("Abids", "Kendall Tindall", 25604)
hdfc_bank.add_customer("Abids", "Gerrit Williams", 53200)
hdfc_bank.add_customer("Abids", "Elmer Keats", 45270)
hdfc_bank.add_customer("Abids", "Harri Smither", 42389)
hdfc_bank.add_customer("Abids", "Harland Alden", 67490)

hdfc_bank.add_customer("Bazaarghat", "Eudokia Braxton", 64590)
hdfc_bank.add_customer("Bazaarghat", "Eartha Birkenhead", 78300)
hdfc_bank.add_customer("Bazaarghat", "Cindy Elton", 526300)
hdfc_bank.add_customer("Bazaarghat", "Trine Padley", 56380)
hdfc_bank.add_customer("Bazaarghat", "Sofie Stonebridge", 52620)
hdfc_bank.add_customer("Bazaarghat", "Makenzie Harding", 61700)
hdfc_bank.add_customer("Bazaarghat", "Tessa Harley", 16700)
hdfc_bank.add_customer("Bazaarghat", "Lilith Dukes", 27390)
hdfc_bank.add_customer("Bazaarghat", "Ronny Alvingham", 516200)
hdfc_bank.add_customer("Bazaarghat", "Chelsey Mildenhall", 125630)

hdfc_bank.add_customer("Kachiguda", "Beardsley Brown", 326740)
hdfc_bank.add_customer("Kachiguda", "Johnson Ashley", 76290)
hdfc_bank.add_customer("Kachiguda", "Paulus Altham", 526380)
hdfc_bank.add_customer("Kachiguda", "Paxon Addington", 67309)
hdfc_bank.add_customer("Kachiguda", "Gerome Brooks", 526390)
hdfc_bank.add_customer("Kachiguda", "Durant Sheldon", 56300)
hdfc_bank.add_customer("Kachiguda", "Raghnall Springfield", 67190)
hdfc_bank.add_customer("Kachiguda", "Christien Paddle", 67250)
hdfc_bank.add_customer("Kachiguda", "Beal Ward", 65340)
hdfc_bank.add_customer("Kachiguda", "Shaw Ridley", 54600)

# ICICI Branches Customers **************************

icici_bank.add_customer("Himayat Nagar", "Krisia", 143400)
icici_bank.add_customer("Himayat Nagar", "Peyra", 14500)
icici_bank.add_customer("Himayat Nagar", "Kotia", 8900)
icici_bank.add_customer("Himayat Nagar", "Lachlia", 27000)
icici_bank.add_customer("Himayat Nagar", "Eissen", 284300)
icici_bank.add_customer("Himayat Nagar", "Draya", 13600)
icici_bank.add_customer("Himayat Nagar", "Janna", 37630)
icici_bank.add_customer("Himayat Nagar", "Xandyr", 100780)
icici_bank.add_customer("Himayat Nagar", "Rikia", 45600)
icici_bank.add_customer("Himayat Nagar", "Frey", 238450)

icici_bank.add_customer("Nampally", "Brayan", 287560)
icici_bank.add_customer("Nampally", "Whitley", 673400)
icici_bank.add_customer("Nampally", "Octavio Brent", 27044)
icici_bank.add_customer("Nampally", "Alcot ", 67300)
icici_bank.add_customer("Nampally", "Spence ", 2764670)
icici_bank.add_customer("Nampally", "Melton", 37600)
icici_bank.add_customer("Nampally", "Hornsby", 283470)
icici_bank.add_customer("Nampally", "Claudde ", 56200)
icici_bank.add_customer("Nampally", "Silvestre ", 67400)
icici_bank.add_customer("Nampally", "Darin ", 6490)

icici_bank.add_customer("Begumpet", "Willi Rodney", 28900)
icici_bank.add_customer("Begumpet", "Verdell", 78300)
icici_bank.add_customer("Begumpet", "Nikolas", 677800)
icici_bank.add_customer("Begumpet", "Chadwick", 38700)
icici_bank.add_customer("Begumpet", " Chatham", 56000)
icici_bank.add_customer("Begumpet", "Per", 236500)
icici_bank.add_customer("Begumpet", "Wolter", 786700)
icici_bank.add_customer("Begumpet", "Timothy", 89302)
icici_bank.add_customer("Begumpet", "Jeremias", 78400)
icici_bank.add_customer("Begumpet", " Garfield", 12900)

icici_bank.add_customer("Badichowdi", "Claudine", 23670)
icici_bank.add_customer("Badichowdi", "Silvina Byron", 787800)
icici_bank.add_customer("Badichowdi", "Berty ", 12789)
icici_bank.add_customer("Badichowdi", "Lily ", 45790)
icici_bank.add_customer("Badichowdi", "Kunigunde Abram", 124780)
icici_bank.add_customer("Badichowdi", "Hallewell", 2335674)
icici_bank.add_customer("Badichowdi", "Xavierra Hayden", 28750)
icici_bank.add_customer("Badichowdi", "Stansfield", 76590)
icici_bank.add_customer("Badichowdi", "Friederika", 59099)
icici_bank.add_customer("Badichowdi", "Stanley", 78565)

icici_bank.add_customer("Gachbowli", "Ashton", 470990)
icici_bank.add_customer("Gachbowli", "Ronald", 549500)
icici_bank.add_customer("Gachbowli", "Brenton Peddle", 34500)
icici_bank.add_customer("Gachbowli", "Byron", 42900)
icici_bank.add_customer("Gachbowli", "Tybalt", 278020)
icici_bank.add_customer("Gachbowli", "Griswold", 67500)
icici_bank.add_customer("Gachbowli", "Clark", 45670)
icici_bank.add_customer("Gachbowli", "Jürgen", 3726500)
icici_bank.add_customer("Gachbowli", "Jarred Soames", 65790)
icici_bank.add_customer("Gachbowli", "Kendall", 785760)

# UNION Branches Customers **************************

union_bank.add_customer("Banjara Hills", "Branson", 239780)
union_bank.add_customer("Banjara Hills", "Kaylie Churchill", 546454)
union_bank.add_customer("Banjara Hills", "Bobby Watt", 343870)
union_bank.add_customer("Banjara Hills", "Cherine", 36374)
union_bank.add_customer("Banjara Hills", "Renee Lester", 27462)
union_bank.add_customer("Banjara Hills", "Lavernia", 826478)
union_bank.add_customer("Banjara Hills", "Clementina Soames ", 67624)
union_bank.add_customer("Banjara Hills", "Silvette", 27467)
union_bank.add_customer("Banjara Hills", "Hidie Harrington", 24435)
union_bank.add_customer("Banjara Hills", "Dania", 45636)

union_bank.add_customer("Bowenpally", "Creighton", 235460)
union_bank.add_customer("Bowenpally", "Garan Colby", 6544540)
union_bank.add_customer("Bowenpally", "Jagger", 3545760)
union_bank.add_customer("Bowenpally", "Enes Sydney", 4426300)
union_bank.add_customer("Bowenpally", "Jean-Luca ", 245489)
union_bank.add_customer("Bowenpally", "Bodil Denholm", 654688)
union_bank.add_customer("Bowenpally", "Garlan Ramsay", 89375)
union_bank.add_customer("Bowenpally", "Fernando", 6748890)
union_bank.add_customer("Bowenpally", "Sadddique", 892764)
union_bank.add_customer("Bowenpally", "Giso Smit", 37857)

union_bank.add_customer("Chikkadapally", "Parkley Lester", 23560)
union_bank.add_customer("Chikkadapally", "Jarvey Hastings", 56490)
union_bank.add_customer("Chikkadapally", "Roland", 25369)
union_bank.add_customer("Chikkadapally", "Dorkasith", 536490)
union_bank.add_customer("Chikkadapally", "Germain", 564389)
union_bank.add_customer("Chikkadapally", "Kendall", 25604)
union_bank.add_customer("Chikkadapally", "Gerrit", 53200)
union_bank.add_customer("Chikkadapally", "Elmer Keats", 45270)
union_bank.add_customer("Chikkadapally", "Harri", 42389)
union_bank.add_customer("Chikkadapally", "Harland Alden", 67490)

union_bank.add_customer("Dilsukh Nagar", "Eudokia Braxton", 6470990)
union_bank.add_customer("Dilsukh Nagar", "Eartha", 78300)
union_bank.add_customer("Dilsukh Nagar", "Cindy Elton", 52630)
union_bank.add_customer("Dilsukh Nagar", "Trine", 565480)
union_bank.add_customer("Dilsukh Nagar", "Sofie", 52620)
union_bank.add_customer("Dilsukh Nagar", "Makenzie Harding", 61700)
union_bank.add_customer("Dilsukh Nagar", "Tessa Harley", 167090)
union_bank.add_customer("Dilsukh Nagar", "Lilithkes", 270990)
union_bank.add_customer("Dilsukh Nagar", "Ronny", 516200)
union_bank.add_customer("Dilsukh Nagar", "Chelsey", 12946630)

union_bank.add_customer("Gayatri Nagar", "Beardsley", 326740)
union_bank.add_customer("Gayatri Nagar", "Johnson", 76290)
union_bank.add_customer("Gayatri Nagar", "Altham", 526380)
union_bank.add_customer("Gayatri Nagar", "Paxon Addington", 67309)
union_bank.add_customer("Gayatri Nagar", "Gerome", 526390)
union_bank.add_customer("Gayatri Nagar", "Durant Sheldon", 56300)
union_bank.add_customer("Gayatri Nagar", "Raghnall", 67190)
union_bank.add_customer("Gayatri Nagar", "Christien Paddle", 67250)
union_bank.add_customer("Gayatri Nagar", "Beal Ward", 65340)
union_bank.add_customer("Gayatri Nagar", "Shaw Ridley", 54600)

# AXIS Branches Customers **************************

axis_bank.add_customer("Rudraram", "Michael", 354673)
axis_bank.add_customer("Rudraram", "Johhny", 25615)
axis_bank.add_customer("Rudraram", "Kanne", 98253)
axis_bank.add_customer("Rudraram", "Jordan", 78152)
axis_bank.add_customer("Rudraram", "Kanam", 987265)
axis_bank.add_customer("Rudraram", "Knvindha", 982534)
axis_bank.add_customer("Rudraram", "Angela", 846632)
axis_bank.add_customer("Rudraram", "Stunnerd", 126352)
axis_bank.add_customer("Rudraram", "Jonamy", 452562)
axis_bank.add_customer("Rudraram", "Kussai", 675645)

axis_bank.add_customer("Saifabad", "Funnete", 652783)
axis_bank.add_customer("Saifabad", "Hunnay", 56172)
axis_bank.add_customer("Saifabad", "German Steve", 887921)
axis_bank.add_customer("Saifabad", "Sholeye", 29382)
axis_bank.add_customer("Saifabad", "Kanmen", 78723)
axis_bank.add_customer("Saifabad", "Jordan Kanish", 478383)
axis_bank.add_customer("Saifabad", "Quert Kane", 735528)
axis_bank.add_customer("Saifabad", "Williamson", 487432)
axis_bank.add_customer("Saifabad", "John", 687793)
axis_bank.add_customer("Saifabad", "Fedbika", 256578)

axis_bank.add_customer("Ramkote", "Kanne", 67329)
axis_bank.add_customer("Ramkote", "Hunnai", 84157)
axis_bank.add_customer("Ramkote", "Loaiky", 2325557)
axis_bank.add_customer("Ramkote", "Kaiily", 265247)
axis_bank.add_customer("Ramkote", "Humano", 889111)
axis_bank.add_customer("Ramkote", "Qwerty", 900000)
axis_bank.add_customer("Ramkote", "KaneSon", 627334)
axis_bank.add_customer("Ramkote", "Lilly", 7246200)
axis_bank.add_customer("Ramkote", "Poperry", 2893230)
axis_bank.add_customer("Ramkote", "Loilo", 100002)

axis_bank.add_customer("Nuzividu", "Enteian", 27800)
axis_bank.add_customer("Nuzividu", "Antony", 47627)
axis_bank.add_customer("Nuzividu", "Knanneli", 67463)
axis_bank.add_customer("Nuzividu", "Broster", 36746)
axis_bank.add_customer("Nuzividu", "Barak", 36737)
axis_bank.add_customer("Nuzividu", "Chinni", 97832)
axis_bank.add_customer("Nuzividu", "Meyalam", 79973)
axis_bank.add_customer("Nuzividu", "Hojn", 3939725)
axis_bank.add_customer("Nuzividu", "Kiae", 85792)
axis_bank.add_customer("Nuzividu", "Jeff", 823926)

axis_bank.add_customer("Kukatpally", "Chotia", 462427)
axis_bank.add_customer("Kukatpally", "Unnai", 386800)
axis_bank.add_customer("Kukatpally", "Feffhoz", 3637600)
axis_bank.add_customer("Kukatpally", "Sachin", 32235)
axis_bank.add_customer("Kukatpally", "Michael", 82682)
axis_bank.add_customer("Kukatpally", "Unaity", 1272736)
axis_bank.add_customer("Kukatpally", "Gosey", 27470)
axis_bank.add_customer("Kukatpally", "Wunart", 390000)
axis_bank.add_customer("Kukatpally", "Chubbed", 79338)
axis_bank.add_customer("Kukatpally", "Jeffy", 383598)

#   **************** End *********************

with open("bank_data.pkl", 'wb') as bank_data:
    pickle.dump(sbi_bank, bank_data)
    pickle.dump(hdfc_bank, bank_data)
    pickle.dump(icici_bank, bank_data)
    pickle.dump(union_bank, bank_data)
    pickle.dump(axis_bank, bank_data)


# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")


# bank1 = Bank("National Bank")
# bank1.add_branch("something")
# bank1.add_customer("something", "Vishwanth", 200)
# bank1.add_customer("something", "hima", 280)
# bank1.add_customer("something", "rishi", 190)
# bank1.add_customer_transaction("something", "Vishwanth", 789)
# bank1.add_customer_transaction("something", "rishi", 689)
#
# bank1.list_branch_customers("something", True)
# bank1.list_branch_customers("something", False)



# branch1 = Branch("SBI")
# branch1.new_customer("Vishwanth", 200)
# branch1.new_customer("Vishwanth", 302)
# branch1.new_customer("Hima", 23)
# branch1.list_customers()
# branch1.add_customer_transaction("Vishwanth", 9999)
# branch1.list_customers()


#
# c1 = Customer("Vishwanth", 20)
# print(c1.get_transactions())
# print(c1.get_name())
# c1.add_transaction(30)
# print(c1.get_transactions())
# c2 = Customer("Hima", 340)
# c2.add_transaction(47)
# print(c2.get_transactions())
# print(c2.get_name())
# print(c1.get_name())
