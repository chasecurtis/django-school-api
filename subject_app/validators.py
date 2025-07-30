from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject_name):
    error_message = "Subject must be in title case format."

    regex = r"^([A-Z][a-z]+)(\s[A-Z][a-z]+)*$"

    good_subject_name = re.match(regex, subject_name)

    if good_subject_name:
        return subject_name
    else:
        raise ValidationError(error_message)


def validate_professor_name(professor_name):
    error_message = 'Professor name must be in the format "Professor Adam".'

    regex = r"^Professor [A-Z][a-z]+$"

    good_professor_name = re.match(regex, professor_name)

    if good_professor_name:
        return professor_name
    else:
        raise ValidationError(error_message)
