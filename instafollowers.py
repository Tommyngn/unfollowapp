from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process
import time
import csv


class unfollowbot:
    python_list=[]

    # def __init__(self):
    #     path = '/Users/tommynguyen/Desktop/chromedriver'
    #     chrome_option = Options()
    #     chrome_option.add_argument('--headless')
    #     chrome_option.add_argument('--window-size=1920x1080')
    #     chrome_option.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
    #
    #     drive = webdriver.Chrome(options=chrome_option, executable_path=path)
    #     drive.get('https://instagram.com')
    #     time.sleep(3)
    #     login=drive.find_element_by_name('username')
    #     login.send_keys('tommyngn')
    #     time.sleep(2)
    #     login=drive.find_element_by_name('password')
    #     login.send_keys('tIge8008')
    #     time.sleep(2)
    #     login.send_keys(Keys.ENTER)
    #
    #     time.sleep(6)
    #     page=drive.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
    #     page.click()
    #     time.sleep(6)
    #     drive.save_screenshot('test2.png')
    #     # page1=drive.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    #     # page1.click()
    #     # time.sleep(3)
    #
    #     # page2=drive.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    #     # page2.send_keys('ayalladiaz')
    #     # page2.send_keys(Keys.ENTER)
    #     # time.sleep(3)
    #     page2=drive.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
    #     page2.click()
    #     time.sleep(3)
    #     page2 = drive.find_elements_by_xpath('//a[contains(@href, "/tommyngn/")]')
    #     page2[2].click()
    #     time.sleep(3)
    #     page3 = drive.find_element_by_xpath('//a[contains(@href ,"/tommyngn/followers/")]')
    #     page3.click()
    #     time.sleep(2)
    #
    #     scroll_box = drive.find_element_by_xpath("//div[@class='isgrP']")
    #     last_ht, ht = 0, 1
    #     while last_ht != ht:
    #         last_ht = ht
    #         time.sleep(2)
    #         ht = drive.execute_script("""
    #                     arguments[0].scrollTo(0, arguments[0].scrollHeight);
    #                     return arguments[0].scrollHeight;
    #                     """, scroll_box)
    #     print('done')
    #     link=scroll_box.find_elements_by_tag_name('a')
    #     for i in link:
    #         if str(i.text) != '':
    #             print(i.text)
    #             self.python_list.append(str(i.text))

    def getfollowerlist(self,name):

        path='/Users/tommynguyen/Desktop/chromedriver'
        chrome_option=Options()
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('--window-size=1920x1080')
        chrome_option.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')

        drive=webdriver.Chrome(chrome_options=chrome_option, executable_path=path)
        drive.get('https://www.instagram.com')
        time.sleep(3)
        login=drive.find_element_by_name('username')
        login.send_keys('tommyngn')
        time.sleep(2)
        login=drive.find_element_by_name('password')
        login.send_keys('tIge8008')
        time.sleep(2)
        login.send_keys(Keys.ENTER)
        # time.sleep(500000)

        time.sleep(6)
        page=drive.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        page.click()
        time.sleep(6)
        # page1=drive.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        # page1.click()
        # time.sleep(3)

        page2=drive.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        page2.send_keys(str(name))
        time.sleep(3)
        page2=drive.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]')
        time.sleep(2)
        page2.click()

        time.sleep(3)
        page3 = drive.find_element_by_xpath('//a[contains(@href ,"/' + name + '/followers/")]')
        page3.click()
        time.sleep(2)

        scroll_box = drive.find_element_by_xpath("//div[@class='isgrP']")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = drive.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
        print('done')
        link=scroll_box.find_elements_by_tag_name('a')
        for i in link:
            if str(i.text) != '':
                print(i.text)
                self.python_list.append(str(i.text))

        return self.python_list

    def writetocsv(self):
        filename= 'following_list_updated_new.csv'

        file=open(filename, 'w')

        writer=csv.writer(file)
        writer.writerow(['Name'])
        for i in self.python_list:
            writer.writerow([str(i)])

    def writetocsv2(self,names):
        a=open('following_list_updated.csv','a')
        write=csv.writer(a)
        for name in names:
            write.writerow([str(name)])



# bot=unfollowbot()
# a=bot.python_list
#
# f=open('following_list_updated_new.csv','r')
# g=open('unfollow_final.csv','a')
# writer=csv.writer(g)
# rows=list(csv.reader(f))
#
# b=[]
# for i in rows:
#     b.append(i[0])
# for i in b:
#     if i not in a and i != 'Name':
#         writer.writerow([str(i)])
#



