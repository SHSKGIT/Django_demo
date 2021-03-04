"""listingllama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'users'


urlpatterns = [
               
    path("", views.dashboard, name="homepage"),
    path("start", views.start, name="start"),
    path("dashboard", views.dashboard, name="dashboard"),  
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path("new_buying", views.new_buying, name="buying"),
    path("new_buying_location", views.new_buying_location, name="buying_location"),
    path("new_selling", views.new_selling, name="selling"),
    path("new_selling_location", views.new_selling_location, name="selling_location"),
    path("my_opportunities", views.my_opportunities, name="my_opportunities"),
    path("opportunities", views.agent_opp, name="agent_opportunities"),
    path("proposals", views.agent_proposals, name="agent_proposals"),
    path("my_proposals", views.user_proposals, name="user_proposals"),
    path("new_proposals", views.agent_create_proposal, name="new_proposals"),
    path("new_proposal_buying", views.agent_proposal_buying, name="new_proposal_buying"),
    path("new_proposal_selling", views.agent_proposal_selling, name="new_proposal_selling"),
    path("posting_buying_<int:id>", views.buy_posting_view, name="buy_posting_view"),
    path("posting_selling_<int:id>", views.sell_posting_view, name="sell_posting_view"),
    path("proposal_<int:id>", views.single_proposal, name="single_proposal"),
    path("realtors", views.realtor_find, name="realtor_find"),
    path("realtors_next_<int:id>", views.realtor_find_next, name="realtor_find_next"),
    path("realtors_back", views.realtor_find_back, name="realtor_find_back"),
    path("profile", views.agent_profile, name="agent_profile"),
    path("edit/posting_buying_<int:id>", views.post_edit_buy, name="post_edit_buy"),
    path("edit/posting_selling_<int:id>", views.post_edit_sell, name="post_edit_sell"),
    path("upload_picture", views.upload_picture, name="upload_picture"),
    path("profile_edit", views.profile_edit, name="profile_edit"),
    path("posting_image_buy<int:id>", views.add_images_buy, name="add_images_buy"),
    path("posting_image_sell_<int:id>", views.add_images_sell, name="add_images_sell"),
    path("accept_proposal_<int:id>", views.accept_proposal, name="accept_proposal"),
    path("accept_proposal_agent<int:id>", views.accept_proposal_agent, name="accept_proposal_agent"),
    path("promo", views.payment_page, name="promo"),
    path("charge", views.charge, name="charge"),
    path("cancel_sub", views.cancel_sub, name="cancel_sub"),
    path("legal", views.legal, name="legal"),
               
    path("jerry/<path:client_attr>/<path:client_attr_2>", views.jerry, name="jerry_1"),
    path("jerry_2/", views.jerry_2, name="jerry_2"),
    path("jerry_3/<path:client_attr>/<path:client_attr_2>", views.jerry_3, name="jerry_3"),
    path("jerry_4/", views.jerry_4, name="jerry_4"),
    path("jerry_5/", views.jerry_5, name="jerry_5"),
]
