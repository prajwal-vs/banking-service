#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json

from flask import request
from flask_restful import Resource

from services.bankManagement import BankService


class BankDetails(Resource):

    def __init__(self):
        self.service = BankService()

    def get(self, ifsc_code):
        """ Get  """

        limit = request.args.get("limit", 10)
        offset = request.args.get("offset", 0)
        keyword = request.args.get("keyword", "")

        response = self.service.get_bank(ifsc_code,limit, offset, keyword)
        return response



