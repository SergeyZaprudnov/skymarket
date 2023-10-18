# Graduation project

# Bulletin board (SB1).   Direction - Backend

This course work is a backend part for an advertisement site.
The frontend part is already ready.

The backend part of the project involves the implementation of the following functionality:

   - Authorization and authentication of users.
   - Distribution of roles between users (user and admin).
   - Password recovery via email (optional).
   - CRUD for advertisements on the site (the admin can delete or edit all advertisements, and users only their own).
   - Users can leave reviews under each ad.
   - In the header of the site you can search for advertisements by name.

Brief technical specifications and recommendations for the order of execution:

   - Stage I. Setting up a Django project.
   - Stage II. Creating a user model. Setting up authorization and authentication.
   - Stage III. Description of ad and review models.
   - Stage IV. Creating views and endpoints.
   - Stage V. Defining permissions for views.

# To work with the project you need:

1. Install database software: PostgreSQL was used in this work
2. Install dependencies with the command pip3 install -r requirements.txt.
3. Create a .env file, enter your data into it, the example is in the .env.example file (we do not change the variables)
4. If the database has not been created in advance, then create a database in PostgreSQL
5. Go to the skymarket directory in the project, migrate data to the database with the command: python3 manage.py migrate
6. Start the server with the command: python3 manage.py runserver


## - - - RU - - - 

# Дипломная работа

# Доска объявлений (SB1). Направление - Бэкэнд*  
*(В данном проекте велась разработка только Бэкэнд части, Фронтенд не используется)

Данная курсовая работа является серверной частью рекламного сайта.
Фронтенд-часть уже готова.

Бэкэнд-часть проекта предполагает реализацию следующего функционала:

    - Авторизация и аутентификация пользователей.
    - Распределение ролей между пользователями (пользователь и администратор).
    - Восстановление пароля по электронной почте (опционально).
    - CRUD для рекламы на сайте (админ может удалять или редактировать все рекламные объявления, а пользователи только свои).
    - Пользователи могут оставлять отзывы под каждым объявлением.
    - В шапке сайта можно искать объявления по названию.

Краткие технические характеристики и рекомендации по порядку выполнения:

    - I этап. Настройка проекта Django.
    - II этап. Создание модели пользователя. Настройка авторизации и аутентификации.
    - III этап. Описание моделей рекламы и отзывов.
    - IV этап. Создание представлений и конечных точек.
    - V этап. Определение разрешений на просмотры.

# Для работы с проектом необходимо:

1. Установите программное обеспечение базы данных: в этой работе использовался PostgreSQL.
2. Установите зависимости с помощью команды pip3 install -r requirements.txt.
3. Создаём файл .env, вписываем в него свои данные, пример в файле .env.example (переменные не меняем)
4. Если база данных не была создана заранее, то создайте базу данных в PostgreSQL
5. Перейдите в каталог skymarket в проекте, перенесите данные в базу данных командой: python3 manage.py migrate.
6. Запустите сервер командой: python3 manage.py runserver.
