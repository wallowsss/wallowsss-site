from model import Profile
from model import Services

from google.appengine.ext import db

def config():
  profile = Profile(name = "Wallowsss")
  profile.title = "...a geek dreamer..."
  profile.subtitle = "I'm a human that promised to himself that will realize all dreams that had been dreamed."
  profile.description = "I'm starting again in my professional life as trainee of an important global consulting, before that I was a Programmer Analyst. Studying information security mobile, project management, some programming languages and all important things that I'm sure are bringing benefits to my growth."
  profile.put()
  services = Services(service = "Twitter")
  services.tumbnail = "/images/twitter.png"
  services.link = "http://www.twitter.com/wallowsss"
  services.put()
  services = Services(service = "Facebook")
  services.tumbnail = "/images/facebook.png"
  services.link = "http://www.facebook.com/wallowsss"
  services.put()
  services = Services(service = "Google Plus")
  services.tumbnail = "/images/gplus.png"
  services.link = "http://www.google.com/profiles/coutinho90"
  services.put()
  services = Services(service = "Linkedin")
  services.tumbnail = "/images/linkedin.png"
  services.link = "http://br.linkedin.com/in/wallacebarbosa"
  services.put()


if __name__ == '__main__':
  config()

