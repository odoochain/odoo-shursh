# Copyright 2019-2021 Artem Shurshilov
# Odoo Proprietary License v1.0

# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, or if you have received a written
# agreement from the authors of the Software (see the COPYRIGHT file).

# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).

# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.

# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from odoo import api, fields, models


class ResConfigSettingsIapFirebase(models.TransientModel):
    _inherit = "res.config.settings"

    res_users_firebase_title_web = fields.Char(
        string="Firebase title web", help="Secret firebase title web-app"
    )
    res_users_firebase_body_web = fields.Char(
        string="Firebase body web", help="Secret firebase body web-app"
    )
    res_users_firebase_icon_web = fields.Char(
        string="Firebase icon web", help="Secret firebase icon web-app"
    )
    res_users_firebase_image_web = fields.Char(
        string="Firebase image web", help="Secret firebase image web-app"
    )
    res_users_firebase_action_web = fields.Char(
        string="Firebase action web", help="Secret firebase action web-app"
    )
    mail_firebase_key = fields.Char(
        string="Mail Firebase key",
        help="Secret firebase key",
    )

    def set_values(self):
        res = super().set_values()
        config_parameters = self.env["ir.config_parameter"]
        config_parameters.set_param("mail_firebase_key", self.mail_firebase_key)
        config_parameters.set_param(
            "res_users_firebase_title_web", self.res_users_firebase_title_web
        )
        config_parameters.set_param(
            "res_users_firebase_body_web", self.res_users_firebase_body_web
        )
        config_parameters.set_param(
            "res_users_firebase_icon_web", self.res_users_firebase_icon_web
        )
        config_parameters.set_param(
            "res_users_firebase_image_web", self.res_users_firebase_image_web
        )
        config_parameters.set_param(
            "res_users_firebase_action_web", self.res_users_firebase_action_web
        )
        return res

    @api.model
    def get_values(self):
        res = super().get_values()
        mail_firebase_key = self.env["ir.config_parameter"].get_param(
            "mail_firebase_key"
        )
        res.update(mail_firebase_key=mail_firebase_key)
        res.update(
            res_users_firebase_title_web=self.env[
                "ir.config_parameter"
            ].get_param("res_users_firebase_title_web")
        )
        res.update(
            res_users_firebase_body_web=self.env[
                "ir.config_parameter"
            ].get_param("res_users_firebase_body_web")
        )
        res.update(
            res_users_firebase_icon_web=self.env[
                "ir.config_parameter"
            ].get_param("res_users_firebase_icon_web")
        )
        res.update(
            res_users_firebase_image_web=self.env[
                "ir.config_parameter"
            ].get_param("res_users_firebase_image_web")
        )
        res.update(
            res_users_firebase_action_web=self.env[
                "ir.config_parameter"
            ].get_param("res_users_firebase_action_web")
        )
        return res
