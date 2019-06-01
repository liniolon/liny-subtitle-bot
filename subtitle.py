import requests
from lxml import html
from time import sleep
import wget


ask = input("Start? (y/n) :")

while ask is not 'n':
    keywords = input("Enter your keywords for search: ")

    URL = "http://subtitlepedia.biz/download/viewdownload/27/index.php?option=com_search&searchword={}&searchphrase=exact&ordering=newest&areas[0]=jdownloads".format(keywords)

    page = requests.get(URL)

    doc = html.fromstring(page.text)

    path = doc.xpath('//dl[@class="search-results"]/dt[@class="result-title"]/a/@href')

    subtitle_result = len(path)
    if subtitle_result == 0:
        print("Not found")
    else:
        
        print("\n\nResult found: %d\n" % subtitle_result )

        for p in path:
            URL = "http://www.subtitlepedia.biz{}".format(p)
            page = page = requests.get(URL)
            doc = html.fromstring(page.text)
            
            download_path = doc.xpath('//*/a[@class="jd_download_url"]/@href')
            title_path = doc.xpath('//*/div[@class="jdtitle"]/h2/text()')
           
            for i in download_path:
                for j in title_path:
                    print("{}\n>>> http://www.subtitlepedia.biz{}".format(j, i))
                 
                break
				
			
			#index_subtitle = int(input("Download which one? "))
			#for i in download_pa
				
			
                
            


        ask = input("Start? (y/n) :")

        if ask is 'n':
            print("Goodbye ...")
            sleep(3)
            break