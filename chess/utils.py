def static_init(cls, init_f='static_init'):
    f = getattr(cls, init_f, None)
    f()
    return cls
