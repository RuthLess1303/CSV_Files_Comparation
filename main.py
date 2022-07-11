import os
def comparation_file():
    path = input('path: ')
    path_content = os.listdir(path)
    for file_name in path_content:
        if file_name[:6] == 'Actual':
            filtered_name = file_name[6:-4]
            added_name = 'Expected' + filtered_name +'.csv'
            if added_name in path_content:
                with open(path+'/'+added_name,'r') as file:
                    list_of_data_exp = file.readlines()
                with open(path+'/'+file_name,'r') as file1:
                    list_of_data_act = file1.readlines()
                if len(list_of_data_act) == len(list_of_data_exp):
                    for data_act in list_of_data_act:
                        if data_act not in list_of_data_exp:
                            print('{} was found in {}\nbut not in {}'.format(data_act,
                                                                             file_name,added_name))
                        else:
                            pass
                    for data_exp in list_of_data_exp:
                        if data_exp in list_of_data_act:
                            print('{} was found in {}\nbut not in {}'.format(data_exp,
                                                                             added_name,file_name))
                        else:
                            pass
                else:
                    print('Files contain different size of data')
                    if len(list_of_data_exp) > len(list_of_data_act):
                        difference = list(set(list_of_data_exp)-set(list_of_data_act))
                        print('{} has more data then {}\nList of different data: {}'.format(added_name,
                                                                                            file_name,difference))
                    elif len(list_of_data_exp) < len(list_of_data_act):
                        difference = list(set(list_of_data_act)-set(list_of_data_exp))
                        print('{} has more data then {}\nList of different data: {}'.format(file_name,
                                                                                            added_name,difference))
            else:
                return ('File {} is missing'.format(added_name))
        else:
            pass
print(comparation_file())