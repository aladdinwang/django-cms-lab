from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class NewsApp( CMSApp ):
    name = "News App"
    urls = ["demo.urls"]
    
apphook_pool.register( NewsApp )
