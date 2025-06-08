def find(xs, fn):
  for x in xs:
    if fn(x):
      return x
  return None


def group_by(xs, fn):
  d = {}
  for x in xs:
    v = fn(x)
    d.setdefault(v, [])
    d[v].append(x)
  return [*d.values()]
