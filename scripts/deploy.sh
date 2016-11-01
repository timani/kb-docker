#!/bin/bash
# Deploy master to knowledge Base on commit

# Check to see if the article Exist
# - Read the ID from the front matter

# 1. If an ID exists then update the article
# 2. Read the ID from the front matter of the markdown and search if an article exists
curl "https://{subdomain}.zendesk.com/api/v2/help_center/articles/search.json?query={search_string}" \
  -v -u {email_address}:{password}

curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{id}.json \
  -d '{"article": {"promoted": false, "position": 42, "comments_disabled": true, "label_names": ["photo", "tripod"]}}' \
  -v -u {email_address}:{password} -X PUT -H "Content-Type: application/json"

# 3. If no ID exists, create the new article as a draft
curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{id}/articles.json \
  -d '{"article": {"title": "How to take pictures in low light", "body": "Use a tripod", "locale": "en-us" }}' \
  -v -u {email_address}:{password} -X POST -H "Content-Type: application/json"
