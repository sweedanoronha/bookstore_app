FROM node:16

WORKDIR /app

COPY ./package.json ./yarn.lock /app/
RUN yarn install

COPY ./src /app/src
COPY ./public /app/public

RUN yarn build

CMD ["yarn", "start"]
