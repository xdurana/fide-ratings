#! /usr/bin/env sh

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

echo "
#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
"

mkdir data
wget -qO- -O tmp.zip http://ratings.fide.com/download/players_list.zip && unzip tmp.zip && rm tmp.zip && mv *.txt data/
