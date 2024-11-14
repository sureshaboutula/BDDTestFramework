class Utils:

    def common_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers
    
    def common_headers_with_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers