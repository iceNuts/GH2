from django.conf.urls import patterns, url




urlpatterns = patterns('',

    # DEBUG : load test data
    url(r'^test$', 'webapp.views.load_test_data.load'),

    # user
    url(r'^login$', 'webapp.views.userview.user_login'),
    url(r'^user/(\w+)$', 'webapp.views.userview.user'),
    
    # pool
    url(r'^repo/popular$', 'webapp.views.poolview.popular_list'),
    url(r'^repo/user/(\w+)$', 'webapp.views.poolview.pool_list'),

    # taxonomy
    url(r'^taxonomy$', 'webapp.views.poolview.taxonomy'),
    url(r'^taxonomy/delete/(\w+)$', 'webapp.views.poolview.taxonomy'),
    url(r'^taxonomy/like$', 'webapp.views.poolview.like_taxonomy'),
    url(r'^taxonomy/publish$', 'webapp.views.poolview.publish_taxonomy'),
    url(r'^taxonomy/fork$', 'webapp.views.poolview.fork_taxonomy'),
    url(r'^taxonomy/export/(\w+)$', 'webapp.views.poolview.export_taxonomy'),
    url(r'^taxonomy/streaming$', 'webapp.views.poolview.more_data_taxonomy'),

    # attribute
    url(r'^taxonomy/attribute$', 'webapp.views.poolview.attribute'),
    url(r'^taxonomy/attribute/(\w+)$', 'webapp.views.poolview.attribute')

)






