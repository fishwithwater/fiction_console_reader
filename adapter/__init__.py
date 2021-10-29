from adapter.xbiquge_adapter import XbiqugeAdapter
from config import app_config


adapter_cls_list = [XbiqugeAdapter]

__adapter = None

def get_adapter():
    global __adapter
    if __adapter is None:
        for adapter_cls in adapter_cls_list:
            if (adapter_cls.supports(app_config.source_website)):
                __adapter = adapter_cls()
    return __adapter