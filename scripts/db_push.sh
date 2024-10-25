#!/bin/bash
# Exit on error
set -e

# Configuration
SERVER="logres.gartmeier.dev"
DEPLOY_PATH="/var/www/gartmeier.dev"

scp db.sqlite3 logres.gartmeier.dev:$DEPLOY_PATHP