import re
import os
from collections import defaultdict

output_dir = "output"

# Creates a CSV file with
# asset (IP), port/protocol, status (open/closed/filtered), application, information
def createcsv(json_dict,filename):

    # Split non-whitespace groups until whitespaces are found. 
    # Matches for example 21/tcp   open    ftp  vsftpd X.X.X
    pattern = r"^(\S+)\s+(\S+)\s+(\S+)\s+(.*)$"

    with open(filename, "w+") as outf:

        for key in json_dict.keys():
            value_list = json_dict[key]
            for item in value_list:
                match = re.match(pattern,item)
                
                group1 = match.group(1)
                group2 = match.group(2)
                group3 = match.group(3)
                group4 = match.group(4)

                outf.write(key.strip()+";"+group1.strip() +";"+group2.strip()+ ";"+group3.strip()+ ";"+ group4.strip())
                outf.write("\n")

# create separate csv files with OS information
def create_os_sv(os_dict,filename):

    with open(filename, "w+") as outf:
        for key,value in os_dict.items():
            outf.write(key.strip()+";"+value.strip())
            outf.write("\n")


# Reads xml zenmap output file and creates a dictionary with Key -> asset/IP and Value -> list of open ports
def read_file(filename):
    
    with open(filename,'r') as f:
        
        dict_scan_results = defaultdict(list)
        dict_os = {}

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
                
                else:
                    #OS details: Microsoft Windows Server 202X build XXXXX - XXXXX
                    # If OS details line is found
                    if "OS details" in line:
                        match3 = re.match(r'^(OS details:)(.*)$',line)
                        
                        if match3:
                            dict_os[target]=match3.group(2).strip()
                    
                    # if not OS exact match line is found
                    elif "No exact OS matches for host" in line:
                        dict_os[target]="No exact OS matches for host"
                
            line=f.readline()

        return dict_scan_results, dict_os

def merge_files():
    if os.path.exists(output_dir):
        with open(output_dir+"/"+"all.csv", "w+") as outf:
            for csv_file in os.listdir(output_dir):
                if os.path.isfile(output_dir+"/"+csv_file) and csv_file.endswith(".csv") and not "os" in csv_file and not "all" in csv_file:
                    with open(output_dir+"/"+csv_file, "r") as inf:
                        for line in inf:
                            outf.write(line)

if __name__ == "__main__":

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if os.path.exists(output_dir):
        #Remove all files from output directory
        for file in os.listdir(output_dir):
            os.remove(output_dir+"/"+file)

    for xml_report in os.listdir(os.getcwd()):
        if os.path.isfile(xml_report) and xml_report.endswith(".xml"):
            print("Processing file: " + xml_report)
            json_dict1, os_dict1 = read_file(xml_report)
            createcsv(json_dict1, output_dir + "/" + xml_report.replace(".xml","")+".csv")
            create_os_sv(os_dict1, output_dir + "/" + xml_report.replace(".xml","")+ "_os.csv")
    
    merge_files()