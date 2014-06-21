import json
import urllib, urllib2
from pprint import pprint

def run_query(search_terms):
    # Specify the base
    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''
    bing_api_key = 'kdiorLyLAkjJpJOhWxPWI55D9fan9H1bHXn6kxWxlJw'

    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, bing_api_key)

    # Create our results list which we'll populate.

    url ='http://data.tmsapi.com/v1/sports/all/events/airings?lineupId=USA-OTA10112&startDateTime=' + search_terms + 'Z&api_key=ubx2nk3jw3arr7tgy3q9wwcd'
    req = urllib2.urlopen(url).read()
    raw = json.loads(req)    
    #print raw
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        #json_response = json.loads(response)
        json_response = json.loads(req)
        print json_response
        # Loop through each page returned, populating out results list.
        #for result in json_response['d']['results']:
        for result in json_response:
            results.append({
                # 'title': result['program']['eventTitle'],
                'title': result['program']['eventTitle'],
                'link': "www.google.com",
                'summary': result['startTime']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results


# if __name__=="__main__":
#         print "Test Big Search"
#         print ">>>> "
#         print run_query("soccer games")[0]



#         #create a json string using json.dumps()
#         data = json.dumps(run_query("soccer games"))

#         #store the json data as a regular string
#         json_data = json.loads(data)

#         #print the first json string in the list of json strings
#         print "\n\n >> %s" % json_data[0]['title']