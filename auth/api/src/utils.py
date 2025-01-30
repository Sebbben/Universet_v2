from urllib.parse import urlparse, urlunparse, urlencode

class OAuth:
    def isValidClient(client_id): 
        return True

    def isValidRedirectUri(client_id, redirect_uri):
        return True

    def hasRequiredParams(params):
        return all([param in params for param in ["client_id", "redirect_uri", "response_type", "state"]])

    def isValidResponseType(response_type):
        return response_type in ["code"]

    def isValidGrantReqest(params):
        return OAuth.hasRequiredParams(params) and \
        OAuth.isValidClient(params["client_id"]) and \
        OAuth.isValidRedirectUri(params["client_id"], params["redirect_uri"]) and \
        OAuth.isValidResponseType(params["response_type"])
    

def makeUrlParamsString(params):
    

    return urlencode(params)

def addParamsToUriString(url, params): # TODO: Check for url safety
    parsedUrl = urlparse(url)

    if parsedUrl.query == "":

        parsedUrl = parsedUrl._replace(query=makeUrlParamsString(params))
    else:
        query = parsedUrl.query.split("&")
        query = {(split:=param.split("="))[0]: split[1] for param in query}

        params.update(query)
        parsedUrl = parsedUrl._replace(query=makeUrlParamsString(params))

    return urlunparse(parsedUrl)