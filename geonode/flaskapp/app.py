from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/geonode_data'
db = SQLAlchemy(app)


# Set "homepage" to index.html

@app.route('/data.json')
def index(searchstr = None):
    geojsonschema = { "type": "FeatureCollection",
        "features": []
         }


    results = db.session.execute("""SELECT 
                          ST_AsGeoJSON(ST_Multi(ST_Union("TM_WORLD_BORDERS_SIMPL_0.35".the_geom))) as geom
                        FROM 
                          public."TM_WORLD_BORDERS_SIMPL_0.35"
                        GROUP BY "TM_WORLD_BORDERS_SIMPL_0.35"."REGION";""")
    for row in results:
        tempfeature = { "type": "Feature",
            "geometry": json.loads(row['geom']),
            "properties": {
                    }
            }
        geojsonschema['features'].append(tempfeature)


    return jsonify(geojsonschema)

@app.route('/map')
def map():
    return render_template('map.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')