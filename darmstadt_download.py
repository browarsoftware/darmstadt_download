from urllib.request import urlretrieve
import os
import time
from termcolor import colored

#####################################################

def prepare_lsa():
    lsa_list_int = [1,2,3,5,6,7,8,9,10,
                    11,12,13,15,16,17,19,20,
                    21,22,23,24,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40,
                    41,42,43,44,45,46,47,48,49,50,
                    51,52,53,54,55,56,57,58,59,
                    61,62,63,64,65,
                    66,#w dniu 04.02.2024 to nie działało
                    67,68,69,70,
                    71,72,73,74,75,76,77,78,79,80,
                    81,82,83,84,85,86,87,88,89,90,
                    93,94,95,96,97,98,99,100,
                    101,102,103,104,105,107,108,110,
                    111,112,113,114,115,116,117,118,119,
                    124,125,126,127,
                    130,131,134,135,136,
                    137,#w dniu 04.02.2024 to nie działało
                    139,140,
                    141,142,145,146,147,149,150,
                    151,153,154,155,159,160,
                    161,162,163,164,166,169,170,
                    171,172,173,174,
                    181,182,185,
                    200
                    ]

    lsa_list_str = []

    for l in lsa_list_int:
        my_number = str(l)
        if len(my_number) == 1:
            my_number = "%20%20" + my_number
        else:
            if len(my_number) == 2:
                my_number = "%20" + my_number
        lsa = "A" + my_number
        lsa_list_str.append(lsa)

    lsa_list_str.append("BSA225")
    lsa_list_str.append("BSA232")
    lsa_list_str.append("BSA900")
    lsa_list_str.append("BSA901")
    lsa_list_str.append("BSA905")
    lsa_list_str.append("BSA914")
    lsa_list_str.append("BSA915")
    lsa_list_str.append("Alle%20LSA%27s")
    return lsa_list_str

def download_from_darmstadt(lsa_list_str,
    path_to_data = 'd:/data/darmstadt/data/',
    start_date = '2024-01-27',
    end_date = '2024-01-28',
    start_time = '00:00:00.000',
    end_time = '00:00:00.000'):

    #start_time = end_time = '00:00:00.000'

    folder_name = path_to_data + start_date + "_" + end_date

    print(colored("*************************************", 'yellow'))
    print(colored("Starting download", 'yellow'))
    print(colored("*************************************", 'yellow'))

    isExist = os.path.exists(folder_name)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(folder_name)
       print("The new directory created")


    repeat_me = False
    while not repeat_me:
        for lsa in lsa_list_str:
            output_file_name = folder_name + "/" + start_date + "_" + end_date + "_" + lsa + ".csv"
            url = (
                "https://datenplattform.darmstadt.de/verkehr/apps/backend/sensordata?since=" + start_date +
                        "T" + start_time + "Z&until=" + end_date + "T" + end_time + "Z&lsa=" + lsa + "&useCustomHeaders=true"
            )

            if not os.path.isfile(output_file_name):
                try:
                    (my_path, http_object) = urlretrieve(url, output_file_name)
                    print('Successfully downloaded: ' + output_file_name)
                except:
                    print(colored("Failed to download " + output_file_name, 'red'))
                    repeat_me = True
                time.sleep(5)
        if repeat_me:
            print(colored("*************************************", 'blue'))
            print(colored("Repeating failed downloads", 'yellow'))
            print(colored("*************************************", 'blue'))

            time.sleep(60)
            repeat_me = False
        else:
            repeat_me = True

    print('Done')

#####################################################

path_to_data = 'd:/data/darmstadt/data/'

start_date = '2024-02-04'
end_date = '2024-02-05'

start_time = end_time = '00:00:00.000'
lsa_list_str = prepare_lsa()
download_from_darmstadt(lsa_list_str, path_to_data, start_date, end_date, start_time, end_time)