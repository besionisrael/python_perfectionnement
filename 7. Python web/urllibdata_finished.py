# Send data to a server using urllib

#import the request and parse modules
import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    # create some data to pass to the GET request
    args = {
        "name" : "Françoise Hardy",
        "is_author" : True
    }
    # the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)

    # issue the request with the data params as part of the URL
    result = urllib.request.urlopen(url + "?" + data)

    print("Result code: {0}".format(result.status))
    print("Returned data: ----------------------")
    print(result.read().decode("utf-8"))
    
    # issue the request with a data parameter to use POST
    url = "http://httpbin.org/post"
    data = data.encode() #Convert data to byte
    result = urllib.request.urlopen(url, data=data)

    print("Result code: {0}".format(result.status))
    print("Returned data: ----------------------")
    print(result.read().decode("utf-8"))


if __name__ == "__main__":
    main()
