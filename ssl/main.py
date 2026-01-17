#virus total malware scanning script
import requests
import argparse
import os
import time
import json

# enter your private key here from virus total
key = 'c795b3b75916a9832cbbf495a65386c4e87a16bcbc111ad2f99aaabec035fbfe'

# validate hash passed by user by checking its length
def checkhash(hsh):
        try:
                if len(hsh) == 32:
                        return hsh
                elif len(hsh) == 40:
                        return hsh
                elif len(hsh) == 64:
                        return hsh
                else:
                        print ("The Hash input does not appear valid.")
                        exit()
        except Exception:
                        print ('There is something wrong with your hash \n' + Exception)

def main():
        parser = argparse.ArgumentParser(description="Virus Total Hash Check by  Mitul M Narotam")
        parser.add_argument('-o', '--output', required=True, help='Output File Location EX: /Home/Desktop/output.txt ')
        parser.add_argument('-H', '--hash', type=checkhash, required=False, help='Single Hash EX: d41d8cd98f00b204e9800998ecf8427e')
        parser.add_argument('-u', '--unlimited', action='store_const', const=1, required=False, help='Changes the 26 second sleep timer to 1.')
        args = parser.parse_args()

        #Run for hash + key
        if args.hash and key:
                file = open(args.output,'w+')
                file.write('\n\nBelow is the identified malicious hash.\n\n')
                file.close()
                VT_Request(key, args.hash.rstrip(), args.output)

def VT_Request(key, hash, output):
        params = {'apikey': key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        x = str(json_response)
        x = x.replace("'", '"')
        x = x.replace("False", '"False"')
        x = x.replace("True", '"True"')
        x = x.replace("None", '"None"')

        parsed = json.loads(x)

        print("s-au detectat "+ str(len(parsed["scans"]))+" vendori")


if __name__ == '__main__':
        main()