from telegram import Bot, Update
from telegram.ext import  CommandHandler

INPUT_RAC , INPUT_COMPLEX , END_CALC, INIT_CALC, CALC = range(5)

def init_calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Это Мистер Калькуляторик!\n '
                                                      'С какими чиселками вы хотите работать??\n '
                                                      'Если с рациональными - введите "1"\n'
                                                      ' Если с комплексными - введите "2"')
    return CALC

def calc(update, _):
    number = update.message.text

    if number == "1":
        return INPUT_RAC
    elif number == "2":
        return  INPUT_COMPLEX



def rac_calc(update, context):

    context.bot.send_message(update.effective_chat.id, 'Введите первое число: ')
    left_value = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введите операцию: ')
    oper = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введите второе число: ')
    right_value = update.message.text

    if oper == "+":
        return (left_value + right_value)
    elif oper == "-":
        return left_value + right_value
    elif oper == "*":
        return left_value + right_value
    elif oper == "/":
        return left_value + right_value
    return  END_CALC


def end_calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Хотите выйти из калькулятора??\n Введите "Да" ')

