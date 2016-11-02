import requests
import bs4

# Sample Request
url = "https://google.com"
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
links = [a.attrs.get('href') for a in soup.select('a[href]')]
print(soup)
print(links)

# Sample Session Request 
cookies = {
    '_tt_ses_id': '928aa8d0c9531923397166b24d995646',
    'localeCookie': 'en_IN',
    'lpCurrency': 'USD',
    'lpUid': 'hIr6zx6SsCTnJfmlrO3s_TMPCg4KJx6-',
    'utag_main': 'v_id:0158247be7f100015401558fbc360904c006b0090086e$_sn:1$_ss:0$_pn:4%3Bexp-session$_st:1478083816265$ses_id:1478080849905%3Bexp-session',
    '_ga': 'GA1.2.1032553494.1478080852',
    's_cc': 'true',
    's_fid': '3232AA7F1EBCE591-3F753E3F2BDDA2FA',
    'gpv_v2': 'no%20value',
    'cam': 'direct',
    'cam_chan': 'direct',
    'chan_stk': 'direct',
    's_sq': 'lonelyplanet-global%3D%2526pid%253Dhttps%25253A%25252F%25252Fauth.lonelyplanet.com%25252Fusers%25252Fsign_in%2526oid%253DSign%252520in%2526oidt%253D3%2526ot%253DSUBMIT',
    '_ceg.s': 'og0eim',
    '_ceg.u': 'og0eim',
    's_vi': '[CS]v1|2C0CDCAB05015F79-600001476000EE7C[CE]',
    'lp_luna_session_id': '7c2a9101bcd88c22228e1f785dd9072d',
    'TrackJS': '12151286-a45c-4f4f-9773-3ed1810a9f14',
    '_gat_tealium_0': '1',
    '_gali': 'login_form',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'auth.lonelyplanet.com',
    'Referer': 'https://auth.lonelyplanet.com/users/sign_in',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0 FirePHP/0.7.4',
    'x-insight': 'activate',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'utf8': '',
  'authenticity_token': 'ZrVahPnSeilbo+MUj2gFGEXEZ0E0WrMOGrDT4MFitgE=',
  'user[login]': '******@gmail.com',
  'user[password]': '******',
  'user[remember_me]': '0'  
}
session = requests.session()

r1 = session.post('https://auth.lonelyplanet.com/users/sign_in', headers=headers, cookies=cookies, data=data)
r = session.get('https://auth.lonelyplanet.com/profiles/****15')
print(r1.text)

