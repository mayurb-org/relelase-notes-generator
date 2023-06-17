FROM node:18-alpine
  
# System Package Updates
RUN apk update \
    && apk upgrade 

# Create app directory
WORKDIR /usr/src/app

# Copy app source
COPY . .

EXPOSE 3000
CMD [ "npm", "start" ]
