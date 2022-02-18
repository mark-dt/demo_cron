This is a Dynatrace ActiveGate Extension that will run on a cronjob basis using cron strings, e.g. following string `*/5 * * * *` it will run every 5min
```
azureuser@test ..eplugin/custom.remote.python.demo_cron
% tail DemoCron.log
2022-02-18 10:44:01.147 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Now: 02/18/2022, 10:44
2022-02-18 10:44:01.147 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Next: 02/18/2022, 10:45
2022-02-18 10:44:01.147 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Waiting...
2022-02-18 10:45:01.205 UTC INFO    [Python][6785419390646166290][test][140158196246272][ThreadPoolExecutor-0_0] - [query] Now: 02/18/2022, 10:45
2022-02-18 10:45:01.206 UTC INFO    [Python][6785419390646166290][test][140158196246272][ThreadPoolExecutor-0_0] - [query] Next: 02/18/2022, 10:45
2022-02-18 10:45:01.206 UTC INFO    [Python][6785419390646166290][test][140158196246272][ThreadPoolExecutor-0_0] - [query] Do stuff
2022-02-18 10:46:01.260 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Now: 02/18/2022, 10:46
2022-02-18 10:46:01.260 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Next: 02/18/2022, 10:50
2022-02-18 10:46:01.260 UTC INFO    [Python][6785419390646166290][test][140157918586624][ThreadPoolExecutor-0_1] - [query] Waiting...
```