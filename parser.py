import re
from collections import defaultdict

def createcsv(json_dict,filename):
  
    pattern = r"^(\S+)\s+(\S+)\s+(\S+)\s+(.*)$"

    with open(filename, "w+") as outf:

        for key in json_dict.keys():
            value_list = json_dict[key]
            for item in value_list:
                print(item)
                match = re.match(pattern,item)
                
                group1 = match.group(1)
                group2 = match.group(2)
                group3 = match.group(3)
                group4 = match.group(4)

                print(group1 +", "+group2+ ", "+group3 + ", "+ group4) 
                outf.write(key+", "+group1 +", "+group2+ ", "+group3 + ", "+ group4)
                outf.write("\n")



def read_file(filename):
    print("Reading file")
    with open(filename,'r') as f:

        outputfile = "results_"+filename+".txt"

        with open(outputfile, "w") as outf:
        
            dict_scan_results = defaultdict(list)
            target = ""
            line = f.readline()
            while line:
                match = re.match(r'^(Nmap scan report for)(.*)', line)
                if match:
                    target = match.group(2)

                else:
                    match2 = re.match(r'^(\d{1,8}\/)', line)
                    if match2:
                        dict_scan_results[target].append(line)
                
                line=f.readline()

            #print(dict_scan_results)
            return dict_scan_results

if __name__ == "__main__":
    json_dict1 = read_file("ms-160-1-15.xml")
    createcsv(json_dict1, "ms-160-1-15.csv")

    json_dict2 = read_file("ms-160-16-31.xml")
    createcsv(json_dict2, "ms-160-16-31.csv")

    json_dict3 = read_file("ms-160-32-47.xml")
    createcsv(json_dict3, "ms-160-32-47.csv")

    json_dict4 = read_file("ms-160-48-63.xml")
    createcsv(json_dict4, "ms-160-48-63.csv")

    json_dict5 = read_file("ms-160-48-79.xml")
    createcsv(json_dict5, "ms-160-48-79.csv")

    json_dict6 = read_file("ms-160-80-95.xml")
    createcsv(json_dict6, "ms-160-80-95.csv")

    json_dict7 = read_file("ms-160-96-111.xml")
    createcsv(json_dict7, "ms-160-96-111.csv")

    json_dict8 = read_file("ms-160-112-127.xml")
    createcsv(json_dict8, "ms-160-112-127.csv")

    json_dict9 = read_file("ms-160-128-143.xml")
    createcsv(json_dict9, "ms-160-128-143.csv")

    json_dict10 = read_file("ms-160-144-159.xml")
    createcsv(json_dict10, "ms-160-144-159.csv")

    json_dict11 = read_file("ms-160-160-175.xml")
    createcsv(json_dict11, "ms-160-160-175.csv")

    json_dict12 = read_file("ms-160-176-191.xml")
    createcsv(json_dict12, "ms-160-176-191.csv")

    json_dict13 = read_file("ms-160-192-207.xml")
    createcsv(json_dict13, "ms-160-192-207.csv")

    json_dict14 = read_file("ms-160-208-223.xml")
    createcsv(json_dict14, "ms-160-208-223.csv")

    json_dict15 = read_file("ms-160-224-239.xml")
    createcsv(json_dict15, "ms-160-224-239.csv")

    json_dict16 = read_file("ms-160-240-255.xml")
    createcsv(json_dict16, "ms-160-240-255.csv")
