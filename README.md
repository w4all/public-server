docker run --name=wfawebserver --network=wfanet -p 9000:80 -v C:\Users\mihas\blinder\images:/storage/images -v C:\Users\mihas\blinder\web-service:/app -e IMAGE_PROCESSOR_PATH=http://imagerecognition/recognite_image  webserver