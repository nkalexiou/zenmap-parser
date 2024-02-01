# zenmap-parser
A python script to parse zenmap/nmap XML results and create a CSV file reports. 

First, run your nmap/Zenmap scan and output results to XML file format.

Then execute: 

```
python parse.py 
```
This creates an output folder which contains the CSV reports. The main CSV report has the following format:

| asset/ip      | port/protocol | status  | application  | information  |
| ------------- | -------------:| -------:| ------------:| ------------:|
| 192.168.10.54 | 21/tcp        | open    |     ftp     :| vsftpd 2.4  :|
| 192.168.10.55 | 22/tcp        | open    |     ssh     :| OpenSSH 6.0 :|

An additional CSV report is created and contain Operating System information. Both of these are created per NMAP XML report.

Finally, a CSV report called "all.csv" containing all CSV reports will be created.
