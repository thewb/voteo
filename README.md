# voteo
Voteo is a Flask application that searches voter records databases to build a database conatining voter information. 
Currently, voteo only works with Austin, Texas (Travis County); and Seattle, Washington (King County) voter records databases. 
 
```Future plans``` 
* Include more counties/parishes and states to compare the amount of information different places provide
about voters.
 
```Reasoning```
* Each county, or parish, and state in the country choose what information to reveal about voters. It should be minimal. 

* Each county, or parish, and state in the country use a different type of authentication scheme. For example, California requires Date of Birth and California ID number or the last four of a Social Security Number. Louisiana requires First name, Last name, Zip code, and Birth Month and Year. Like Texas and King County, Oregon uses a system that requires First Name, Last Name and Date of Birth. But The Oregon system uses a CSRF token and a session ID with a 30 minute timeout. 

* Among information revealed by Texas, and Washington are address, date of birth, and name. Whereas Louisiana 
provides party information, and does not reveal addresses. So far Travis county reveals the most information, but there is no consistency among systems.

```Changes that should be made```

* A federal information security standard should be created. It should include periodic penetration tests. 

* Voter records databases should only reveal minimal information. 

* Voter records databases should all require the same level of authentication. 

* All states/counties/parishes should reveal the same amount of information. 



