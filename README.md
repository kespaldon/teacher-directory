# teacher-directory

## Installation:

1. Clone the repository

2. Enter the directory

  ```shell
  cd teacher-directory
  ```

3. Install pip virtual environment and dependencies
  
  ```python
  pipenv install
  
  # initialize virtual environment
  pipenv shell
  
  # once inside,
  pip install -r requirements.txt
  ```
  
4. Migrate
  ```python
  python manage.py migrate
  ```
  
5. Run server
  ```python
  python manage.py runserver
  ```
