import math
def calculateStats(numbers):
  cs = {}
  cs["avg"] = math.nan
  cs["max"] = math.nan
  cs["min"] = math.nan

  if len(numbers) > 0:
    cs["avg"] = sum(numbers) / len(numbers)
    cs["max"] = max(numbers)
    cs["min"] = min(numbers)
    
  return cs
