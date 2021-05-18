# qiot-sensor-service

## Exposed endpoints

Retrieving gas sensor data
```shell script
0.0.0.0:5000/api/sensors/gas
```

Retrieving particles sensor data
```shell script
0.0.0.0:5000/api/sensors/pollution
```

Retrieving raspberry pi serial
```shell script
0.0.0.0:5000/api/system/id
```

Swagger UI
```shell script
0.0.0.0:5000/swagger
```

## building the image 

Building aarch64 images, using buildx
```shell script
docker buildx build --platform linux/arm64 -t <a-docker-username>/qiot-sensor-service --push .
```