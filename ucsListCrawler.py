import json
import requests

from bs4 import BeautifulSoup

ucsUrl = 'http://www.piugame.com/bbs/board.php?bo_table=ucs&page='

ucsList = []

with open('UCSSongData.json', encoding='utf-8') as f:
    songDatas = json.load(f)


def getTotalPage():
    total_steps_parsed = requests.get(ucsUrl)
    total_steps_soup = BeautifulSoup(total_steps_parsed.text, "html.parser")

    total_steps = total_steps_soup.find(class_="share_board_info_text")
    total_steps = total_steps.find("span").text.strip()
    total_steps = total_steps.replace("Total ", "").replace(",", "").replace(' cases', "")
    total_steps = int(total_steps)

    if total_steps % 15 == 0:
        total_page = total_steps // 15
    else:
        total_page = total_steps // 15 + 1
    return total_page


def getUcsList(page):
    res = requests.get(ucsUrl + str(page))
    res_soup = BeautifulSoup(res.text, "html.parser")

    ucs_list = res_soup.find("tbody")
    ucs_list = ucs_list.find_all('tr')

    for ucs_data in ucs_list:
        song_no = ucs_data.find(class_="share_song").find_all("img")[-1]['src'].replace("/piu.songimg/", "").replace(".png", "")
        for songData in songDatas:
            if song_no == songData['songNo']:
                song_title_ko = songData['songTitle_ko']
                song_title_en = songData['songTitle_en']

        ucs_no = ucs_data.find(class_="btnaddslot_ucs btnAddtoUCSSLOT")['data-ucs_id'].strip()
        ucs_lv = ucs_data.find(class_="share_level").find("span")['class']
        if "single" in ucs_lv[0]:
            ucs_lv = "S" + ucs_lv[1][4:]
        elif "sinper" in ucs_lv[0]:
            ucs_lv = "SP" + ucs_lv[1][4:]
        elif "double" in ucs_lv[0]:
            ucs_lv = "D" + ucs_lv[1][4:]
        elif "douper" in ucs_lv[0]:
            ucs_lv = "DP" + ucs_lv[1][4:]
        else:
            ucs_lv = "CO-OPx" + ucs_lv[1][5:]
        step_maker = ucs_data.find(class_="share_stepmaker").text.strip()

        try:
            ucsList.append((int(ucs_no), song_title_ko, song_title_en, ucs_lv, step_maker))
        except:
            pass


def runCrawler(mode):
    if mode == 'u':
        page = 2
    elif mode == 'r':
        page = getTotalPage()

    for i in range(900, page):
        getUcsList(i)
    return ucsList
