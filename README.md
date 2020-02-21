To use:

create .pre-commit-config.yaml file with following content:

```
repos:
  - repo: https://github.com/Wonqu/sort_makefile/
    rev: "0.9"
    hooks:
      - id: sort_makefile
```