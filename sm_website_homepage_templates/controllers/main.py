# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


SM_TEMPLATE_META = {
    'arsha': ('Startup Homepage', 'arsha-hero.png', 'Launch Ready', 'Clean startup homepage with strong first screen.', 'Startup', 'Modern UI', 'Odoo'),
    'bizland': ('Service Homepage', 'bizland-hero.jpg', 'Service Ready', 'Strong service and company homepage layout.', 'Service', 'Lead CTA', 'Public'),
    'bootslander': ('App Homepage', 'bootslander-hero.png', 'App Showcase', 'Landing page for software, app, and digital tools.', 'App', 'Preview', 'CTA'),
    'dewi': ('Digital Agency', 'dewi-hero.jpg', 'Agency Ready', 'Bold image-led homepage for agencies and services.', 'Agency', 'Hero', 'Sales'),
    'flexstart': ('Creative Homepage', 'flexstart-hero.png', 'Creative Start', 'Friendly visual layout for growing businesses.', 'Creative', 'Flexible', 'Fast'),
    'impact': ('Consulting Homepage', 'impact-hero.jpg', 'Business Impact', 'Professional homepage for consulting and advisory.', 'Trust', 'Impact', 'Leads'),
    'knightone': ('Portfolio Homepage', 'knightone-hero.jpg', 'Portfolio Style', 'Dark visual homepage for creators and premium brands.', 'Brand', 'Visual', 'Premium'),
    'mentor': ('Education Homepage', 'mentor-hero.jpg', 'Learning Ready', 'Education and course homepage before login.', 'Course', 'Learn', 'Enroll'),
    'onepage': ('Product Homepage', 'onepage-hero.jpg', 'One Page Flow', 'Focused homepage for product and company stories.', 'Product', 'Story', 'CTA'),
    'sailor': ('Corporate Homepage', 'sailor-hero.jpg', 'Corporate Ready', 'Classic company homepage for teams and services.', 'Company', 'Team', 'Trust'),
    'selecao': ('Creative Homepage', 'selecao-hero.jpg', 'Creative Flow', 'Portfolio-inspired page for creative businesses.', 'Work', 'Showcase', 'CTA'),
    'enno': ('Business Homepage', 'enno-hero.png', 'Simple Business', 'Clean business front page with fast setup.', 'Simple', 'Clean', 'Ready'),
    'gp': ('Agency Homepage', 'gp-hero.jpg', 'Agency Lead Page', 'High contrast homepage for bold lead generation.', 'Agency', 'Bold', 'Leads'),
    'medicio': ('Medical Homepage', 'medicio-hero.jpg', 'Medical Front Desk', 'Healthcare homepage with clear contact path.', 'Clinic', 'Care', 'Booking'),
    'upconstruction': ('Construction Homepage', 'upconstruction-hero.jpg', 'Project Ready', 'Construction and builder homepage with strong visuals.', 'Build', 'Project', 'Quote'),
}


class WebsiteHomepageTemplates(http.Controller):

    @http.route(['/sm/home', '/sm/home/<string:template_key>'], type='http', auth='public', website=True, sitemap=True)
    def sm_homepage(self, template_key=None, **kwargs):
        params = request.env['ir.config_parameter'].sudo()
        template = template_key or params.get_param('sm_website_homepage_templates.template', 'vaultedge')
        if template not in ('vaultedge', 'monoline', 'clinic', 'company', 'ilanding') and template not in SM_TEMPLATE_META:
            template = 'vaultedge'
        meta = SM_TEMPLATE_META.get(template)
        template_meta = False
        if meta:
            template_meta = {
                'eyebrow': meta[0],
                'image': '/sm_website_homepage_templates/static/src/img/%s' % meta[1],
                'panel_title': meta[2],
                'panel_text': meta[3],
                'stat_one': meta[4],
                'stat_two': meta[5],
                'stat_three': meta[6],
            }
        values = {
            'template_key': template,
            'template_meta': template_meta,
            'brand_name': params.get_param('sm_website_homepage_templates.brand_name') or request.website.name,
            'hero_title': params.get_param('sm_website_homepage_templates.hero_title') or 'Build a sharper website before users sign in.',
            'hero_subtitle': params.get_param('sm_website_homepage_templates.hero_subtitle') or 'Launch a clean public homepage for Odoo with a focused message, strong CTA, and native sign-in access.',
            'phone': params.get_param('sm_website_homepage_templates.phone') or '+1 555-555-5556',
            'cta_label': params.get_param('sm_website_homepage_templates.cta_label') or 'Contact Us',
            'cta_url': params.get_param('sm_website_homepage_templates.cta_url') or '/contactus',
        }
        return request.render('sm_website_homepage_templates.homepage', values)
