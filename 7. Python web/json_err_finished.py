# Process JSON data returned from a server

# use the JSON module
import json
from json import JSONDecodeError


def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "contents" : [
                "Corned beef",
                "Sauerkraut"
                "Swiss Cheese"
            ],
            "price" : 8.99
        }'''

    try:
        # parse the JSON data using loads
        data = json.loads(jsonStr)

        # print information from the data structure
        print("Sandwich: " + data['sandwich'])
        if (data['toasted']):
            print("And it's toasted!")
        for content in data['contents']:
            print("content: " + content)
    except Exception as err:
        print("Whoops, JSON Decoding error:")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == "__main__":
    main()
