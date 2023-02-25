def add_values_to_result(result, key, value):
    if value not in result[key]:
            result[key][value] = 1
        
    else:
        result[key][value] += 1


def my_data_process(input):
    result = {"Gender": {}, "Email": {}, "Age": {}, "City": {}, "Device": {}, "Order At": {}}
    for line in input[1:]:
        values = line.split(",")

        add_values_to_result(result, "Gender", values[0])
        add_values_to_result(result, "Email", values[4])
        add_values_to_result(result, "Age", values[5])
        add_values_to_result(result, "City", values[6])
        add_values_to_result(result, "Device", values[7])
        add_values_to_result(result, "Order At", values[9])
        
    return str(result).replace(", ", ",").replace(": ",":").replace("'", '"')
def run():
    input = ["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
    #print(my_data_process(input))

run()