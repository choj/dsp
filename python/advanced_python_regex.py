import pandas as pd


def word_count(words):
    wc = {}
    for w in words:
        wc[w] = wc.get(w, 0) + 1
    return wc

# must use regexp to match columns separated by commas, or by commas followed by a space

fac_data = pd.read_csv("faculty.csv", sep=',\s|,')

# cleanup 'degree' column by removing periods...

##
## Part 1 Q1
##

fac_data.degree = fac_data.degree.map(lambda x: x.replace('.',''))

# ...and replacing multiple degrees with a list, and switch to lowercase
for i,deg in enumerate(fac_data.degree):
    fac_data.degree[i] = deg.split(" ")

# combine all lists of degrees into one list
all_degrees = sum(fac_data.degree.tolist(),[])
all_degrees.sort()

# if degree is single character, remove
for deg in all_degrees:
    if len(deg) < 2:
        all_degrees.remove(deg)

count_degrees = word_count(all_degrees)

print("\nPart 1 Q1\n")
print("there are " + str(len(count_degrees.keys())) +" different degrees, with the following frequencies: ")
print(count_degrees)


##
## Part 1 Q2
##

# clean up "title" column by removing words shorter than 4 chars, maintain dictionary
# uses a list comprehension to look at each item in the .title series, and generate a list of words longers than three characters, then call the .join operator on each list to combine it into a word
fac_data.title = fac_data.title.map(lambda t: " ".join([word for word in t.split() if len(word) > 3]))

count_titles = word_count(fac_data.title.tolist())
print("\nPart 1 Q2\n")
print("there are " + str(len(count_titles.keys())) +" different titles, with the following frequencies: ")
print(count_titles)

##
## Part 1 Q3
##
print("\nPart 1 Q3\n")
print(fac_data.email)

##
## Part 1 Q4
##

# generate list of email domains
email_domains = fac_data.email.map(lambda d: d[d.find("@")+1:]).tolist()

count_domains = word_count(email_domains)
print("\nPart 1 Q4\n")
print("there are " + str(len(count_domains.keys())) +" different email domains, with the following frequencies: ")
print(count_domains)

