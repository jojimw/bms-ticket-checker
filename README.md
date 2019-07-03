# bms-ticket-checker
Checks the bookmyshow website whether the ticket booking has started for a movie in particular theatres of your choice
# bms.py
* Check ticket availability and sends email when tickets are available
* Makes a log whenever the script is executed
### Crontab command to run the python script every 15 minutes
```
*/15 * * * * $(which python) /path/to/file/bms.py >> ~/path/to/file/bms-cron.log
```
# bms-clear-log.py
* Clear logs and send the log data to your email
### Crontab command to run the python script every 2 hours at exactly n:01 Local Time (n = even number)
```
1 */2 * * * $(which python) /path/to/file/bms-clear-log.py
```
