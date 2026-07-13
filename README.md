# Loop Engineering Test Sandbox

Чистый тестовый полигон для процесса разработки с независимой проверкой:

```text
GitHub Issue → отдельная ветка → Maker → Checker → Draft Pull Request → человек → Merge
```

Репозиторий реконструирован из идеи `test_codex_22`, но не переносит его историю,
`.env`, базу данных или опубликованные секреты.

## Что входит в полигон

- минимальное FastAPI-приложение;
- smoke-тесты главной страницы и `/health`;
- единая детерминированная команда проверки;
- проверка отслеживаемых файлов на секреты, `.env` и локальные базы;
- GitHub Actions для каждого Pull Request;
- роли Orchestrator, Maker и Checker;
- шаблоны Issue и Pull Request.

## Локальный запуск

Требуется Python 3.11 или новее.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Откройте <http://127.0.0.1:8000>.

## Единая проверка

Основная команда для всех платформ:

```powershell
python scripts/validate.py
```

Обёртки для окружений, где разрешён запуск скриптов:

```text
scripts\validate.ps1
./scripts/validate.sh
```

Обе команды запускают `scripts/validate.py`. Результат считается успешным только
при коде возврата `0` и строке `VALIDATION_RESULT: PASS`.

## Правила пилота

1. Каждая задача начинается с GitHub Issue и измеримых критериев приёмки.
2. Maker работает только в ветке `agent/issue-<номер>-<описание>`.
3. Maker не утверждает и не объединяет собственный результат.
4. Checker не меняет реализацию: он запускает единую проверку и сообщает PASS/FAIL.
5. Pull Request создаётся черновиком. Issue закрывается только после Merge.
6. Секреты хранятся только вне Git; `.env.example` содержит пустые значения.

Подробные контракты ролей находятся в [`AGENTS.md`](AGENTS.md) и каталоге
[`/.agents`](.agents/).
