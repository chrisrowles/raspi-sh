# A web-based SSH client.

## Install

```sh
pip install -r requirements.txt
```

## Run

```sh
python manage.py
```

### Supervisord

Manage the process via [supervisord](http://supervisord.org/)

1. Install supervisord
  ```sh
  pip install supervisord
  ```
  
2. Copy `production/supervisord.conf` to your home directory
  ```sh
  cp production/supervisord.conf ~
  ```
  
3. Symlink `production/raspish.supervisor` to your home directory
  ```sh
  ln -s production/raspish.supervisor ~
  ```

4. Run supervisord
  ```
  supervisord
  ```
  
5. Check supervisord status
  ```
  supervisorctl status
  ```
  
6. Don't forget to update if you make changes to supervisord config files
  ```
  supervisorctl update
  ```





