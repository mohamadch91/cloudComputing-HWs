import string
import requests
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
from .S3_helper import create_image_url
from .models import Advertisement
IMG_KEY="acc_90ccaadfac4bca7"
IMG_SECRET_KEY="daee709507bb27b5756e6dfac46b5222"
IMG_AUTH="Basic YWNjXzkwY2NhYWRmYWM0YmNhNzpkYWVlNzA5NTA3YmIyN2I1NzU2ZTZkZmFjNDZiNTIyMg=="
IMG_ENDPOINT="https://api.imagga.com"
temp_data={
  "result": {
    "tags": [
      {
        "confidence": 61.4116096496582,
        "tag": {
          "en": "mountain"
        }
      },
      {
        "confidence": 54.3507270812988,
        "tag": {
          "en": "landscape"
        }
      },
      {
        "confidence": 50.969783782959,
        "tag": {
          "en": "mountains"
        }
      },
      {
        "confidence": 46.1385192871094,
        "tag": {
          "en": "wall"
        }
      },
      {
        "confidence": 40.6059913635254,
        "tag": {
          "en": "clouds"
        }
      },
      {
        "confidence": 37.2282066345215,
        "tag": {
          "en": "sky"
        }
      },
      {
        "confidence": 36.2647514343262,
        "tag": {
          "en": "park"
        }
      },
      {
        "confidence": 35.3734092712402,
        "tag": {
          "en": "national"
        }
      },
      {
        "confidence": 35.1284828186035,
        "tag": {
          "en": "range"
        }
      },
      {
        "confidence": 34.7774543762207,
        "tag": {
          "en": "snow"
        }
      },
      {
        "confidence": 32.9128646850586,
        "tag": {
          "en": "tree"
        }
      },
      {
        "confidence": 29.5557823181152,
        "tag": {
          "en": "rock"
        }
      },
      {
        "confidence": 28.4864749908447,
        "tag": {
          "en": "trees"
        }
      },
      {
        "confidence": 28.1904907226562,
        "tag": {
          "en": "travel"
        }
      },
      {
        "confidence": 28.1532077789307,
        "tag": {
          "en": "valley"
        }
      },
      {
        "confidence": 27.2323837280273,
        "tag": {
          "en": "scenic"
        }
      },
      {
        "confidence": 25.4718055725098,
        "tag": {
          "en": "forest"
        }
      },
      {
        "confidence": 24.6589889526367,
        "tag": {
          "en": "outdoors"
        }
      },
      {
        "confidence": 23.2137584686279,
        "tag": {
          "en": "peak"
        }
      },
      {
        "confidence": 23.1196212768555,
        "tag": {
          "en": "tourism"
        }
      },
      {
        "confidence": 22.9586181640625,
        "tag": {
          "en": "outdoor"
        }
      },
      {
        "confidence": 22.5058460235596,
        "tag": {
          "en": "canyon"
        }
      },
      {
        "confidence": 21.1684589385986,
        "tag": {
          "en": "stone"
        }
      },
      {
        "confidence": 20.7627124786377,
        "tag": {
          "en": "scenery"
        }
      },
      {
        "confidence": 19.8215427398682,
        "tag": {
          "en": "cloud"
        }
      },
      {
        "confidence": 19.6833038330078,
        "tag": {
          "en": "river"
        }
      },
      {
        "confidence": 19.4671821594238,
        "tag": {
          "en": "desert"
        }
      },
      {
        "confidence": 18.9360198974609,
        "tag": {
          "en": "environment"
        }
      },
      {
        "confidence": 16.9691829681396,
        "tag": {
          "en": "rocks"
        }
      },
      {
        "confidence": 16.6996059417725,
        "tag": {
          "en": "lake"
        }
      },
      {
        "confidence": 16.6136302947998,
        "tag": {
          "en": "cliff"
        }
      },
      {
        "confidence": 16.5426540374756,
        "tag": {
          "en": "geology"
        }
      },
      {
        "confidence": 15.9809865951538,
        "tag": {
          "en": "wilderness"
        }
      },
      {
        "confidence": 15.4057178497314,
        "tag": {
          "en": "hiking"
        }
      },
      {
        "confidence": 14.7685861587524,
        "tag": {
          "en": "erosion"
        }
      },
      {
        "confidence": 14.6678800582886,
        "tag": {
          "en": "glacier"
        }
      },
      {
        "confidence": 14.482006072998,
        "tag": {
          "en": "winter"
        }
      },
      {
        "confidence": 14.3086681365967,
        "tag": {
          "en": "panorama"
        }
      },
      {
        "confidence": 14.1589803695679,
        "tag": {
          "en": "summer"
        }
      },
      {
        "confidence": 14.0245943069458,
        "tag": {
          "en": "water"
        }
      },
      {
        "confidence": 13.453519821167,
        "tag": {
          "en": "grass"
        }
      },
      {
        "confidence": 13.1261720657349,
        "tag": {
          "en": "hill"
        }
      },
      {
        "confidence": 13.011589050293,
        "tag": {
          "en": "high"
        }
      },
      {
        "confidence": 12.622181892395,
        "tag": {
          "en": "grand"
        }
      },
      {
        "confidence": 12.6174287796021,
        "tag": {
          "en": "hills"
        }
      },
      {
        "confidence": 12.5902862548828,
        "tag": {
          "en": "rocky"
        }
      },
      {
        "confidence": 12.0642681121826,
        "tag": {
          "en": "sunny"
        }
      },
      {
        "confidence": 11.7458524703979,
        "tag": {
          "en": "landmark"
        }
      },
      {
        "confidence": 11.4653568267822,
        "tag": {
          "en": "vacation"
        }
      },
      {
        "confidence": 11.321738243103,
        "tag": {
          "en": "alp"
        }
      },
      {
        "confidence": 10.7740707397461,
        "tag": {
          "en": "southwest"
        }
      },
      {
        "confidence": 10.5922183990479,
        "tag": {
          "en": "sand"
        }
      },
      {
        "confidence": 10.3427696228027,
        "tag": {
          "en": "cold"
        }
      },
      {
        "confidence": 9.98015022277832,
        "tag": {
          "en": "orange"
        }
      },
      {
        "confidence": 9.7638635635376,
        "tag": {
          "en": "sandstone"
        }
      },
      {
        "confidence": 9.75960826873779,
        "tag": {
          "en": "formation"
        }
      },
      {
        "confidence": 9.669753074646,
        "tag": {
          "en": "ice"
        }
      },
      {
        "confidence": 9.37593650817871,
        "tag": {
          "en": "natural"
        }
      },
      {
        "confidence": 9.03097343444824,
        "tag": {
          "en": "roof"
        }
      },
      {
        "confidence": 8.87552165985107,
        "tag": {
          "en": "peaks"
        }
      },
      {
        "confidence": 8.81966876983643,
        "tag": {
          "en": "alpine"
        }
      },
      {
        "confidence": 8.80224514007568,
        "tag": {
          "en": "mount"
        }
      },
      {
        "confidence": 8.73800754547119,
        "tag": {
          "en": "vista"
        }
      },
      {
        "confidence": 8.6391773223877,
        "tag": {
          "en": "day"
        }
      },
      {
        "confidence": 8.31719589233398,
        "tag": {
          "en": "top"
        }
      },
      {
        "confidence": 8.24748420715332,
        "tag": {
          "en": "peaceful"
        }
      },
      {
        "confidence": 8.17128562927246,
        "tag": {
          "en": "sun"
        }
      },
      {
        "confidence": 8.11302661895752,
        "tag": {
          "en": "horizon"
        }
      },
      {
        "confidence": 7.91500616073608,
        "tag": {
          "en": "land"
        }
      },
      {
        "confidence": 7.91032791137695,
        "tag": {
          "en": "country"
        }
      },
      {
        "confidence": 7.87008666992188,
        "tag": {
          "en": "geological"
        }
      },
      {
        "confidence": 7.86280584335327,
        "tag": {
          "en": "national park"
        }
      },
      {
        "confidence": 7.85683012008667,
        "tag": {
          "en": "spring"
        }
      },
      {
        "confidence": 7.84731531143188,
        "tag": {
          "en": "wild"
        }
      },
      {
        "confidence": 7.79706764221191,
        "tag": {
          "en": "scene"
        }
      },
      {
        "confidence": 7.7928295135498,
        "tag": {
          "en": "color"
        }
      },
      {
        "confidence": 7.72600078582764,
        "tag": {
          "en": "west"
        }
      },
      {
        "confidence": 7.72066307067871,
        "tag": {
          "en": "majestic"
        }
      },
      {
        "confidence": 7.59368371963501,
        "tag": {
          "en": "adventure"
        }
      },
      {
        "confidence": 7.58410120010376,
        "tag": {
          "en": "stones"
        }
      },
      {
        "confidence": 7.51064872741699,
        "tag": {
          "en": "cloudy"
        }
      },
      {
        "confidence": 7.48021507263184,
        "tag": {
          "en": "tourist"
        }
      },
      {
        "confidence": 7.34951877593994,
        "tag": {
          "en": "dome"
        }
      },
      {
        "confidence": 7.33834314346313,
        "tag": {
          "en": "ecology"
        }
      },
      {
        "confidence": 7.24884223937988,
        "tag": {
          "en": "tranquil"
        }
      },
      {
        "confidence": 7.12695741653442,
        "tag": {
          "en": "sunlight"
        }
      }
    ]
  },
  "status": {
    "text": "",
    "type": "success"
  }
}
@shared_task
def second_service_task(id):
    #get advertisment image from s3
    #send advertisment to second service
    #get response from second service
    #update advertisment state
    ## get advertisment image from s3
    url=create_image_url(id)
    response = requests.get(
    IMG_ENDPOINT+'/v2/tags?image_url=%s' % url,
            auth=(IMG_KEY, IMG_SECRET_KEY))
    data=response.json()
    # we use temp data for testing
    res=temp_data["result"]["tags"]
    max_confidence=0
    max_tag=""
    for i in res:
        text=i["tag"]["en"]
        confidence=i["confidence"]
        if(text == "car" or text == "vehicle" or text == "transportation" or text == "automobile" or text == "motor vehicle" or text == "motorcar" or text == "machine" or text == "motor" or text == "motorcycle" or text == "motorbike"):
            if(confidence>max_confidence):
                max_confidence=confidence
                max_tag=text
    if(max_confidence>0):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="accepted"
        advertisment.save()
    if(max_confidence==0):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="rejected"
        advertisment.save()
        
        

        ## send advertisment to second service

        
        