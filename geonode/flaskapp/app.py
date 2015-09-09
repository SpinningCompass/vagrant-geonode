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


    results = db.session.execute("""SELECT \
                          ST_AsGeoJSON("TM_WORLD_BORDERS_SIMPL_0.35".the_geom) as geom, \
                          "TM_WORLD_BORDERS_SIMPL_0.35"."ISO2" as iso2, \
                          "TM_WORLD_BORDERS_SIMPL_0.35"."NAME" as name\
                        FROM \
                          public."TM_WORLD_BORDERS_SIMPL_0.35";""")
    for row in results:
        tempfeature = { "type": "Feature",
            "geometry": json.loads(row['geom']),
            "properties": {
                        "iso2": row['iso2'],
                        "name": row['name']
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