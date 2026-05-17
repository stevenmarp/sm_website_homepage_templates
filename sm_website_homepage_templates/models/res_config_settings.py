# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sm_homepage_template_enabled = fields.Boolean(
        string='Enable Landing Homepage',
        config_parameter='sm_website_homepage_templates.enabled',
    )
    sm_homepage_template = fields.Selection([
        ('vaultedge', 'Finance / Service'),
        ('monoline', 'Agency / Marketing'),
        ('clinic', 'Clinic / Healthcare'),
        ('company', 'Corporate / Business'),
        ('ilanding', 'SaaS / Startup'),
        ('arsha', 'Arsha / Startup'),
        ('bizland', 'BizLand / Service'),
        ('bootslander', 'Bootslander / App'),
        ('dewi', 'Dewi / Digital Agency'),
        ('flexstart', 'FlexStart / Creative'),
        ('impact', 'Impact / Consulting'),
        ('knightone', 'KnightOne / Portfolio'),
        ('mentor', 'Mentor / Education'),
        ('onepage', 'OnePage / Product'),
        ('sailor', 'Sailor / Corporate'),
        ('selecao', 'Selecao / Creative'),
        ('enno', 'eNno / Business'),
        ('gp', 'Gp / Agency'),
        ('medicio', 'MediCio / Medical'),
        ('upconstruction', 'UpConstruction / Builder'),
    ], string='Homepage Template', default='vaultedge', config_parameter='sm_website_homepage_templates.template')
    sm_homepage_brand_name = fields.Char(
        string='Brand Name',
        config_parameter='sm_website_homepage_templates.brand_name',
    )
    sm_homepage_hero_title = fields.Char(
        string='Hero Title',
        config_parameter='sm_website_homepage_templates.hero_title',
    )
    sm_homepage_hero_subtitle = fields.Char(
        string='Hero Subtitle',
        config_parameter='sm_website_homepage_templates.hero_subtitle',
    )
    sm_homepage_phone = fields.Char(
        string='Phone',
        config_parameter='sm_website_homepage_templates.phone',
    )
    sm_homepage_cta_label = fields.Char(
        string='CTA Label',
        config_parameter='sm_website_homepage_templates.cta_label',
    )
    sm_homepage_cta_url = fields.Char(
        string='CTA URL',
        config_parameter='sm_website_homepage_templates.cta_url',
    )

    def _sm_get_homepage_config_values(self):
        self.ensure_one()
        return {
            'enabled': self.sm_homepage_template_enabled,
            'template': self.sm_homepage_template or 'vaultedge',
            'brand_name': self.sm_homepage_brand_name or self.env.company.name,
            'hero_title': self.sm_homepage_hero_title or 'Build a sharper website before users sign in.',
            'hero_subtitle': self.sm_homepage_hero_subtitle or 'Launch a clean public homepage for Odoo with a focused message, strong CTA, and native sign-in access.',
            'phone': self.sm_homepage_phone or '+1 555-555-5556',
            'cta_label': self.sm_homepage_cta_label or 'Contact Us',
            'cta_url': self.sm_homepage_cta_url or '/contactus',
        }

    def _sm_save_homepage_config(self):
        params = self.env['ir.config_parameter'].sudo()
        for key, value in self._sm_get_homepage_config_values().items():
            params.set_param('sm_website_homepage_templates.%s' % key, value)

    def _sm_get_current_website(self):
        return self.website_id if 'website_id' in self._fields else self.env['website'].get_current_website()

    def _sm_apply_homepage_url(self):
        self._sm_get_current_website().homepage_url = '/sm/home'

    def set_values(self):
        res = super().set_values()
        if self.sm_homepage_template_enabled:
            self._sm_apply_homepage_url()
        elif self._sm_get_current_website().homepage_url == '/sm/home':
            self._sm_get_current_website().homepage_url = False
        return res

    def action_sm_preview_homepage(self):
        self._sm_save_homepage_config()
        return {
            'type': 'ir.actions.act_url',
            'url': '/sm/home/%s' % (self.sm_homepage_template or 'vaultedge'),
            'target': 'new',
        }

    def action_sm_apply_homepage(self):
        self._sm_save_homepage_config()
        self._sm_apply_homepage_url()
        self.env['ir.config_parameter'].sudo().set_param('sm_website_homepage_templates.enabled', True)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Homepage Applied'),
                'message': _('Selected landing template is now used as the website homepage.'),
                'type': 'success',
                'sticky': False,
            },
        }
