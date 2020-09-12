#!/usr/bin/python3

from urllib.parse import urlparse, parse_qs

raw = """https://www.votetravis.com/vexpress/submit.do?
		action=display&searchType=N&electionCode=&electionDateStr=&
		criteria.firstName=DEREK&maxPollingLocationsDisplay=3&
		criteria.lastName=HINCH&criteria.vuid=&criteria.month=01&
		criteria.day=01&criteria.year=1980&earlyVoting=true&address.fullAddress=TX+&
		address.partialAddress=&address.city=&address.state=TX&address.zipcode="""

parse_qs(urlparse(raw).query)