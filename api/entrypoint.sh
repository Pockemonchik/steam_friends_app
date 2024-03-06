#!/bin/sh
#alembic init -t async migrations
# alembic revision -m "init" --autogenerate
echo "start fastapi app";
echo "migrate db";
alembic upgrade head;
echo "run...";
exec "$@"