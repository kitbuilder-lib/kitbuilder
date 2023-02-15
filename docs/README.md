![KitBuilder](/assets/header.png)

<div align="center">

# Documentation

</div>

## Usage
To use it, install KitBuilder library suitable for your programming language, import `Kit` class from `kitbuilder`, provide it with `filepath` and call `build()` function which will return class you can use as SDK.

## **name**: `string`
> Name of the SDK class

### Example
```yaml
name: SDK
```

## **description**: `string`
> Description of the SDK class

### Example
```yaml
description: SDK Description
```

## **import**: `string`
> File path of another YAML definition

### Example
```yaml
import: ../../file.api.yml
```

## **construct**: `array`
> Array of constructor arguments

### Example
```yaml
construct:
    - api_key
```

## **environment**: `object`
> Object of environment variables

### Example
```yaml
environment:
    API_URL: https:://...
```

## **functions**: `object`
> Object of function definitions

### Example
```yaml
functions:
    get:
        ...
```

## **functions.<NAME>.type**: `request` | `cli`
> Function type definition

### Example
```yaml
functions:
    get:
        type: cli | request
```

## **functions.<NAME>.args**: `array`
> Function arguments

### Example
```yaml
functions:
    get:
        args:
            - type
```

## **functions.<NAME>.config**: `object`
> Configuration object for given function type

### Example
```yaml
functions:
    get:
        config:
            url: "%{{ [environment][API_URL] }}%"
            method: get
            headers: ...
            ...
```

## Variables
> Currently you can only get variables from `args`, `environment` and `construct` properties. To access them in different strings, use: `%{{ [VARIABLE_LOCATION][VARIABLE_NAME] }}%`. 

### Example:
```yaml
...
config:
    cmd: echo %{{ msg }}%
```