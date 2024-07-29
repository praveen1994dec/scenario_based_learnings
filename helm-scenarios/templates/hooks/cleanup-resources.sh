#!/bin/sh
# Cleanup logic
kubectl delete crd old-custom-resource
kubectl delete my-custom-resource --all
echo "Custom resources cleaned up."
