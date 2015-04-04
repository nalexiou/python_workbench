
import multiprocessing
import mechanize
from BeautifulSoup import BeautifulSoup


def do_work(item):
	temp = str(item)
	url = "http://www.somewebaddress.com/"
	br = mechanize.Browser()
	br.set_handle_robots(False) # ignore robots
	br.open(url)
	response = br.response()
	# print response
	# for form in br.forms():
	# 	    print "Form name:", form.name
	# 	    print form
	br.select_form(nr=0) #select first form
	br.form['someformfield']= '3242'
	br.form['anotherfield']= temp
	response = br.submit()

	html = BeautifulSoup(br.response().read())
	# print html

	try:
		mymatch = html.find("span", {"id": "MainContent_lblMsg"}).text
		print "found: " + mymatch

	except:
		print "Not found: " + mymatch

if __name__ == '__main__':
	jobs =[]
	for x in range(1, 500): 
		p = multiprocessing.Process(target=do_work, args=(x,))
		jobs.append(p)
		p.start()
