import mysql.connector
from tabulate import tabulate

DB_PARAMS = {
	'user': 'taxicab_user',
	'password': 'taxi',
	'host': '127.0.0.1',
	'database': 'taxicab_system',
}


def execute_query(query):
	cursor.execute(query)
	fields = [i[0] for i in cursor.description]
	rows = cursor.fetchall()
	print(tabulate(rows, headers=fields))


if __name__ == '__main__':
	cnx = mysql.connector.connect(**DB_PARAMS)
	cursor = cnx.cursor()
	print('\nTaxicab System DB:\n{}\n'.format(18 * '='))
	execute_query('SHOW TABLES')
	while True:
		try:
			query = input('\nEnter your query (or "exit"): ')
			if query == 'exit':
				break
			execute_query(query)
		except Exception as e:
			print('Invalid query: {}'.format(e))
	cnx.close()
