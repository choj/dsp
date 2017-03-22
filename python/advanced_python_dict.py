import pandas as pd
fac_data = pd.read_csv("faculty.csv", sep=',\s|,')
fac_data.email

fac_data.email.to_csv("emails.csv", index=False)

####Q6.  Create a dictionary in the below format:
#Print the first 3 key and value pairs of the dictionary:


# clean up data

for i,deg in enumerate(fac_data.degree):
    fac_data.degree[i] = deg.split(" ")
    if len(deg) == 1:
        fac_data.degree[i] = ""

fac_data.title = fac_data.title.map(lambda t: " ".join([word for word \
in t.split() if len(word) > 3]))


# generate lastname directory
lastname_dir = {}
for i,row in fac_data.iterrows():
    lastname = row[0].split()[-1]
    
    lastname_dir[lastname] = lastname_dir.get(lastname, [])
    lastname_dir[lastname].append([" ".join(row[1]) , " ".join(row[2].split()[0:-1]), row.email])



# generate first & last name directory
fullname_dir = {}
for i,row in fac_data.iterrows():
    firstname, lastname = row[0].split()[0], row[0].split()[-1]
    fullname = (firstname, lastname)
    fullname_dir[fullname] = [" ".join(row[1]) , " ".join(row[2].split()[0:-1]), row.email]
