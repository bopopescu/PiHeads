import urllib.request
import xml.etree.ElementTree as ET



class Predictions:
    def __init__(self, routeTag):
        self.routeTag = routeTag
        self.url = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=cyride&stopId=2530'

    def getPrediction(self):
        self.tree = ET.parse(urllib.request.urlopen(self.url))
        self.root = self.tree.getroot()
        if self.routeTag == 930:
            for elem in self.tree.iterfind('predictions[@routeTag="930"]/direction/prediction[1]'):
                seconds = elem.attrib["seconds"]

        if self.routeTag == 952:
            for elem in self.tree.iterfind('predictions[@routeTag="952"]/direction/prediction[1]'):
                seconds = elem.attrib["seconds"]

        if self.routeTag == 822:
            for elem in self.tree.iterfind('predictions[@routeTag="822"]/direction/prediction[1]'):
                seconds = elem.attrib["seconds"]

        if self.routeTag == 862:
            for elem in self.tree.iterfind('predictions[@routeTag="862"]/direction/prediction[1]'):
                seconds = elem.attrib["seconds"]

        if self.routeTag == 830:
            for elem in self.tree.iterfind('predictions[@routeTag="830"]/direction/prediction[1]'):
                seconds = elem.attrib["seconds"]

        minutes = int(seconds) // 60
        seconds = int(seconds) % 60
        return minutes,"minutes and ",seconds," seconds."