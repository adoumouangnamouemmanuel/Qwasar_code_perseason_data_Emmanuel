def my_csv_parser(param_1, param_2):
    ar1 = param_1.split("\n")
    tabl1 = []
    tabl2 = []

    for i in ar1[0]:
        if (i != ","):
            tabl1.append(i)
    
    for i in ar1[1]:
        if (i != ","):
            tabl2.append(i)

    result = [tabl1, tabl2]
    return result

