## When you run this code, images of cloud computing artcle from wikipedia will be downloaded and saved into files with names as image1.jpg etc..,
##source: https://en.wikipedia.org/wiki/Cloud_computing#:~:text=Cloud%20computing%20is%20the%20on,many%20users%20over%20the%20Internet
## Note this code may break if any wikipedia has any done any changes to the article's html


import requests,bs4


def save_images():
  result= requests.get('https://en.wikipedia.org/wiki/Cloud_computing#:~:text=Cloud%20computing%20is%20the%20on,many%20users%20over%20the%20Internet.')

  soup=bs4.BeautifulSoup(result.text,'lxml')
  link=soup.select('.thumbimage')
  count=0
  all=set()
  for i in link:
      all.add('https:'+i['src'])

  for i in all:
      count+=1
      name='image'+str(count)+'.jpg'
      image_link=requests.get(i)
      myfile= open(name,'wb')
      myfile.write(image_link.content)
      myfile.close()

if __name__ == '__main__':
    save_images()
