print ("Welcome to bibliography creator 1.0.0");
print ("Created by Evan Pratten");
borw = input ("Are you using a 'Book' or a 'Website'? >>");
if borw == 'Book':
	fname = input ("What is the author's first name?>>");
	lname = input ("What is the authors' last name?>>")
	title = input ("What is the title of the book?>>")
	pubname = input ("What is the name of the publisher?>>")
	pubyear = input ("What year was this book published?>>")
	med = input ("Is the book an 'Ebook' an 'Audiobook' or 'Print'?>>")




	print(lname, ",", fname, ",", title, ",", pubname, ",", pubyear, ",", med)
	exit = input ("After you have copied the text above press ENTER to exit")
else:
	fname = input ("What is the author's first name?>>");
	lname = input ("What is the authors' last name?>>")
	title = input ("What is the title of the webpage?>>")
	domain = input ("What is the domain name (eg. cnn.com)?>>")
	pubyear = input ("What date was this page published?>>")
	med = 'website'




	print(lname, ",", fname, ",", title, ",", domain, ",", pubyear, ",", med)
	exit = input ("After you have copied the text above press ENTER to exit")
