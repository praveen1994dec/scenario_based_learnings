#!/bin/sh
# Health check logic
if ! curl -s http://my-app:80/health | grep "OK"; then
  echo "Deployment verification failed. Triggering rollback."
  helm rollback my-app
  exit 1
fi
echo "Deployment verification successful."
