# python 3
FROM python:latest

# set up working dir
WORKDIR /bot
COPY . /bot

# install pip packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# use port 80
EXPOSE 80

# run app
CMD ["python", "bot.py"]
