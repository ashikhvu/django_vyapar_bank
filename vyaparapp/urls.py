from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register', views.register, name='register'),
    
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('sale_invoices', views.sale_invoices, name='sale_invoices'),
    path('estimate_quotation', views.estimate_quotation, name='estimate_quotation'),
    path('payment_in', views.payment_in, name='payment_in'),
    path('sale_order', views.sale_order, name='sale_order'),
    path('delivery_chellan', views.delivery_chellan, name='delivery_chellan'),
    path('sale_return_cr', views.sale_return_cr, name='sale_return_cr'),

    # created by athul
    path('settings', views.settings, name='settings'),
    path('hide_options', views.hide_options, name='hide_options'),

    path('staffhome/<id>', views.staffhome, name='staffhome'),
    path('adminhome', views.adminhome, name='adminhome'),
    
    
    path('staff_register', views.staff_register, name='staff_register'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('company_reg', views.company_reg, name='company_reg'),
    path('company_reg2', views.company_reg2, name='company_reg2'),
    path('add_company', views.add_company, name='add_company'),
    path('log_page', views.log_page, name='log_page'),
    path('login', views.login, name='login'),
    path('adminaccept/<id>', views.adminaccept, name='adminaccept'),
    path('adminreject/<id>', views.adminreject, name='adminreject'),
    path('View_staff', views.View_staff, name='View_staff'),
    path('companyaccept/<id>', views.companyaccept, name='companyaccept'),
    path('companyreject/<id>', views.companyreject, name='companyreject'),
    path('client_request', views.client_request, name='client_request'),
    path('client_details', views.client_details, name='client_details'),
    path('staff_request', views.staff_request, name='staff_request'),
    path('payment_term', views.payment_term, name='payment_term'),
    path('add_payment_terms', views.add_payment_terms, name='add_payment_terms'),
    path('Allmodule/<uid>', views.Allmodule, name='Allmodule'),
    path('addmodules/<uid>', views.addmodules, name='addmodules'),
    path('client_request_overview/<id>', views.client_request_overview, name='client_request_overview'),
    path('client_details_overview/<id>', views.client_details_overview, name='client_details_overview'),


    
    path('companyreport', views.companyreport, name='companyreport'),
    path('Companyprofile', views.Companyprofile, name='Companyprofile'),
    path('editcompanyprofile', views.editcompanyprofile, name='editcompanyprofile'),
    path('editcompanyprofile_action', views.editcompanyprofile_action, name='editcompanyprofile_action'),
    path('editmodule', views.editmodule, name='editmodule'),
    path('editmodule_action', views.editmodule_action, name='editmodule_action'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
    path('module_updation_details/<mid>', views.module_updation_details, name='module_updation_details'),
    path('module_updation_ok/<mid>', views.module_updation_ok, name='module_updation_ok'),
    path('staff_profile/<sid>', views.staff_profile, name='staff_profile'),
    path('editstaff_profile/<sid>', views.editstaff_profile, name='editstaff_profile'),
    path('editstaff_profile_action/<sid>', views.editstaff_profile_action, name='editstaff_profile_action'),

    path('distributor_home', views.distributor_home, name='distributor_home'),
    path('distributor_reg', views.distributor_reg, name='distributor_reg'),
    path('distributor_reg_action', views.distributor_reg_action, name='distributor_reg_action'),
    path('distributors', views.distributors, name='distributors'),
    path('clients', views.clients, name='clients'),
    path('distributor_request', views.distributor_request, name='distributor_request'),
    path('admin_distributor_accept/<id>', views.admin_distributor_accept, name='admin_distributor_accept'),
    path('admin_distributor_reject/<id>', views.admin_distributor_reject, name='admin_distributor_reject'),
    path('distributor_request_overview/<id>', views.distributor_request_overview, name='distributor_request_overview'),
    path('distributor_details', views.distributor_details, name='distributor_details'),
    path('distributor_details_overview/<id>', views.distributor_details_overview, name='distributor_details_overview'),
    path('dcompany_request', views.dcompany_request, name='dcompany_request'),
    path('dcompany_details', views.dcompany_details, name='dcompany_details'),
    path('dcompany_request_overview/<id>', views.dcompany_request_overview, name='dcompany_request_overview'),
    path('distributor_accept_company/<id>', views.distributor_accept_company, name='distributor_accept_company'),
    path('distributor_reject_company/<id>', views.distributor_reject_company, name='distributor_reject_company'),
    path('dcompany_details_overview/<id>', views.dcompany_details_overview, name='dcompany_details_overview'),
    path('distributor_profile', views.distributor_profile, name='distributor_profile'),
    
    # ========================================   ASHIKH V U (START) ======================================================

    path('item_create', views.item_create, name='item_create'),
    path('items_list/<int:pk>', views.items_list, name='items_list'),
    path('item_create_new', views.item_create_new, name='item_create_new'),
    path('item_delete/<int:pk>', views.item_delete, name='item_delete'),
    path('item_view_or_edit/<int:pk>', views.item_view_or_edit, name='item_view_or_edit'),
    path('item_unit_create', views.item_unit_create, name='item_unit_create'),
    path('item_update/<int:pk>', views.item_update, name='item_update'),
    path('item_search_filter', views.item_search_filter, name='item_search_filter'),
    path('item_get_detail/<int:pk>', views.item_get_detail, name='item_get_detail'),
    path('item_get_details_for_modal_target/<int:pk>', views.item_get_details_for_modal_target, name='item_get_details_for_modal_target'),
    path('ajust_quantity/<int:pk>', views.ajust_quantity, name='ajust_quantity'),
    path('transaction_delete/<int:pk>', views.transaction_delete, name='transaction_delete'),
    path('item_transaction_view_or_edit/<int:pk>/<int:tran>', views.item_transaction_view_or_edit, name='item_transaction_view_or_edit'),
    path('update_adjusted_transaction/<int:pk>/<int:tran>', views.update_adjusted_transaction, name='update_adjusted_transaction'),
    path('item_delete_open_stk/<int:pk>',views.item_delete_open_stk,name='item_delete_open_stk'),
    
    # ========================================   ASHIKH V U (END) ======================================================
    
    #______________Parties(new)_________________Antony Tom___________________________

    path('add_parties', views.add_parties, name='add_parties'),
    path('save_parties', views.save_parties, name='save_parties'),
    path('view_parties', views.view_parties, name='view_parties'),
    path('view_party/<int:id>', views.view_party, name='view_party'),
    path('edit_party/<int:id>', views.edit_party, name='edit_party'),
    path('edit_saveparty/<int:id>', views.edit_saveparty, name='edit_saveparty'),
    path('deleteparty/<int:id>', views.deleteparty, name='deleteparty'),
    #End

    #******************************************   ASHIKH V U (start) ****************************************************

    path('bank_create',views.bank_create,name='bank_create'),
    path('banks_list/<int:pk>',views.banks_list,name='banks_list'),
    path('get_bank_to_bank',views.get_bank_to_bank,name='get_bank_to_bank'),
    path('get_bank_to_cash',views.get_bank_to_cash,name='get_bank_to_cash'),
    path('get_cash_to_bank',views.get_cash_to_bank,name='get_cash_to_bank'),
    path('get_adjust_bank_balance',views.get_adjust_bank_balance,name='get_adjust_bank_balance'),
    path('bank_create_new',views.bank_create_new,name='bank_create_new'),
    path('bank_delete/<int:pk>',views.bank_delete,name='bank_delete'),
    path('account_num_check',views.account_num_check,name='account_num_check'),
    path('account_num_check_for_edit/<int:pk>',views.account_num_check_for_edit,name='account_num_check_for_edit'),
    path('bank_ifsc_check',views.bank_ifsc_check,name='bank_ifsc_check'),
    path('bank_view_or_edit/<int:pk>',views.bank_view_or_edit,name='bank_view_or_edit'),
    path('bank_update/<int:pk>',views.bank_update,name='bank_update'),
    path('bank_to_bank_transaction_create',views.bank_to_bank_transaction_create,name='bank_to_bank_transaction_create'),
    path('bank_to_cash_transaction_create',views.bank_to_cash_transaction_create,name='bank_to_cash_transaction_create'),
    path('cash_to_bank_transaction_create',views.cash_to_bank_transaction_create,name='cash_to_bank_transaction_create'),
    path('get_adjust_bank_balance_create',views.get_adjust_bank_balance_create,name='get_adjust_bank_balance_create'),
    path('delete_bank_open_balance/<int:pk>',views.delete_bank_open_balance,name='delete_bank_open_balance'),
    path('delete_bank_transaction/<int:pk>',views.delete_bank_transaction,name='delete_bank_transaction'),
    path('view_or_edit_bank_transaction/<int:pk>',views.view_or_edit_bank_transaction,name='view_or_edit_bank_transaction'),
    path('update_bank_transaction/<int:pk>',views.update_bank_transaction,name='update_bank_transaction'),

    #******************************************   ASHIKH V U (start) ****************************************************

    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)