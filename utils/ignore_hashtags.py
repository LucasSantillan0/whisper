import re

def ignoreHasthags(text):
  match = re.search(r'(?s)(.*?)(##){3}', text)
  if match:
    return match.group(1).strip()
  else:
    return text.strip()