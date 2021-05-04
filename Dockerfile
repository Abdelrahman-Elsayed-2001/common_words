FROM ubuntu:21.04
RUN apt-get update
RUN apt-get install -y python3
COPY . /
CMD ["common_words.py"]
ENTRYPOINT ["python3"]