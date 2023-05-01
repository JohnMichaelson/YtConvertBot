import pyshorteners
import os
import requests
import validators

#defining the codes as 0, 0 represents error
#I use codes to understand through the code if any action has passed or failed, so the next part works
url_check_code = 0

#defining function that cheks if the url is reachable 
def url_checker(url):
	#global is neccesary for the variable to be modified outside the function
	global url_check_code
	try:
		get = requests.get(url)
		# if the request succeeds, I dont know why it should be 200
		if get.status_code == 200:
			url_check_code = 1
			print(f"{url}: is reachable")
		else:
			url_check_code = 0
			print(f"{url}: is Not reachable")

	except:
		url_check_code = 0
		print(f"{url}: is Not reachable")

#Using validators to check the validity of an url
def url_valid(url):
	# global is neccesary for the variable to be modified outside the function
	global url_check_code
	try:
		valid = validators.url(url)
		if valid == True:
			url_check_code = 1
			print(f"{url}: is Valid")
		else:
			url_check_code = 0
			print(f"{url}: is Not Valid")
	except:
		url_check_code = 0
		print(f"{url}: is Not Valid")

def yt_dlp(url):
	if url_check_code == 1:
		try:
			yt_dlp_audio = os.system("yt-dlp -f 140 " + str(long_url))
			print(yt_dlp_audio)
		except:
			print("Couldn't download the audio from the video")

	else:
		print("Couldn't download the audio from the video")



#TERMINAL INTERACTIONS begin here:
long_url = input("Enter the URL:")

#testing if the url is reachable
#If not, prints out that its not reachable 
url_checker(long_url)
#url_valid(long_url)

print("url_check_code is " + str(url_check_code))

#Using ytdlp to download the audio from the url
#using the long_url variable that was created in the short url function 
if url_check_code == 1:
	yt_dlp(long_url)
else:
	print("Error url_check_code is " + str(url_check_code))
