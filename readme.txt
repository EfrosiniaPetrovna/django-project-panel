Простая мониторинг-панель проекта (размеры всех таблиц в базе данных, медиа файлов и т.д)

***
Установка:

1. добавить в
INSTALLED_APPS = [
	...
	'django_project_panel',
]

2. добавить в urls проекта
path('project_panel/', include('django_project_panel.urls')),

3. выполнить миграции django_project_panel
manage.py makemigrations django_project_panel
manage.py migrate django_project_panel

***
Настройка:

Добавить в settings.py

PROJECT_PANEL = {
	'folders_files': [
		{'path': os.path.join(BASE_DIR, 'logs'), 'label': 'Логи'},
		{'path': os.path.join(BASE_DIR, 'static'), 'label': 'Статика'},
		{'path': BASE_DIR, 'label': 'Проект'},
	],
	'clean_model': {
		'default.reports': {'filter_field_lt': 'created_at'},
	},
}

folders_files - можно перечислить каталоги и файлы, данные о которых нужно выводить в панели
каталог медиа уже добавлен

clean_model - можно перечислить таблицы, для которых будет доступа функция очистки в панели
'clean_model': {
	'<алиас базы>.<имя таблицы>': {'filter_field_lt': '<имя поля для фильтрации записей на удаление>'},
},

ВАЖНО!
Удаление записей происходит в соответствии с настройками on_delete вашей таблицы в базе

***
Права:
- Панель управления проектом - просмотр
- Панель управления проектом - управление

***
Подходит для mysql/mariadb и postgresql

***
url расширения: /project_panel/panel/