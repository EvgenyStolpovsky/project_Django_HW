## 21.1 fbv и cbv

# Задание 1. Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

# Задание 2. Создайте новую модель блоговой записи со следующими полями:

- заголовок,
- slug (реализовать через CharField),
- содержимое,
- превью (изображение),
- дата создания,
- признак публикации,
- количество просмотров.
- Для работы с блогом реализуйте CRUD для новой модели.

# Задание 3. Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.


## 20.2 Шаблонизация

# Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение карточки товара. На странице важно выводить
всю информацию о товаре.

Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу данный шаблон.

# Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек
отображаемое описание обрежьте после первых выведенных 100 символов.

# Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый)
шаблон и также подшаблон с главным меню.

При необходимости можно выделить больше общих шаблонов.

# Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь
для доступа к медиафайлу.

_________________________________________________________________________________________________________________
# Задание 1

Подключите СУБД PostgreSQL для работы в проекте. Для этого:

- Создайте базу данных в ручном режиме.
- Внесите изменения в настройки подключения.

# Задание 2

В приложении каталога создайте модели:

- Product,
- Category.

# Задание 3

Для каждой модели опишите следующие поля:

- Product:
  наименование, описание, отображение, категория, цена за покупку, дата создания, дата последнего изменения
- Category:

наименование,
описание.
Для поля с изображением необходимо добавить соответствующие настройки в проект, а также установить библиотеку для работы
с изображениями
Pillow
.

# Задание 4

Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:

- Создайте миграции для новых моделей.
- Примените миграции.
- Внесите изменения в модель категорий, добавьте поле
  created_at
- примените обновление структуры с помощью миграций.
- откатите миграцию до состояния, когда поле
  created_at
- для модели категории еще не существовало, и удалите лишнюю миграцию.

# Задание 5

Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и
наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а
также осуществлять поиск по названию и полю описания.

# Задание 6

Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные
рассмотренные фильтры. В качестве решения приложите скриншот.

- сформируйте фикстуры для заполнения базы данных.
- напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от
  старых данных.

# Урок 19.2 Знакомство с Django. Домашнее задание

### Задание 1

Для начала работы над задачей необходимо выполнить первые шаги:

- Настройте виртуальное окружение
- Создай новый Django проект

### Задание 2

После успешного создания проекта, необходимо сделать первую настройку, для этого:

- Создайте первое приложение с названием `catalog`
- Внесите начальные настройки проекта
- Сделайте настройку url’ов для нового приложения

### Задание 3

Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

<aside>
ℹ️ **Примечание**
Для создания шаблонов лучше использовать uikit Bootstrap, при возникновении проблем, можно брать за основу 
данный шаблон (https://github.com/oscarbotru/skystore-templates)

</aside>

### Задание 4

В приложении в контроллере реализуйте два контроллера:

- Контроллер, который отвечает за отображение домашней страницы
- Контроллер, который отвечает за отображение контактной информации
