#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Flask base application declaration and URL configuration."""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.bank import BankDetails
from resources.branch import BranchDetails

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['PROPAGATE_EXCEPTIONS'] = True

# ------------------------------------------------------------------------------
# Property Management Services
# ------------------------------------------------------------------------------

# http://server/api/v1/add_building
api.add_resource(BankDetails, '/api/v1/bank/<string:ifsc_code>')

# http://server/api/v1/add_building
api.add_resource(BranchDetails, '/api/v1/<string:bank_name>/bank/<string:city_name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
