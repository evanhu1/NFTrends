from flask import Flask, request, abort, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

def open():
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '71B30sF829FL586'
    app.config['MYSQL_DATABASE_DB'] = 'nftrends'
    app.config['MYSQL_DATABASE_HOST'] = '35.197.29.194'
    mysql.init_app(app)
    connection = mysql.connect()
    return connection

conn = open()
cursor = conn.cursor()
sql = "SELECT * FROM analytics"
cursor.execute(sql)
print(cursor.fetchall())

@app.route('/api/data', methods = ["GET"])
def getData():
    cursor = conn.cursor()
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    return result

@app.route('/api/nft_collections', methods = ["GET"])
def getCollections():
    cursor = conn.cursor()
    sql = "SELECT * FROM nft_collections"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    return result

@app.route('/api/analytics', methods = ["GET"])
def getAnalytics():
    cursor = conn.cursor()
    sql = "SELECT * FROM analytics"
    cursor.execute(sql)
    result = jsonify(cursor.fetchall())
    cursor.close()
    return result

@app.route('/api/nft_collections', methods=['POST'])
def postCollections():
    # Check if valid request
    if not request.is_json():
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor()
    
    # POST to nft_collections
    insertTweet = "INSERT INTO nft_collections(collection_name, image_url, description) VALUES (%s, %s, %s)"
    cursor.execute(insertTweet, [data["collection_name"], data["image_url"], data["description"]])
    conn.commit()
    return 201

@app.route('/api/data', methods=['POST'])
def postData():
    # Check if valid request
    if not request.is_json:
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor()
    
    # GET NFT collection ID
    checkID = "SELECT id FROM nft_collections WHERE nft_collection = %s"
    cursor.execute(checkID, [data["name"]])
    id = cursor.fetchone()[0]

    # POST tweet to data
    insertTweet = "INSERT INTO data VALUES (%i, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insertTweet, [id, data["time"], data["retweet_count"], data["reply_count"], data["like_count"], data["quote_count"]])
    conn.commit()
    return 201

@app.route('/api/analytics', methods=['POST'])
def postAnalytics():
    # Check if valid request
    if not request.is_json():
        abort(400)
    
    data = request.get_json(force=True);
    cursor = conn.cursor()
    
    # POST to analytics
    insertAnalysis = "INSERT INTO analytics VALUES (%i, %s)"
    cursor.execute(insertAnalysis, [data["analytic"]])
    conn.commit()
    return 201