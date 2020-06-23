import codecs
import csv

import phonenumbers

from ..models import Teacher

from PIL import Image
import glob


class InvalidRow(Exception):
    pass


def process_import(file):
    csvfile = csv.DictReader(codecs.iterdecode(file, 'utf-8'))

    success = True
    count = 0

    invalid_row = InvalidRow()

    for r in csvfile:
        model = dict(
            first_name=None,
            last_name=None,
            profile_picture=None,
            email_address=None,
            phone_number=None,
            room_number=None,
        )
        try:
            for key, value in r.items():
                slug = key.replace(' ', '_').lower()

                # row validation
                if slug == 'first_name' or slug == 'last_name':
                    if not value:
                        raise invalid_row

                if slug == 'phone_number':
                    try:
                        value = phonenumbers.parse(value, 'AE')
                        model[slug] = '{}{}'.format(
                            value.country_code,
                            value.national_number
                        )
                    except Exception as e:  # noqa
                        continue

                elif slug == 'profile_picture':
                    globs = glob.glob(f'listing/assets/{value}')

                    if globs:
                        model[slug] = value
                    else:
                        model[slug] = '400.png'

                elif slug == 'subjects_taught':
                    subjects = value.split(',')

                    if len(subjects) <= 5:
                        model[slug] = ', '.join(subjects)
                    else:
                        continue

                else:
                    model[slug] = value

        except InvalidRow as ir:  # noqa
            print('invalid row raised')
            continue

        Teacher.objects.create(**model)
        count += 1

    return success, count
