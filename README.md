# dotget

Read `data["a"]["b"]` as `dig(data, "a.b")`. A missing key returns the default. An empty path segment is an error.

```python
from dotget import dig, has_path

dig({"a": {"b": 1}}, "a.b")
has_path({"a": {"b": 1}}, "a.c")  # False
```

```bash
python -m unittest test_dotget.py
```

MIT
