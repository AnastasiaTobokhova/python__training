import os
from datetime import datetime, timezone

# Путь к директории, где находятся файлы
repo_path = "."

# Получаем список всех файлов в директории
files = [(f, os.path.getmtime(f)) for f in os.listdir(repo_path) if os.path.isfile(f)]

# Сортируем файлы по дате изменения (новейшие сверху)
sorted_files = sorted(files, key=lambda x: x[1], reverse=True)

# Преобразуем UNIX timestamp в читаемое время с учетом timezone-aware объектов
formatted_files = [
    f"{file}: Last modified at {datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}"
    for file, mtime in sorted_files
]

# Обновляем README.md
with open("README.md", "w") as readme_file:
    readme_file.write("## Сортировка файлов по дате изменения\n\n")
    for idx, file_info in enumerate(formatted_files, 1):
        readme_file.write(f"{idx}. {file_info}\n")

# Выводим отсортированный список в терминал для проверки
for file_info in formatted_files:
    print(file_info)
