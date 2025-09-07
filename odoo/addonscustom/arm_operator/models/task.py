from odoo import models, fields
from datetime import datetime

class ArmOperatorTask(models.Model):
    _name = 'arm.operator.task'
    _description = 'Задание оператора'

    order_number = fields.Integer(string="Номер заказа")
    order_name = fields.Char(string="Название заказа")
    status = fields.Selection([
        ('ready', 'Готово к работе'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
        ('defect', 'Брак'),
    ], string="Статус", default="ready")

    start_time = fields.Datetime(string="Время начала")
    end_time = fields.Datetime(string="Время окончания")
    # Для отображения "скрыть строку" при статусе done
    is_done = fields.Boolean(compute='_compute_is_done')

    def _compute_is_done(self):
        for rec in self:
            rec.is_done = (rec.status == 'done')

    def action_take(self):
        for record in self:
            record.status = 'in_progress'
            record.start_time = datetime.now()
            record.end_time = False
        return True

    def action_done(self):
        for record in self:
            record.status = 'done'
            record.end_time = datetime.now()
        return True

    def action_defect(self):
        for record in self:
            record.status = 'defect'
            record.end_time = datetime.now()
        return True

    # Заглушки для кнопок "Подробнее" и "Файлы"
    def action_more(self):
        return True

    def action_files(self):
        return True
