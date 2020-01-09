from flask import jsonify, render_template, make_response
import uuid

from . import dstvza

CUSTOMER_NUMBER = 12345678


@dstvza.route('/GetOAuthTokenAPI', methods=['get', 'post'])
def oauth():
    r = make_response(render_template('dstvza/oauth.json', access_token=str(uuid.uuid4())))
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/agreements', methods=['get', 'post'])
def agreements():
    customer_number = CUSTOMER_NUMBER
    charge_token = str(uuid.uuid4())
    user_id = str(uuid.uuid4())

    r = make_response(
        render_template(
            'dstvza/agreements.json',
            customer_number=customer_number,
            charge_token=charge_token,
            user_id=user_id
        )
    )
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/agreements/<string:charge_token>', methods=['get', 'post', 'put'])
def agreement(charge_token):
    customer_number = CUSTOMER_NUMBER
    user_id = str(uuid.uuid4())

    r = make_response(
        render_template(
            'dstvza/agreements.json',
            customer_number=customer_number,
            charge_token=charge_token,
            user_id=user_id
        )
    )
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/agreements/<string:charge_token>/charges', methods=['get', 'post'])
def charges(charge_token):
    dstv_transaction_ref = str(uuid.uuid4())
    ext_transaction_ref = str(uuid.uuid4())

    r = make_response(
        render_template(
            'dstvza/charges.json',
            charge_token=charge_token,
            dstv_transaction_ref=dstv_transaction_ref,
            ext_transaction_ref=ext_transaction_ref
        )
    )
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('showmaxperformanceapi/zaf/customers/customer-detail/identityNumber=<int:identity_number>')
def customer(identity_number):

    mapping = {
        '3409045056082': {'customer_number': 38739503, 'phone_number': '827408863'},
        '7702050146087': {'customer_number': 38752143, 'phone_number': '722528322'},
    }

    try:
        customer_data = mapping[str(identity_number)]
    except KeyError:
        customer_data = None

    if customer_data is None:
        r = make_response(
            render_template(
                'dstvza/customer_404.json',
            )
        )
        r.headers.set('Content-Type', 'application/json')
        return r, 404

    r = make_response(
            render_template(
                'dstvza/customer.json',
                identity_number=identity_number,
                customer_data=customer_data
            )
        )
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/ZAF/customers/<int:customer_number>/activations', methods=['get', 'post'])
def activations(customer_number):
    activation_code = str(uuid.uuid4())

    r = make_response(
        render_template(
            'dstvza/activations.json',
            customer_number=customer_number,
            activation_code=activation_code
        )
    )
    r.headers.set('Content-Type', 'application/json')
    return r, 200


@dstvza.route('/ShowmaxExtApi/partners/showmax/ZAF/customers/<int:customer_number>/agreements/eligibility')
def eligibility(customer_number):

    mapping = {
        '38739503': 'IsEligible',
        '38752143': 'HasActiveAgreement'
    }

    try:
        eligibility = mapping[str(customer_number)]
    except KeyError:
        eligibility = 'NotFound'

    r = make_response(
        render_template(
            'dstvza/eligibility.json',
            customer_number=customer_number,
            eligibility=eligibility
        )
    )
    r.headers.set('Content-Type', 'application/json')
    return r, 200






