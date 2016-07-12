# -*- coding:utf-8 -*-
import MySQLdb
import traceback

class superdao(object):
	def __init__(self,host,db,user,password):
		self.host = host
		self.db = db
		self.user = user
		self.password = password
		pass

	def save_record(self,table_name,record):
		db = MySQLdb.connect(self.host, self.user, self.password, self.db, charset='utf8')
		cursor = db
		try:
			placeholders = ', '.join(['%s'] * len(record))
			columns = ', '.join(record.keys())
			sql = "insert into %s( %s ) values ( %s )" % (table_name, columns, placeholders)
			cursor.execute(sql, record.values())
		except Exception,e:
			print e
		db.commit()
		cursor.close()
		db.close()
		pass

	def save_records(self, table_name, records):
		db = MySQLdb.connect(self.host, self.user, self.password, self.db, charset='utf8')
		cursor = db.cursor()
		for record in records:
			placeholders = ', '.join(['%s'] * len(record))
			columns = ', '.join(record.keys())
			sql = "insert into %s( %s ) values ( %s )" % (table_name, columns, placeholders)
			print sql
			try:
				cursor.execute(sql, record.values())
			except:
				#traceback.print_exc()
				#break
				print '----------------------------------------------------------'
		db.commit()
		cursor.close()
		db.close()