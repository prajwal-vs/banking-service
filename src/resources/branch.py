#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from services.bankManagement import BankService


class BranchDetails(Resource):

    def __init__(self):
        self.service = BankService()

    def get(self, bank_name, city_name):
        """ Get """

        limit = request.args.get("limit", 10)
        offset = request.args.get("offset", 0)
        keyword = request.args.get("keyword", "")

        result = self.service.get_branch(bank_name, city_name, limit, offset, keyword)
        return result
