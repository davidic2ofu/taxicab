import mysql.connector
from pprint import pprint

cnx = mysql.connector.connect(user='taxicab_user', password='taxi',
                              host='127.0.0.1',
                              database='taxicab_system')


def execute_query(query):
	cursor.execute(query)
	result = cursor.fetchall()
	return result


if __name__ == '__main__':
	cursor = cnx.cursor()
	print('\nTaxicab System DB:\n{}\n'.format(18 * '='))
	print('Tables in DB:')
	pprint(execute_query('SHOW TABLES'))
	while True:
		try:
			query = input('\nEnter your query (or "exit"): ')
			if query == 'exit':
				break
			pprint(execute_query(query))
		except Exception as e:
			print('Invalid query: {}'.format(e))
	cnx.close()
