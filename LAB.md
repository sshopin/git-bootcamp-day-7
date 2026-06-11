# LAB — день 7

> Скопируйте в `LAB.md` в корне `git-bootcamp-day-7` на **GitHub** и заполните по ходу работы.

## Базовая задача — `01-platforms-tour`

### Ссылки на репозитории

| Платформа | URL |
|-----------|-----|
| GitHub (основной) | https://github.com/sshopin/git-bootcamp-day-7 |
| GitLab | https://gitlab.com/sshopin/git-bootcamp-day-7 |
| GitFlic | https://gitflic.ru/project/sshopin/git-bootcamp-day-7 |
| GitVerse | https://gitverse.ru/sshopin/git-bootcamp-day-7 |

### GitLab — скриншоты (3)

1. SSH-ключ в UI:

![GitLab SSH keys](screenshots/gitlab-ssh-keys.png)

2. Терминал `ssh -T`:

![GitLab ssh -T](screenshots/gitlab-ssh-test.png)

3. Репозиторий после push (ветки + тег):

![GitLab repository](screenshots/gitlab-repo.png)

### GitFlic — скриншоты (3)

1. SSH-ключ в UI:

![GitFlic SSH keys](screenshots/gitflic-ssh-keys.png)

2. Терминал `ssh -T`:

![GitFlic ssh -T](screenshots/gitflic-ssh-test.png)

3. Репозиторий после push:

![GitFlic repository](screenshots/gitflic-repo.png)

### GitVerse — скриншоты (3)

1. SSH-ключ в UI:

![GitVerse SSH keys](screenshots/gitverse-ssh-keys.png)

2. Терминал `ssh -T`:

![GitVerse ssh -T](screenshots/gitverse-ssh-test.png)

3. Репозиторий после push:

![GitVerse repository](screenshots/gitverse-repo.png)

### Таблица сравнения платформ

| Возможность | GitHub | GitLab | GitFlic | GitVerse |
|-------------|--------|--------|---------|----------|
| SSH-ключ через UI | да | да  | да  | да |
| Markdown render в README | да | да | да | да |
| Issues встроены | да | да | Проблемы | Задачи |
| PR / Merge Request | PR | Merge Request | Merge Request | Pull Request |
| Встроенный CI | Actions | CI/CD | CI/CD | Workflows |
| Релизы / теги в UI | да | да | нет | нет |
| Видимость для незалогиненных | да | да  | да  | да  |
| Что-то особенное | нет | тормозит | нет | нет |

### Команды

```bash
# git remote add gitlab git@gitlab.com:sshopin/git-bootcamp-day-7.git
# git remote add gitflic git@gitflic.ru:sshopin/git-bootcamp-day-7.git
# git remote add gitverse git@gitverse.ru:sshopin/git-bootcamp-day-7.git

# git push -u gitflic main --tags
# git push -u gitflic feature/greeting --tags
# git push -u gitlab main --tags
# git push -u gitlab feature/greeting --tags
# git push -u gitverse main --tags
# git push -u gitverse feature/greeting --tags

# ssh -T git@gitlab.com
# ssh -T git@gitflic.ru
# ssh -T git@gitverse.ru
```

### Впечатления (2–3 предложения)

Продвинутыми функциями я не пользовался, с точки зрения обычного использования платформы очень похожи. Выделяется только gitlab, в котором интерфейс тормозит и на gitlab.com, а не только в локальном Community Edition.

---

## ⭐1 — bare headless

**Где bare на VM и URL remote `vm`:**

```bash
git remote add vm git@px-baregit:/srv/git/myrepo.git
git push vm --all
```

![push в bare](screenshots/star1-push.png)

![git log после clone](screenshots/star1-clone-log.png)

---

## ⭐2 — Gitea

**Чем UI Gitea отличается от GitHub (1 абзац):**
На первый взгляд особых отличий не видно, разница выглядит больше косметической. Возможно при углубленной работе проявится.


![Gitea repository](screenshots/star2-gitea-repo.png)

![Gitea issue](screenshots/star2-gitea-issue.png)

![Gitea pull request](screenshots/star2-gitea-pr.png)

---

## ⭐3 — GitLab CE self-hosted

**GitLab CE vs Gitea: RAM, время старта (2–3 предложения):**
жрет много памяти ~8Гб даже при простых проектах, если делать некоторые оптимизации, которые всё равно не сильно снижают требования к памяти.
Gitlab CE - большой проект с большим числом компонентов, время запуска длительное.

![GitLab project](screenshots/star3-gitlab-project.png)

![GitLab merge request](screenshots/star3-gitlab-mr.png)

