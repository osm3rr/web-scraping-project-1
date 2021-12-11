from bs4 import BeautifulSoup
import requests
import time

print( 'Put some skllis that you are not familiar with' )
unfamiliar_skills = input('> ')
print( f'Filtered by: {unfamiliar_skills}\n' )

def find_jobs ():
    """ Function to scrap python jobs in timesjobs"""
    
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
    
    html_text =   requests.get( url ).text
    
    soup = BeautifulSoup( html_text, 'lxml' )

    jobs = soup.find_all( 'li', class_ = 'clearfix job-bx wht-shd-bx' )

    for index, job in enumerate(jobs):
        condition = job.find( 'span', class_ = 'sim-posted' ).span.text

        if 'few' in condition:

            company_name = job.find( 'h3', class_ = 'joblist-comp-name' ).text
            skills = job.find( 'span', class_ = 'srp-skills' ).text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                with open( f'posts/{index}.txt', 'w' ) as file_out:
                    file_out.write(f'Company name: {company_name.strip()}\n')
                    file_out.write(f'skills : {skills.strip()}\n')
                    file_out.write( f'More info: {more_info}')
                
                print(f'Filed saved: {index} ')

# Routine for wait 5 minutes
# the name of the file it'll be "main"
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)