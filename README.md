`find_ida_user_dir` determines the current user's IDA Pro user directory in a platform independent way.

```python
import find_ida_user_dir
user_dir = find_ida_user_dir.find_path()
```

`find_ida_user_dir` first checks for the existence of an `IDAUSR` environment variable: if it is present, that is returned. If not, the correct path of the default user directory as described in the [IDA Pro documentation](https://www.hex-rays.com/products/ida/support/idadoc/1375.shtml) is returned.