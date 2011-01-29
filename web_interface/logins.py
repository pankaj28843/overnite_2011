from django.contrib.auth.models import User
import datetime
now = datetime.datetime.now
def in_users(minutes, ):
    delta = datetime.timedelta(minutes=minutes)
    users = User.objects.filter(last_login__gte=now()-delta).order_by('last_login')
    list_users = ''    
    for user in users:
        list_users += user.first_name+'; '
    print list_users
    print 'Users logged in in last %d minutes: %d' %(minutes, users.count())        
