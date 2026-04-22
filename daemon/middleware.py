
accounts = {
    "admin" : "password",
    "thienloc": "1",
    "anmap": "2"
}


def process_request(req, resp):
    if req.hook:
        print("[HttpAdapter] hook in route-path METHOD {} PATH {}".format(req.hook._route_path,req.hook._route_methods))
        #
        # TODO: handle for App hook here
        hook_response = req.hook(headers = req.headers, body = req.body)
        response = resp.build_response(req, hook_response)
    else:
        username = req.body.get("username")
        password = req.body.get("password")
        if req.method == "POST" and req.path == "/login":
            if  username in accounts:
                if password == accounts[username]:
                    req.path = "/index.html"
                    resp.headers['Set-Cookie'] = "auth={}; HttpOnly; Path=/".format(username)
                    response = resp.build_response(req)
            else:
                response = resp.build_unauthorized()
        elif req.method == "GET":
            if req.path == "/" or req.path == "/index.html":
                if req.cookies and req.cookies.get("auth") in accounts:
                    req.path = "/index.html"
                else:
                    req.path = "/login.html"
            elif not req.cookies:
                req.path = "/login.html"

            response = resp.build_response(req)
    
    return response