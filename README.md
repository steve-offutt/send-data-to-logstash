# Demo of how to send data to logstash using python
Using docker run a logstash-oss container.
```
docker run --rm -v ~/code/send-events-to-logstash/pipeline:/usr/share/logstash/pipeline -it --name logstash -p 12345:12345 docker.elastic.co/logstash/logstash-oss:7.17.0
```
Then send data using the `send-data.py` script.
```
python send-data.py
```

There will be many warning about `ecs_compatability`. I have not figured out a way to turn this off.