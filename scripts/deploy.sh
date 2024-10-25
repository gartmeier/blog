#!/bin/bash
# Exit on error
set -e

# Configuration
SERVER="logres.gartmeier.dev"
DEPLOY_PATH="/var/www/gartmeier.dev"
VENV_PATH="$DEPLOY_PATH/venv"
SYSTEMD_SERVICE="gunicorn_gartmeier_dev.service"

echo "Deploying to $SERVER..."

# Connect to server and execute deployment steps
ssh $SERVER bash -c "'
    cd $DEPLOY_PATH

    echo \"Activating virtual environment...\"
    source $VENV_PATH/bin/activate

    echo \"Pulling latest changes...\"
    git pull

    echo \"Installing dependencies...\"
    poetry install

    echo \"Running migrations...\"
    python manage.py migrate

    echo \"Collecting static files...\"
    python manage.py collectstatic --noinput

    echo \"Restarting Gunicorn...\"
    sudo systemctl restart $SYSTEMD_SERVICE

    echo \"Checking service status...\"
    sudo systemctl status $SYSTEMD_SERVICE --no-pager
'"

echo "Deployment completed successfully!"