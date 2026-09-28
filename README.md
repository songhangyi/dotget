# dotget

Read `data["a"]["b"]` as `dig(data, "a.b")`. A missing key returns the default. An empty path segment is an error.

```python
from dotget import dig

dig({"a": {"b": 1}}, "a.b")
```

```bash
python -m unittest test_dotget.py
```

MIT
