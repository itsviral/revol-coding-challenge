import pandas as pd
import collections
import json as js
import sys
import argparse

def process_data(df , key1, key2 , key3):

    # grouping dataframe on the basis of initial key
    
    groupby_data = df.groupby([key1] , as_index= False )

    my_collection = collections.defaultdict(dict)

    # creating nested disctionaries 
    
    for item in groupby_data:

        temp = (pd.DataFrame(list(item)[1]))

        temp.set_index(key1)

        groupby_new_data = temp.groupby([key2] , as_index= False )

        for items in groupby_new_data:

            temp_dict = collections.defaultdict(dict)

            temp_df = (pd.DataFrame(list(items)[1]))
            
            # making sure all encoding are in ascii
            
            value1 = list(temp_df[key1])[0].encode("ascii", "ignore")

            value2 = list(temp_df[key1])[0].encode("ascii", "ignore")

            value3 = list(temp_df[key3])[0].encode("ascii", "ignore")

            amount = list(temp_df["amount"])[0]

            temp_dict[value2][value3] = amount

            if value1 in my_collection:

                my_collection[value1].update(temp_dict)

            else:

                my_collection[value1] = temp_dict

    sys.stdout.write(js.dumps(my_collection))
    
    sys.stdout.write("\n")
    
    sys.stdout.close()  
    
    
if __name__ == '__main__':
    
    
    # parse commandline argumets
    
    parser = argparse.ArgumentParser(description='Test app')
    
    parser.add_argument("key1", type=str,
                    help=" Enter one key from currency or country or city ")
    parser.add_argument("key2", type=str,
                    help=" Enter one key from currency or country or city. Dont repeat any key ")
    parser.add_argument("key3", type=str,
                    help=" Enter one key from currency or country or city. Dont repeat any key ")

    args = parser.parse_args()
    
    key1 = args.key1
    
    key2 = args.key2
    
    key3 = args.key3
    
    if (key1 != key2 != key3):
        
        try: 
        
            df = pd.read_json(sys.stdin)
        
            try:
                
                # pass data to process further
            
                process_data(df , key1 , key2 , key3)
            
            except:
            
                sys.stderr.write("Error in processing file")
            
        except:
        
            sys.stderr.write("Error in opening file")
    
    else:
        
        sys.stderr.write("Keys cannot be same")
        