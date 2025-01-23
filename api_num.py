import requests,time
import pypinyin,schedule,time
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QSettings
import get_name
app = QApplication([])
settings = QSettings('MyCompany', 'MyApp')
content = settings.value('input_value')

text = content

def hanzi_to_pinyin(text):
    pinyin = pypinyin.lazy_pinyin(text)
    pinyin_str = ''.join(pinyin)
    return pinyin_str


def search_city_code(city_name):
    city_code_url = 'https://geoapi.qweather.com/v2/city/lookup?location=%s&key=926d17dc2fe943e2baaffbf732dfb584' % city_name
    city_code_content = requests.get(city_code_url).json()
    code = city_code_content['location'][0]['id']
    return code
try:
    code = search_city_code(hanzi_to_pinyin(text))
except:
    app = QApplication([])
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText("当前服务不可用")
    msg_box.setWindowTitle("警告")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
    app.quit()

def search_weather_suggest (code):
    city_weather_suggest_url = 'https://devapi.qweather.com/v7/indices/1d?type=1&location=%s&key=926d17dc2fe943e2baaffbf732dfb584' % code
    text_content = requests.get(city_weather_suggest_url).json()
    text = text_content['daily'][0]['text'].split('；')[0]
    return text


def search_air_quality(code):
    air_quality_url = 'https://devapi.qweather.com/v7/air/now?location=%s&key=926d17dc2fe943e2baaffbf732dfb584' % code
    quality_content = requests.get(air_quality_url).json()
    air_quality_text = quality_content['now']['category']
    return air_quality_text


def search_waring(code):
    waring_url = 'https://devapi.qweather.com/v7/warning/now?location=%s&lang=cn&key=926d17dc2fe943e2baaffbf732dfb584' % code
    waring_content = requests.get(waring_url).json()
    try:
        waring_text_title = waring_content['warning'][0]['title']
        #waring_text_text = waring_content['warning'][0]['text']
        return waring_text_title
    except:
        return "最近暂无灾害预警，较为安全！"


def search_now_date(code):
    date_url = 'https://devapi.qweather.com/v7/weather/now?location=%s&key=926d17dc2fe943e2baaffbf732dfb584' % code
    date_content = requests.get(date_url).json()
    date_temp = date_content['now']['temp']
    date_feelsLike = date_content['now']['feelsLike']
    date_windDir = date_content['now']['windDir']
    date_windScale = date_content['now']['windScale']
    date_humidity = date_content['now']['humidity']
    date_pressure = date_content['now']['pressure']
    date_dew = date_content['now']['dew']
    return date_temp,date_feelsLike,date_windDir,date_windScale,date_humidity,date_pressure,date_dew




def search_24h_date(code):
    twenty_four_hour_date_url = 'https://devapi.qweather.com/v7/weather/24h?location=%s&key=926d17dc2fe943e2baaffbf732dfb584'%code
    twenty_four_hour_date_content = requests.get(twenty_four_hour_date_url).json()
    twenty_four_hour_date_time = []
    twenty_four_hour_date_temp = []
    twenty_four_hour_date_text = []
    twenty_four_hour_date_windDir = []
    twenty_four_hour_date_windScale = []
    twenty_four_hour_date_humidity = []
    twenty_four_hour_date_pop = []
    twenty_four_hour_date_pressure = []
    twenty_four_hour_date_dew = []
    for i in range(24):
        a = twenty_four_hour_date_content['hourly'][i]['fxTime'].split('T')[1]
        twenty_four_hour_date_time.append(a.split(':')[0])
        twenty_four_hour_date_temp.append(int(twenty_four_hour_date_content['hourly'][i]['temp']))
        twenty_four_hour_date_text.append(twenty_four_hour_date_content['hourly'][i]['text'])
        twenty_four_hour_date_windDir.append(twenty_four_hour_date_content['hourly'][i]['windDir'])
        twenty_four_hour_date_windScale.append(twenty_four_hour_date_content['hourly'][i]['windScale'])
        twenty_four_hour_date_humidity.append(twenty_four_hour_date_content['hourly'][i]['humidity'])
        twenty_four_hour_date_pop.append(twenty_four_hour_date_content['hourly'][i]['pop'])
        twenty_four_hour_date_pressure.append(twenty_four_hour_date_content['hourly'][i]['pressure'])
        twenty_four_hour_date_dew.append(twenty_four_hour_date_content['hourly'][i]['dew'])
    return twenty_four_hour_date_time,twenty_four_hour_date_temp,twenty_four_hour_date_text,twenty_four_hour_date_windDir,twenty_four_hour_date_windScale,twenty_four_hour_date_humidity,twenty_four_hour_date_pop,twenty_four_hour_date_pressure,twenty_four_hour_date_dew



def search_7d_date(code):
    seven_day_date_url = 'https://devapi.qweather.com/v7/weather/7d?location=%s&key=926d17dc2fe943e2baaffbf732dfb584' % code
    seven_day_date_content = requests.get(seven_day_date_url).json()
    seven_day_date_fxDate = []
    seven_day_hour_date_tempMax = []
    seven_day_hour_date_tempMin = []
    seven_day_hour_date_textDay = []
    seven_day_hour_date_textNight = []
    seven_day_hour_date_windDirDay = []
    seven_day_hour_date_windScaleDay = []
    seven_day_hour_date_humidity = []
    seven_day_hour_date_pressure = []
    seven_day_hour_date_sunrise = []
    seven_day_hour_date_sunset = []
    seven_day_hour_date_moonrise = []
    seven_day_hour_date_moonset = []
    seven_day_hour_date_moonphase = []
    for i in range(7):
        seven_day_date_fxDate.append(seven_day_date_content['daily'][i]['fxDate'])
        seven_day_hour_date_tempMax.append(seven_day_date_content['daily'][i]['tempMax'])
        seven_day_hour_date_tempMin.append(seven_day_date_content['daily'][i]['tempMin'])
        seven_day_hour_date_textDay.append(seven_day_date_content['daily'][i]['textDay'])
        seven_day_hour_date_textNight.append(seven_day_date_content['daily'][i]['textNight'])
        seven_day_hour_date_windDirDay.append(seven_day_date_content['daily'][i]['windDirDay'])
        seven_day_hour_date_windScaleDay.append(seven_day_date_content['daily'][i]['windScaleDay'])
        seven_day_hour_date_humidity.append(seven_day_date_content['daily'][i]['humidity'])
        seven_day_hour_date_pressure.append(seven_day_date_content['daily'][i]['pressure'])
        seven_day_hour_date_sunrise.append(seven_day_date_content['daily'][i]['sunrise'])
        seven_day_hour_date_sunset.append(seven_day_date_content['daily'][i]['sunset'])
        seven_day_hour_date_moonrise.append(seven_day_date_content['daily'][i]['moonrise'])
        seven_day_hour_date_moonset.append(seven_day_date_content['daily'][i]['moonset'])
        seven_day_hour_date_moonphase.append(seven_day_date_content['daily'][i]['moonPhase'])
    return seven_day_date_fxDate, seven_day_hour_date_tempMax, seven_day_hour_date_tempMin,seven_day_hour_date_textDay,seven_day_hour_date_textNight, seven_day_hour_date_windDirDay, seven_day_hour_date_windScaleDay,seven_day_hour_date_humidity, seven_day_hour_date_pressure, seven_day_hour_date_sunrise, seven_day_hour_date_sunset,seven_day_hour_date_moonrise,seven_day_hour_date_moonset, seven_day_hour_date_moonphase


if __name__ == "__main__":
    # 每小时的整点触发更新
    schedule.every().hour.at(":00").do(search_city_code)
    while True:
        schedule.run_pending()
        time.sleep(1)


