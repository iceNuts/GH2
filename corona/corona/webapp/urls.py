from django.conf.urls import patterns, url




urlpatterns = patterns('',

    # DEBUG : load test data
    url(r'^test$', 'webapp.views.load_test_data.load'),
)






