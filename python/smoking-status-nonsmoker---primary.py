# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"137..11","system":"readv2"},{"code":"1371.11","system":"readv2"},{"code":"1372.11","system":"readv2"},{"code":"137A.00","system":"readv2"},{"code":"137B.00","system":"readv2"},{"code":"137H.00","system":"readv2"},{"code":"137I000","system":"readv2"},{"code":"137J.00","system":"readv2"},{"code":"137L.00","system":"readv2"},{"code":"137N.00","system":"readv2"},{"code":"137O.00","system":"readv2"},{"code":"137P.00","system":"readv2"},{"code":"137P.11","system":"readv2"},{"code":"137R.00","system":"readv2"},{"code":"137S.00","system":"readv2"},{"code":"137j.00","system":"readv2"},{"code":"137l.00","system":"readv2"},{"code":"13WF.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-nonsmoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-nonsmoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-nonsmoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
