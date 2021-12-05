# Process JSON data returned from a server

# use the JSON module
import json


def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "contents" : [
                "Corned beef",
                "Sauerkraut",
                "Swiss Cheese"
            ],
            "price" : 8.99
        }'''

    # parse the JSON data using loads
    data = json.loads(jsonStr)
    print(type(data)) #Dictionnaire
    print(type(data["toasted"]))
    print(type(data["contents"]))
    print(type(data["price"]))
    

    # print information from the data structure
    print("Sandwich: " + data['sandwich'])
    if (data['toasted']):
        print("And it's toasted!")
    for content in data['contents']:
        print("content: " + content)


if __name__ == "__main__":
    main()
