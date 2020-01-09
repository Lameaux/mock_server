from flask import jsonify, render_template
import uuid

from . import dstvza


@dstvza.route('/GetOAuthTokenAPI', methods=['get', 'post'])
def oauth():
    ret = dict(expires_in=1295999, token_type='Bearer', access_token=str(uuid.uuid4()))
    return jsonify(ret), 201


@dstvza.route('/ShowmaxExtApi/partners/showmax/agreements', methods=['get', 'post'])
def agreements():
    return jsonify({}), 201


@dstvza.route('/ShowmaxExtApi/partners/showmax/agreements/<string:charge_token>', methods=['get', 'post', 'put'])
def agreement(charge_token):
    return jsonify({'charge_token': charge_token}), 201



@dstvza.route('showmaxperformanceapi/zaf/customers/customer-detail/identityNumber=<string:identity_number>')
def customer(identity_number):
    return jsonify({'identity_number': identity_number}), 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/ZAF/customers/<string:customer_number>/activations', methods=['get', 'post'])
def activations(customer_number):
    return jsonify({'customer_number': customer_number}), 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/ZAF/customers/<string:customer_number>/agreements/eligibility')
def eligibility(customer_number):
    return jsonify({'customer_number': customer_number}), 200





