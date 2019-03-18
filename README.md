# lottery_winners
## This code utilized *Python, BeautifulSoup, and Selenium* in order to provide information on previous lottery winners from March of 2018 to now. While this code was unsuccessful in accomplishing this, this page will try to narrate what went wrong.
### What I planned to scrape:
- Names of lottery winners (*found in an h2*)
- Heading of the article about the winner(*found in an h2*)
- Their location(*found in an h3*)
- How much they won (*found in an h3*)
- What game they had won (Powerball, MegaMillion, etc.) *(found in an  `<em></em>`. This is the only `<em>` tag on each page.)*
### Step 1: Getting the URLs
Since there were 18 pages total for me to collect from, and each time I clicked next it did not lead to a new URL but kept me at https://nylottery.ny.gov/winners-wall, I had to use Selenium in order to move to the next page. This was a struggle to figure out. 
To get Selenium:
1. I first pip installed it into my Git CMD.
2. I imported Selenium into my code using: 
    - `from selenium import webdriver`
3. I then wrote the following:
    - `for n in range(17): `
    
          driver.find_element_by_css_selector(".pagination .next").click();
           s = randint(1, 10)
           time.sleep(s)`
4. I then had an **issue** with error codes when I got Selenium, so I used the following code:
    - `from selenium.common.exceptions import NoSuchElementException`
    -
    -`options = webdriver.ChromeOptions()`
      
      `options.add_argument('--ignore-certificate-errors')`
      
      `options.add_argument('--ignore-ssl-errors')`
      
5. I added the drivers needed to get web pages and set `html = driver.page_source`
### Step 2: Get the Details from the pages
This is the part I left off at because I still failed to get the all info from my first link.
I did this with my `get_winner_details` function. However, I am aware that my issue is most likely with my new_url. I tried to find the h2 and h3 element and created a list called winner_list.

I used `headline=bsObj.find('h2')` to get the headline from each page. I believe my issue is that I was doing bsObj.find.
The same thing would go with my `name` variable.

### All the issues I've faced and fixed:
1.) Initially I had an issue where I was forbidden from the page, so I had to include a header. 

2.) Selenium had a lot of error issues, so I included the options to fix that issue.

3.) Also had an issue where Selenium just wouldn't scan the page. I had to find elements by CSS rather than anything else in order for it to work.

### Issues left:
1.) The only things that print are three items on the first page and three on the last page. I had an issue with the csv file only writing items from the last page, but somehow got three items from the first page. 

2.) I am struggling to figure out how to get the details for the page. I am aware where the issue is (with the new_url) but after multiple hours I could not resolve it.
