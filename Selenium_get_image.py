from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl
from time import sleep
import os


ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://ja.wikipedia.org/wiki/Category:アメリカ合衆国の男優'

def get_hp(url):
    res = requests.get(url)
    res.raise_for_status() # エラーならここで例外を発生させる
    return res.text

# keyword_list = []
# soup = BeautifulSoup(get_hp(url), 'lxml')
# names = soup.findAll('li')
# for name in names:
#     if '・' in name.text and '(' not in name.text:
#         keyword_list.append(name.text)
#     if len(keyword_list) == 100:
#         break
#
# print(keyword_list)

# keyword_list = ['哀川翔', '相葉雅紀', '明石家さんま', '赤西仁', '安住紳一郎',
#                 '阿部寛', '綾部祐二', '新田真剣佑', '浅野忠信', '愛川欽也',
#                 '石橋貴明', '五木ひろし', '市村正親', '今井翼', '岩尾望',
#                 '上田晋也', '内村光良', 'えなりかずき', '大泉洋', '及川光博',
#                 '大竹まこと', '大沢たかお', '岡田将生', '織田裕二', '香川照之',
#                 '川崎麻世', 'カンニング竹山', '上川隆也', '片岡愛之助', '春日俊彰',
#                 '北野武', '桐谷健太', '吉川晃司', '北島三郎', '草彅剛',
#                 '宮藤官九郎', '劇団ひとり', '小池徹平', '河本準一', '小日向文世',
#                 '小山慶一郎', '近藤真彦', '西城秀樹', '坂口健太郎', '堺正章',
#                 '坂上忍', '佐藤二朗', '沢田研二', '柴田恭兵', '城田優']
#
# keyword_list = ['須賀健太', '杉浦太陽', '鈴木浩介', '菅田将暉', '関口宏',
#                 '染谷将太', 'DAIGO', '高倉健', '高橋克実', '滝沢秀明',
#                 '田口淳之介', '竹内力', '武田鉄矢', '竹中直人', '伊達みきお',
#                 '田中義剛', '玉木宏', '玉置浩二', '田村亮', '千原ジュニア',
#                 '千原せいじ', '堤真一', '妻夫木聡', 'つるの剛士', '出川哲朗',
#                 '堂本光一', '豊川悦司', '中井貴一', '中田敦彦', '長瀬智也',
#                 '仲村トオル', '名倉潤', '成宮寛貴', '西川貴教', '西田敏行',
#                 '二宮和也', '温水洋一', '野口五郎', '博多大吉', '波田陽区',
#                 'はなわ', 'パパイヤ鈴木', '濱田岳', '板東英二', '東野幸治',
#                 '彦摩呂', '日村勇紀', '平野紫耀', '福山雅治', '古田新太']
# keyword_list = ['クリント・イーストウッド', 'ブルース・ウィリス', 'リチャード・ギア', 'メル・ギブソン',
#                 'ジム・キャリー', 'ヒュー・グラント', 'トム・クルーズ', 'ジョージ・クルーニー',
#                 'ラッセル・クロウ', 'ニコラス・ケイジ', 'ケビン・コスナー', 'ライアン・ゴズリング',
#                 'キーファー・サザーランド', 'チャーリー・シーン', 'ヒュー・ジャックマン', 'ロバート・ダウニー・Jr',
#                 'レオナルド・ディカプリオ','マット・デイモン','ボブ・ディラン','ジョニー・デップ',
#                 'ロバート・デ・ニーロ','ジャック・ニコルソン','アル・パチーノ','トム・ハンクス',
#                 'ブラッド・ピット','ジェイミー・フォックス','モーガン・フリーマン','アレック・ボールドウィン',
#                 'エディ・マーフィ','ユアン・マクレガー','ヒース・レジャー','ミッキー・ローク',
#                 'ビルゲイツ','ザッカーバーグ','ジム・ロジャース','ピーター・ティール',
#                 'マイケル・ジャクソン','ファレル・ウィリアムス','エミネム','タイガー・ウッズ',
#                 'ルイス・ハミルトン','アダム・サンドラー','ジョーダン・スピース','フィル・ミケルソン',
#                 'キャム・ニュートン','ジャスティンビーバー','ヴィン・ディーゼル','ノバク・ジョコビッチ',
#                 'ケビン・デュラント','ドウェイン・ジョンソン','ガース・ブルックス','ロジャー・フェデラー',
#                 'マーク・ウォールバーグ','ポール・マッカートニー','ハワード・スターン','リオネル・メッシ',
#                 'ケヴィン・ハート','フィル・マグロー','クリスティアーノ・ロナウド','ジェイムズ・パタースン',
#                 'バラク・オバマ','ドナルド・トランプ','ジョージ・ブッシュ','ロナルド・レーガン',
#                 'ウィル・スミス','キアヌ・リーブス','クリス・エヴァンス','ジェイソン・ステイサム',
#                 'ブラッドリー・クーパー','ハリソン・フォード','ジュード・ロウ','トム・ホランド',
#                 'デンゼル・ワシントン','ポール・ウォーカー','ブルーノ・マーズ', 'ドレイク',
#                 'ジャスティン・ティンバーレイク','フロー・ライダー','ニーヨ','ジェームス・ブラウン']

# keyword_list = ['マット・ルブランク', 'デヴィッド・シュワイマー', 'マシュー・ペリー', 'ブライアン・クランストン',
#                 'アーロン・ポール', 'ボブ・オデンカーク', 'ジョナサン・バンクス', 'ジャンカルロ・エスポジート',
#                 'コンリース・ヒル', 'ハリー・ロイド', 'ショーン・ビーン', 'ジェイソン・モモア',
#                 'ジョン・ブラッドリー', 'ロリー・マッキャン', 'ニコライ・コスター＝ワルドー', 'アルフィー・アレン',
#                 'イアン・グレン', 'キット・ハリントン', 'スティーヴン・ディレイン', 'ピーター・ディンクレイジ']
#
# keyword_list = ['石原良純', '市原隼人', '岩本勉', '上島竜兵', '内山信二',
#                 '遠藤憲一', 'オダギリジョー', '賀来賢人', 'ガッツ石松', '加藤茶']

keyword_list = ['ガブリエル・マクト', 'パトリック・J・アダムス', 'リック・ホフマン', 'エリック・クローズ',
                'ジョン・ファヴロー', 'デニス・ヘイスバート', 'D・B・ウッドサイド', 'グレン・モーシャワー',
                'アラン・デイル', 'キャメロン・ダッド']

url = 'https://search.yahoo.co.jp/image'


driver = webdriver.Chrome("/Users/k.masuda/Desktop/programs/chromedriver-2")


# キーワードをYahoo画像検索で検索
def search_keyword(keyword):
    # Yahoo検索を開く
    driver.get(url)

    # 検索窓にキーワードを入れる。
    search_box = driver.find_element_by_css_selector("#yschsp")
    search_box.send_keys(keyword)

    # 検索ボタンをクリックする
    search_button = driver.find_element_by_css_selector('#sbn > fieldset > div.sbox_1.cf > input').click()

    # ドロップダウンリストから'顔'を選択
    drop_down_list = driver.find_element_by_css_selector('#slidtoggle3 > a:nth-child(2)').get_attribute('href')
    print(drop_down_list)
    driver.get(drop_down_list)


# imageのURLを取得して、url_listに格納する。
def get_image_urls():
    li = []
    # scroll_and_morebutton()
    soup = BeautifulSoup(driver.page_source, "html5lib")
    photos = soup.find_all('p', attrs={'class', 'tb'})
    for photo in photos:
        img_url = photo.find('img').get('src')
        li.append(img_url)
    return li

#
# # 画面下までスクロールしてもっと見るボタンを押す
# def scroll_and_morebutton():
#     for i in range(2):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(1)
#     more = driver.find_element_by_css_selector('#autopagerMore > a').click()
#     for i in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(1)
#     more = driver.find_element_by_css_selector('#autopagerMore > a').click()
#     for i in range(8):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(1)
#
#
# PC内にキーワードを名前としたフォルダを作成し、そこに画像を保存する。
def save_photos(count):
    count = count
    url_list = get_image_urls()
    os.chdir("/Users/k.masuda/Desktop/images/American_man_for_test")
    for i in range(10):
        img_url = url_list[i]
        img = urllib.request.urlopen(img_url).read()
        with open('img{}.jpg'.format(count), 'wb') as file:
            file.write(img)
        count += 1

count = 0

for keyword in keyword_list:
    search_keyword(keyword)
    save_photos(count)
    count += 10
    sleep(5)


driver.close()
driver.quit()