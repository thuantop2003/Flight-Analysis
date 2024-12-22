#!/usr/bin/env python3

from kafka import KafkaProducer
import json, csv, time
# tạo producer để gửi dữ liệu
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
# đọc file và gửi dữ liệu cho kafka mỗi 10s.
with open('../dataset/2019.csv') as file:
    reader = csv.DictReader(file, delimiter=",")
    index = 0
    for row in reader:
        print("sending data...")
        print(row)
        producer.send(topic='live-data', value=row)
        producer.flush()
        index += 1
        if (index % 20) == 0:
            time.sleep(10)
