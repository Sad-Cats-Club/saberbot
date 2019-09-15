# python 3
FROM python:latest

# set up working dir
WORKDIR /bot

# install pip packages
COPY requirements.txt /bot
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# copy rest of dir
COPY . /bot

# use port 80
EXPOSE 80

# run app
CMD ["python", "bot.py"]
