#import libs
import urllib
from bs4 import BeautifulSoup
Soup = BeautifulSoup


#what I want
districtZone = {'eixample':['la-sagrada-familia', 'el-fort-pienc', 'la-dreta-de-l-eixample','la-nova-esquerra-de-l-eixample']
                ,'horta-guinardo':['el-baix-guinardo']
                ,'sant-marti':['el-clot','el-camp-de-l-arpa-del-clot', 'el-poblenou']
                ,'les-corts':['la-maternitat-i-sant-ramon','les-corts']
               }


for district, zones in districtZone.items():
    
    for zone in zones:

        #counters
        i = 0
        pag = 1
        
        #declare url
        url = 'https://www.idealista.com/alquiler-viviendas/barcelona/'+district+'/'+zone+'/con-precio-hasta_1200/'
        print(url)
        
        #query the website and return the html to the var 'page'
        iniHtml = urllib.request.urlopen(url)

        #parse the html and store in variable 'soup'
        soup = Soup(iniHtml, 'html.parser')

        #extracting ad info from html
        numAds = soup.find_all('span',attrs={'class': 'h1-simulated'})

        print('Distinct: {}, Zone: {}'.format(district, zone))
        print("no of Ads: {}".format(int(numAds[0].get_text())))
        print("--------- urls ----------")
        
        while True:

            itemLinks = soup.find_all('a',attrs={'class': 'item-link '})

            for ilink in itemLinks:

                #ad url
                urlFlat = 'https://www.idealista.com' + ilink.get('href')
                
                try:
                    #query the ad website
                    adHtml = urllib.request.urlopen(urlFlat)
                    #parse html
                    soupAd = Soup(adHtml, 'html.parser')
                    #extract contact info
                    contactInfo = soupAd.find_all('div',attrs={'class': "advertiser-data txt-soft"})

                    strContact = str(contactInfo)

                    #print if diferent from profesional
                    if strContact.find('Profesional') == -1:
                        print("{}".format(urlFlat))

                    i += 1

                except:
                    print('broken link: {}'.format(urlFlat))
                    
            #see if we still have ads
            if i < int(numAds[0].get_text()) - 1:

                pag += 1
                url += 'pagina-' + str(pag) + '.htm'
                print(url)
                #query the website and return the html to the var 'page'
                iniHtml = urllib.request.urlopen(url)
                #parse the html and store in variable 'soup'
                soup = Soup(iniHtml, 'html.parser')

            else:
                break

print("acabao!")
