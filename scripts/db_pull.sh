#!/bin/bash
# Exit on error
set -e

# Configuration
SERVER="logres.gartmeier.dev"
DEPLOY_PATH="/var/www/gartmeier.dev"

scp logres.gartmeier.dev:$DEPLOY_PATH/db.sqlite3 .