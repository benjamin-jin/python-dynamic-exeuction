# python-dynamic-exeuction

Load module, or member of module from string. The following is an example

```python3
datetime_module = execute("datetime")
print(datetime_module.datetime.now())
dateteim_datetime_now_function = execute("datetime.datetime.now")
print(dateteim_datetime_now_function())
```
