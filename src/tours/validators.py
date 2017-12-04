from django.core.exceptions import ValidationError

def validate_phone(value):
    # result_phone = re.match(r'^((8|\+375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}$', value)
    # if !result_phone:
        # raise ValidationError("Введите правильный телефон")
    pass

def validate_name(value):
    # result_name = re.match(r'^[А-Яа-я]+$', value)
    # if !result_name:
        # raise ValidationError("Введите правильное имя")
    pass