# whreceiver
RAW Webhook Receiver for develop use

This is particularly useful in develop/setup your applications and scripts.

INSTALLATION

1. Clone repository git clone `https://github.com/ReuschelCGN/whreceiver`
2. Copy content of docker-compose.yml.example into your running docker-compose.yml
3. Change networks key `default` to your existing dockernetwork name
3. Adjust config `config.ini` if needet.
4. `docker-compose build whreceiver`
5. `docker-compose up -d whreceiver`

6. Output file in folder: `./output/`

get logs of service:
`docker-compose logs -f -t whreceiver`

CONFIGURATION

in `config.ini`:

[socketserver] => leave as it is

change filename for output if desired

[output] filename = `webhook_log.json`

point your Webhook (e.g. from rdm) to see what infos are send to:

`http://whreceiver:4444/webhook`
