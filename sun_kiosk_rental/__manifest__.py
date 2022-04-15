{
    'name': "Sun - Kiosk Management Rental",
    'name_vi_VN': "Sun - Quản lý thuê Kiosk",

    'summary': """
    The module will allow to manage the costs of the kiosk rental
    """,
    'summary_vi_VN': """
    Mô-đun sẽ cho phép quản lý các chi phí việc cho thuê kiosk
    """,

    'description': """
What it does
============
* The module will provide features for managing rentals and utilities,
  surcharges associated with renting a shop/Kiosk

    """,

    'description_vi_VN': """
Mô tả
=====
* Mô-đun sẽ cung cấp các tính năng về quản lý việc cho thuê và các chi phí điện nước,
 phụ phí liên quan tới việc thuê cửa hàng/Kiosk


    """,

    'author': "Sun group",
    'website': 'https://www.sungroup.com.vn/',
    'category': 'Rental',
    'version': '0.1.0',
    'depends': ['base',
                'mail'],
    'data': [
#         'data/template_email_data.xml',
        'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/menu_root.xml',
        'views/contract_cost_type_views.xml',
        'views/cost_type_views.xml',
        'views/kiosk_contract_views.xml',
        'views/kiosk_electric_number_views.xml',
        'views/kiosk_kiosk_views.xml',
#         'views/kiosk_payment_line_views.xml',
        'views/kiosk_payment_views.xml',
        'views/kiosk_water_number_views.xml',
        'views/res_partner_views.xml'
        ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}
