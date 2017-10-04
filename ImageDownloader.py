from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import argparse

class ImageDownloader:
        #addrs is a list of image's address 
	def __init__(self,path,addrs,class_name,size,format):
		self.addrs = addrs
		self.class_name = class_name
		self.path = path
		self.size = size
		self.format = format

	def import_image(self,addr):
		file = BytesIO(urlopen(addr).read())
		return Image.open(file)

	def download(self,list_heuristics):
		for img_addr in self.addrs:
			img = self.import_image(img_addr)
			valide_img = True
			for h in list_heuristics:
				if not h(img):
					valide_img = False
					break
			if valide_img:
				self.save_image(img,0)

	def save_image(self,image,id):
		image.thumbnail(self.size)
		image.save("{0}/{1}_{2}_{3}x{4}".format(self.path,self.class_name,id,self.size[0],self.size[1]),self.format)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Download a images from a list of url")
	parser.add_argument("-p","--path",help="The path where you'll store your images")
	parser.add_argument("-f","--format",help="The format in which you'll encode your images")
	parser.add_argument("-s","--size",help="d1xd2 the size in which you'll resize your image before save it on on your disk")
	args = parser.parse_args()
	d1 = int(args.size.split("x")[0])
	d2 = int(args.size.split("x")[1])
	img_dl = ImageDownloader(args.path,["https://cdn.pixabay.com/photo/2017/02/07/16/47/kingfisher-2046453_960_720.jpg"],"bird",(d1,d2),args.format)
	img_dl.download([])



