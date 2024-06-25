import json
import logging
logging.basicConfig(level = logging.INFO)



def connect_to_mw_dict(key, dict):
  logging.info("Connecting to Merriam-Webster Dictionary")
  url = "https://dictionaryapi.com/api/v3/references/sd3/json/"+dict+"?key="+key
  print (url)


def main():
  key=os.environ["API_KEY"]
  dict= sys.argv[1] 
  outcome, result_json = connect_to_mw_dict(key, dict)


if __name__ == "__main__":
    main()