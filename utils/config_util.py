import os
import configparser
import logging
from utils.env_util import get_app_loc

__author__ = 'zzh'

# 全局变量
gblCfp = configparser.ConfigParser()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CFGTYPE = None
CASELEVEL = None


# 获取配置类型
def get_cfg_type_path():
    filepath = get_app_loc() + 'config/cfgtype.ini'
    logger.info(filepath)
    return filepath


# 获取配置目录
def get_cfg_type():

    if CFGTYPE is None:
        filepath = get_cfg_type_path()
        cfgtype = None

        try:
            gblCfp.read(filepath)
            cfgtype = gblCfp.get('cfg', "type")
        except Exception as e:
            logger.error(e)

        if cfgtype is None or cfgtype == "None":
            cfgtype = "development"

        return cfgtype
    else:
        return CFGTYPE


def set_cfg_type(env='test'):
    filepath = get_cfg_type_path()
    gblCfp.read(filepath)
    cfgtype = gblCfp.set('cfg', "type", env)
    gblCfp.write(open(filepath, "w"))
    return cfgtype


def read_db_cfg(cfgfile, db):
    """读取数据配置数据"""
    cf = configparser.ConfigParser()
    cf.read(cfgfile)
    dbcfg = dict()
    dbcfg['host'] = cf.get(db, "hostname")
    dbcfg['user'] = cf.get(db, "username")
    dbcfg['pass'] = cf.get(db, "password")
    dbcfg['db'] = cf.get(db, "database")
    return dbcfg


if __name__ == "__main__":
    pass
