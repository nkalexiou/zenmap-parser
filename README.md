# zenmap-parser
A python script to parse zenmap XML results and create a CSV file. 

The CSV file has the following format:

| asset/ip      | port/protocol | status  | application  | information  |
| ------------- | -------------:| -------:| ------------:| ------------:|
| 192.168.10.54 | 21/tcp        | open    |     ftp     :| vsftpd 2.4  :|
| 192.168.10.55 | 22/tcp        | open    |     ssh     :| OpenSSH 6.0 :|

Simply run 

```
python parse.py 
```

and add the filenames of the zenmap output XML files. 

