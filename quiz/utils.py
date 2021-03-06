from random import randint

import requests
from django.conf import settings
from django.db.models import Count


PARTY_SHORT_NAMES = {
    'Arbeiderpartiet': 'Ap',
    'Fremskrittspartiet': 'FrP',
    'Høyre': 'H',
    'Kristelig Folkeparti': 'KrF',
    'Miljøpartiet De Grønne': 'MDG',
    'Rødt': 'R',
    'Senterpartiet': 'Sp',
    'Sosialistisk Venstreparti': 'SV',
    'Venstre': 'V'
}

PARTY_SHORT_NAME_SLUGS = dict({k: v.lower() for k, v in PARTY_SHORT_NAMES.items()})


def get_google_sheet_data():
    from quiz.models import GoogleProfile
    """ Ref: https://github.com/google/oauth2client/blob/master/oauth2client/contrib/django_util/__init__.py#L188
        Ref: https://github.com/google/oauth2client/tree/master/samples/django/django_user
    """
    access_token = get_google_access_token()
    if not access_token:
        return []

    params = {
        'access_token': access_token
    }
    url = 'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/promises'.format(
        spreadsheet_id=settings.GOOGLE_SPREADSHEET_ID)
    res = requests.get(url, params).json()

    if res.get('error') and res['error']['code'] == 401:
        # Reset access_token
        GoogleProfile.objects.all().delete()
        return []

    return res.get('values')


def get_google_access_token():
    from quiz.models import GoogleProfile
    gp = GoogleProfile.objects.first()
    return gp.credential.access_token if gp else None


def get_promise_id(promise_document):
    return promise_document['_links']['self']['href'].split('/')[-1]


def format_question(promise, question_type='checked'):
    # TODO: You are here
    # TODO: Move this
    from quiz.models import Party
    if question_type == 'checked':
        return {
            'possible': [promise.FULFILLED, promise.BROKEN],
            'answer': promise.status
        }
    elif question_type == 'a_or_b':
        right = promise.parties.first()

        wrong_parties = Party.objects.filter(pk=right.pk)
        count = wrong_parties.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        wrong = wrong_parties[random_index]

        return {
            'possible': [right, wrong],
            'answer': right
        }
    elif question_type == 'true_or_false':
        return {
            'possible': [True, False],
            'answer': promise
        }
