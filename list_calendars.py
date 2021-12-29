from pickle import TRUE
from cal_setup import get_calendar_service

def main():
    service = get_calendar_service()
    # Call the Calendar API
    print('Getting list of calendars')
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])

    
    noExist = True
    for calendar in calendars:
       summary = calendar['summary']


       if summary == 'Trend':
            noExist = False
            break

    if noExist:
        calendarT = {
            'summary': 'Trend',
            'timeZone': 'America/Los_Angeles'
        }

        service.calendars().insert(body=calendarT).execute()



if __name__ == '__main__':
   main()