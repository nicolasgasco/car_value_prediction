FROM node:20.12.0

COPY ./docker/node/run.sh ./

COPY ./data/predictions ./interface/data

CMD ["sh", "run.sh"]