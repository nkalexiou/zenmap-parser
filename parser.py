import re
from collections import defaultdict

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

                outf.write(key+", "+group1 +", "+group2+ ", "+group3 + ", "+ group4)
                outf.write("\n")


# Reads xml zenmap output file and creates a dictionary with Key -> asset/IP and Value -> list of open ports
def read_file(filename):

    with open(filename,'r') as f:

        outputfile = "results_"+filename+".txt"
        
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

        return dict_scan_results

if __name__ == "__main__":
    json_dict1 = read_file("the_zenmap_xml_output.xml")
    createcsv(json_dict1, "csv_filename_to_create.csv")