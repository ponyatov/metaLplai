from metaL import *

####################################################### namespace /environment/
class Ns(Object):
    pass


############################################################## global namespace
glob = Ns('global')
glob << glob
glob >> glob
