# social_website
Django training project

create new virtual environment by command
 uv init 
Add required dependencies by means of
uv add <django or other package>
To create new project run activate virtual environment
uv run django-admin startproject config .
project will be created in root of your project
add docker's yaml file and configure ports and name of db and maybe other parmeters
rename .env.template to .env
generate new secret key by command 
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
fill in .env
Create new database by command
docker-compose up -d
Docker desktop must be run at that moment