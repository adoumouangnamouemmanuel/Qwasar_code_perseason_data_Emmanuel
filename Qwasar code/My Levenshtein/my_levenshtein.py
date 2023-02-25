def my_levenshtein(str1, str2):
    
    if len(str1) != len(str2):
        return -1

    else:
        return sum ( str1[i] != str2[i] for i in range(len(str1)) )

#print(my_levenshtein("ACCAGGG" , "ACTATGG"))