from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():
    # mark the entire day as a special event
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])
    calID = ''

    for calendar in calendars:
        if calendar[ 'summary' ] == 'Trend' :
            calID = calendar[ 'id' ]
            break


    service.events().insert(calendarId='calID',
       body={
           "summary": 'Automating calendar',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
    ).execute()

if __name__ == '__main__':
   main()