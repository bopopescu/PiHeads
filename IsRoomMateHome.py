import http.client

conn = http.client.HTTPSConnection('enwemnmn9zugj.x.pipedream.net')
conn.request("POST", "/", '{ "name": "Han Solo" }', {'Content-Type': 'application/json'})