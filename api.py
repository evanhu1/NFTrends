from typing import Dict
from flask import Flask, request, abort, jsonify
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '71B30sF829FL586'
app.config['MYSQL_DATABASE_DB'] = 'nftrends'
app.config['MYSQL_DATABASE_HOST'] = '35.197.29.194'
mysql.init_app(app)
def open():
    connection = mysql.connect()
    return connection
 
@app.route('/api/analytic', methods=['GET'])
def getAnalytics():
    conn = open()
    cursor = conn.cursor(DictCursor) 
    sql = "SELECT * FROM analytics ORDER BY count DESC"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    conn.close()
    return result
    # jsonify([{"count" : 125125}, {"count" : 5}, {"count" : 3}, {"count" : 1}, {"count" : 2412}])

@app.route('/api/data', methods = ["GET"])
def getData():
    conn = open()
    cursor = conn.cursor(DictCursor)
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    conn.close()
    return result

@app.route('/api/nft_collections', methods = ["GET"])
def getCollections():
    conn = open()
    cursor = conn.cursor(DictCursor)
    sql = "SELECT * FROM nft_collections"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    conn.close()
    return result

@app.route('/api/nft_collections', methods=['POST'])
def postCollections():
    conn = open()
    # Check if valid request
    if not request.is_json():
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor(DictCursor)
    
    # POST to nft_collections
    insertTweet = "INSERT INTO nft_collections(collection_name, image_url, description) VALUES (%s, %s, %s)"
    cursor.execute(insertTweet, [data["collection_name"], data["image_url"], data["description"]])
    cursor.close()
    conn.commit()
    conn.close()
    return data, 201

@app.route('/api/data', methods=['POST'])
def postData():
    conn = open()
    # Check if valid request
    if not request.is_json:
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor(DictCursor)
    
    # GET NFT collection ID
    checkID = "SELECT id FROM nft_collections WHERE nft_collection = %s"
    cursor.execute(checkID, [data["name"]])
    id = cursor.fetchone()[0]

    # POST tweet to data
    insertTweet = "INSERT INTO data VALUES (%i, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insertTweet, [id, data["time"], data["text"], data["retweet_count"], data["reply_count"], data["like_count"], data["quote_count"]])
    cursor.close()
    conn.commit()
    conn.close()
    return data, 201

@app.route('/api/analytic', methods=['POST'])
def postAnalytics():
    conn = open()
    # Check if valid request
    if not request.is_json:
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor()
    # POST to analytics
    insertAnalysis = "INSERT INTO analytics VALUES (%s, %s)"
    cursor.execute(insertAnalysis, [data["id"], data["count"]])
    cursor.close()
    conn.commit()
    conn.close()
    return data, 201
