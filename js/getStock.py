import os
import re
import sys
import ystockquote
import time

from string import letters

import webapp2
import jinja2


class Handler(webapp2.RequestHandler):
    # Instead of having to write self.response.out.write everytime.
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class RenderDynamic(Handler):
    def post(self):
        self.write("{\"number\": \"five\"}")
		if request.headers['Content-Type'] == 'application/json':
			data = json.loads(request.data)
			ticker = data['ticker']
			price = ystockquote.get_price(ticker)
			returnStatement = "{\"price\": \""+str(price)+"\"}"
			self.write(returnStatement)


app = webapp2.WSGIApplication([('/render',RenderDynamic)], debug=True)