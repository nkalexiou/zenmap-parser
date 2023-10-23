# zenmap-parser
A python script to parse zenmap/nmap XML results and create a CSV file. 

Run your nmap scan and output results to XML file format.

Then simply execute 

```
python parse.py 
```
to get csv output of the most important details, which you can use further for reporting results and working further with the dataset.

The CSV file has the following format:

| asset/ip      | port/protocol | status  | application  | information  |
| ------------- | -------------:| -------:| ------------:| ------------:|
| 192.168.10.54 | 21/tcp        | open    |     ftp     :| vsftpd 2.4  :|
| 192.168.10.55 | 22/tcp        | open    |     ssh     :| OpenSSH 6.0 :|


Just don't forget to edit the names of the zenmap output XML files in the script. 
