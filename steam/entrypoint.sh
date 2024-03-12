#!/bin/sh
#alembic init -t async migrations
# alembic revision -m "initial"
echo "start steam service";
exec "$@"