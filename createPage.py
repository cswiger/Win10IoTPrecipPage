from json import loads
from datetime import datetime

def createPage(jfc):
  page = "<html><head/><body><table border=1><tr><td>Date</td><td>Precip Probability</td></tr>"
  for idx in range(len(jfc["hourly"]["data"])):
     page += "<tr><td>%s</td><td>%s</td></tr>" % (jfc["hourly"]["data"][idx]["precipProbability"],datetime.fromtimestamp(jfc["hourly"]["data"][idx]["time"]).strftime('%Y-%m-%d %H:%M:%S') )
  page += "</body></html>"
  return bytes(page,'utf-8')

