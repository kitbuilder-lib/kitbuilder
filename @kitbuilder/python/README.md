# 🔧KitBuilder🔧

KitBuilder is a library used for generating API-based and CLI-based SDK for multiple programming languages using only one definition file!

# Tutorial

Initialization is pretty straight-forward. Simply install the package for your programming language, import and run `build` function.

> Tutorial below showcases how to run KitBuilder on Python

1. Install KitBuilder package

```
pip3 install kitbuilder
```

2. Create YAML definition with the name of `dog.api.yaml`:

```yaml
name: DogAPI
description: Showcase

environment:
    # Will be using DogCEO API
    API_URL: https://dog.ceo

functions:
    get:
        type: request

        args:
            - breed

        config:
            method: GET
            url: "%{{ [environment][API_URL] }}%/api/breed/%{{ [args][breed] }}%/images/random"
```

3. Import and run!

```python
from kitbuilder import Kit

DogAPI = Kit("dog.api.yml").build()

api = DogAPI()

pitbull = api.get("pitbull")

print(pitbull.json())
```

# Support

> ***NOTE*** Since KitBuilder is currently `v0.1`, it will be heavily limited in functionality and usage across different programming languages. Goal is to have at least 5 different programming languages supported

Currently, KitBuilder is supported for:

* `Python`
