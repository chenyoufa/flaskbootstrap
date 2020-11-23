from flask import session,redirect

import functools

#装饰器的方法
def is_login(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        user = session.get('logged_in')
        if not user:
            return redirect('login')
        return func(*args,**kwargs)
    return inner

