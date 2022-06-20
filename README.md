# Setting up the Environment Variables and PostGres DB via Docker

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
3. With **Docker Engine** installed and running, run the command below from the project root's terminal and your **Postgres Server** is good to go
    ```
    docker compose up -d --build
    ```
      * **Notes:**
        * To shut down the Postgres Server **without removing the data**, run 
        ```
        docker compose down
        ```
        * To shut down the Postgres Server **and removing the data**, run 
        ```
        docker compose down -v
        ```