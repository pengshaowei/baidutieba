# -*- coding:utf-8 -*-
from superdao import superdao

class TiebaDAO(superdao):
	def __init__(self,host,db,user,password):
		superdao.__init__(host,db,user,password)
		pass
	def save(self, invitation):
		superdao.save_record(table_name='tb_baidutieba',record=invitation)
		pass