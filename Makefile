.PHONY: all update run

all: update run

update: update.dummy
update.dummy: bot.py apikey.yml Dockerfile
	sudo docker build --tag=saberbot .
	touch $@

run: update
	sudo docker run -p 4000:80 saberbot
