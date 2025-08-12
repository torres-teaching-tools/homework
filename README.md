# Jasper CLI – Course Helper Tool

`jasper` is the command-line helper for our programming assignments.  
It runs inside your GitHub Codespace and gives you quick commands for:

- **Explaining** an assignment: `jasper explain <problem>`
- **Get** starter code: `jasper get <problem>`
- **Checking** your solution locally: `jasper check`
- **Submitting** your solution for grading: `jasper submit`
- **Viewing badges** you’ve earned: `jasper badges`

Think of it as your course toolbox — one command instead of typing long scripts.

---

## 📦 Installing `jasper` in your Codespace

You **do not** need to remember `pipx` commands.  
Your course template repo already has a `Makefile` with helper targets.

From your Codespace terminal, run:

```bash
make jasper-install
```

This will:
1. Install [`pipx`](https://pypa.github.io/pipx/) if needed.
2. Ensure your PATH is set.
3. Install the latest version of `jasper` so you can run it anywhere in the Codespace.

Once installed, test it:

```bash
jasper --help
```

---

## 🔄 Updating `jasper`

Your instructor may release new versions during the semester.  
To update to the latest version, run:

```bash
make jasper-update
```

This will pull the newest release and replace your current installation.

---

## 🛠 Common Commands

```bash

jasper get <problem_id>     # Download starter files
cd problem_id-name-of-folder # Change directory in to the problem folder
jasper explain              # Show details about an assignment
jasper check                # Run local unit tests (compilation, tests, etc.)
jasper crit                 # Reviews your code for maintainability and readability (AI)
jasper submit               # Submits your solution
jasper badges               # Show your progress and earned badges
```

Run `jasper <command> --help` to see options for that command.

---

## ❓ Troubleshooting

**`bash: jasper: command not found`**  
- Run `make jasper-install` again to reinstall and refresh your PATH.  
- If you just installed, restart your terminal.

**I updated but nothing changed**  
- Run `make jasper-update`.  
- If problems persist, try:
  ```bash
  make jasper-uninstall
  make jasper-install
  ```

---

## 📌 Notes
- `jasper` is only supported inside our GitHub Codespaces environment for this course.
- Always run `make jasper-update` before starting a new assignment.
