'''
Beautiful Soup scrape of 
http://mobile311.sfgov.org/?external=false&service_id=50fea92c4aa48a4a9e000099
to get the new fire hydrant reports



'''
from bs4 import BeautifulSoup
import urllib2
import re
import string

category = 'http://mobile311.sfgov.org/?external=false&service_id=50fea92c4aa48a4a9e000099' # graffiti


def page_of_data(i):
	page_no =str(i)
	url_base = 'http://mobile311.sfgov.org/'
	url_ext = '?page='+page_no+'&'+category
	url= url_base+url_ext+'&status=open'
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),'lxml')
	#get report numbers
	reports = soup.table('span',"activity-timestamp")
	#get details from second page
	#should modify code to also get location information
	for line in reports:
		line=str(line)
		x=line.find("#")+1
		y=x+7
		z=line[x:y]
		#print z
		url_goal = url_base+"reports/"+z
		print url_goal # Debugging maybe comment out this line
		page2 = urllib2.urlopen(url_goal)
		real_soup = BeautifulSoup(page2.read())
		blockquote = real_soup('blockquote')
		for lne in blockquote:
			request_type = lne.find_next_sibling('p') 
			#print request_type
			if 'Fire hydrant'in str(request_type):
				print url_goal
				print blockquote
				pane = real_soup("div","tab-pane active")
				#kids = real_soup.findchildren("div","tab-pane active")
				for ln in pane:
					#kids = real_soup.findchildren("div","tab-pane active")	
					print ln	
					print "	kids**********************************"
				#for line in pane:
					



#end
for i in range(20):
	page_of_data(i)
