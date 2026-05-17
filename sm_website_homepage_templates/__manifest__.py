# -*- coding: utf-8 -*-
{
    'name': 'Website Homepage Templates Pro',
    'version': '18.0.1.2.0',
    'category': 'Website',
    'summary': 'Premium homepage template selector with 20 public landing pages, 5 full-flow layouts, custom branding, preview, and one-click apply as Odoo homepage.',
    'description': """
Website Homepage Templates Pro for Odoo 18
==========================================

Turn the default Odoo website homepage into a polished public landing page
before users sign in. This premium template pack gives admins 20 ready homepage
styles, 5 richer full-flow layouts, editable branding, CTA controls, preview,
and one-click apply as website homepage without editing code.

Main Features
-------------

* 20 ready public homepage templates
* 5 richer full-flow templates for iLanding, Company, Arsha, BizLand, and UpConstruction
* Real preview screenshots included in the Odoo Apps description page
* Finance / Service, Agency / Marketing, Clinic / Healthcare, Corporate / Business, and SaaS / Startup templates
* Arsha, BizLand, Bootslander, Dewi, FlexStart, Impact, KnightOne, Mentor, OnePage, Sailor, Selecao, eNno, Gp, MediCio, and UpConstruction-inspired templates
* Website Settings configuration panel
* Enable or disable landing homepage from settings
* Template selector stored in Odoo system parameters
* Custom brand name
* Custom hero title
* Custom hero subtitle
* Custom phone number
* Custom CTA button label
* Custom CTA button URL
* Preview selected template in a new tab
* Apply selected template as website homepage
* Automatic homepage URL setup when enabled
* Revert homepage URL when disabled
* Public website route for each template
* Native Odoo Sign In button
* Contact CTA support
* Responsive desktop, tablet, and mobile layout
* Custom hero imagery per template
* Polished first-screen landing page before login
* Lightweight QWeb implementation
* Frontend CSS bundled through Odoo assets
* Multi-website friendly settings flow
* ThemeWagon and BootstrapMade attribution kept visible
* Professional homepage template pack for lead generation and website conversion
* Ideal for agencies, consultants, clinics, schools, SaaS products, construction companies, portfolios, and service businesses
* Useful upsell base for custom website implementation projects

Search Keywords
---------------

Odoo website homepage, Odoo landing page, Odoo homepage template, custom Odoo
homepage, Odoo login landing page, Odoo website template, Odoo 18 website
template, Odoo public homepage, Odoo pre-login homepage, website landing
template, premium Odoo website templates, Odoo homepage template selector,
ThemeWagon Odoo templates, BootstrapMade Odoo template, Odoo website landing
page, Odoo homepage before login, Odoo corporate homepage, Odoo SaaS landing
page, Odoo agency homepage, Odoo medical homepage, Odoo construction homepage,
Odoo education homepage, Odoo portfolio homepage, Odoo service business
homepage, Odoo startup landing page, Odoo website theme selector, Odoo
no-code homepage, Odoo lead generation homepage.
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/browse?order=Newest&repo_maintainer_id=512936',
    'license': 'OPL-1',
    'price': 38.92,
    'currency': 'USD',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/homepage_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'sm_website_homepage_templates/static/src/css/homepage_templates.css',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
