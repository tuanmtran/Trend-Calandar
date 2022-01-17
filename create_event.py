from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main( color):
    # mark the entire day as a special event
    service = get_calendar_service()

    d = datetime.now().date()
    tmr = d +timedelta(days=1)
    start = d.isoformat()
    end = datetime(tmr.year, tmr.month, tmr.day).date().isoformat()

    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])
    calID = ''

    for calendar in calendars:
        if calendar[ 'summary' ] == 'Trend' :
            calID = calendar[ 'id' ]
            break

    print (start)
    print(end)
    event = {
            'summary': '',
            'start': {
                'date': start,
                'timeZone': 'America/Los_Angeles'
            },
            'end': {
                'date': end,
                'timeZone': 'America/Los_Angeles'
            },
            'colorId': color,
        }
    service.events().insert(calendarId=calID, body=event).execute()

if __name__ == '__main__':
   main()