# Tv Channel Schedule Api
      API for Indian Tv channel schedule.

## List of api services:-
      /getCategories:-  
                  Json response of languages list and channel categories list.
      /searchChannel:- 
                  args:- lang(optional),cate(optional)
                  Json response of sorted Channels on bases of language and categories.
      /TodaySchedule:-
                  args:- channel
                  Json response for todays schedule of respective Channel.
      /Schedule:-
                  args:- channel,offset(optional)
                  offset values as -1 for yesterday,0 for today,1 for tomorrow
                  Json response for channel schedule on offset day
      /GetTodaysMovies:-
                  args- lang,offset(optional)
                  offset values as -1 for yesterday,0 for today,1 for tomorrow
                  Text for particular day movies in a language

## List of Test urls:-
Click here :- https://rapidapi.com/Garuda07/api/indian-tv-schedule
      

## You can fork the repo and deploy on VPS or deploy it on Heroku :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/datta07/tv-channel-schedule-api/tree/master)
