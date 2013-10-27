import urllib2


def biauthorizeVerifyToken(user, token):
    url = (
        "http://biauthorize.com/api/verify_token/" +
        user + "/" + token
    )
    web = urllib2.urlopen(url)
    return web.read() == "true"
