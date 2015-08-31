from datetime import datetime

def createPage(jfc):
  page = "<html><head /><body><table border=1><tr><td>Date</td><td>Summary</td><td>Precip Probability</td><td>Temperature</td><td>humidity</td></tr>"
  for idx in range(len(jfc["hourly"]["data"])):
     page += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % ( datetime.fromtimestamp(jfc["hourly"]["data"][idx]["time"]).strftime('%Y-%m-%d %H:%M:%S'),jfc["hourly"]["data"][idx]["summary"],jfc["hourly"]["data"][idx]["precipProbability"],jfc["hourly"]["data"][idx]["temperature"],jfc["hourly"]["data"][idx]["humidity"] )
  page += "</body></html>"
  return bytes(page,'utf-8')

