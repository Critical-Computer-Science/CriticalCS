def tsvDicts(fname):
    f = open(fname, "r")
    key_list = f.readline().strip().split("\t")
    print(key_list)
    d_list = []
    
    rest = f.read().strip().split("\n")
    #print(rest)
    for line in rest:
        current_dict = dict()
        d_list.append(current_dict)
        current_values = line.split("\t")
        for x, entree in enumerate(current_values):
            if entree.isdigit():
                current_values[x] = int(entree)
            elif entree.split(".")==2 and entree[0].isdigit() and entree[1].isdigit():
                current_values[x] = float(entree)
        gap = len(current_values) - len(key_list)
        for x, i in enumerate(current_values[gap:]):
            current_dict[key_list[x].lower()] = i
    return d_list

def searchByCriteria(fname, header, result=None):
    header=header.lower()
    if result==None:
        d_list = tsvDicts(fname)
        return sorted(d_list, key = lambda x: x[header])
    else:
        result=result.lower()
        d_list = tsvDicts(fname)
        return list(filter(lambda x: x[header].lower()==result.lower(), d_list))

def crossSearch(fname, header1, result1, header2, result2):
    header1, header2 = header1.lower(), header2.lower()
    result1, result2 = result1.lower(), result2.lower()
    if header1 == header2:
        raise NameError("Cannot 'crossSearch' the same criteria")
    else:
        d_list = tsvDicts(fname)
        print(header1)
        return list(filter(lambda x: (x[header1].lower()==result1 and x[header2].lower()==result2), d_list))

if __name__ == "__main__":
    print(tsvDicts("sars_final.tsv"))
    #print(searchByCriteria("data_set_1.tsv", "name"))
    #print(crossSearch("data_set_4.tsv", "gender", "female", "illness", "broken bone"))