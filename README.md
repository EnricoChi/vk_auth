# web app auth with vk OAUTH2

# demo
https://vk-auth.herokuapp.com/

# install
Clone repository

Install requirements in your virtualenv

    pip install -r requirements.txt

Create vk app in https://vk.com/editapp?act=create

Use secrecy for add vk app keys

    python manage.py secrecy --add
    
 Keys:
 
     VK_OAUTH2_ID
     VK_OAUTH2_SECRET
     VK_OAUTH2_TOKEN

 Run migration:

     python manage.py migrate
     
 Runserver:
 
     python manage.py runserver
