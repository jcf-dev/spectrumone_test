# Setting up the Environment Variables
1. Copy and rename `.env.sample` file to `.env` using this command 
    ```
    cp .env.sample .env
    ```
2. Modify `.env` variable values to desired values. 
* **Note:** You can generate a fresh Django secret key by running these on a Python console:  
   ```python
   from django.core.management.utils import get_random_secret_key  
   get_random_secret_key()
   ```