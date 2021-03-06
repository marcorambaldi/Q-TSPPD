from handler.MenuHandler import MenuHandler


class Menu:

	def __init__(self, handler: MenuHandler):
		self.handler = handler

	def show(self) -> None:
		""" Shows the menu that interacts with the user

		:return: None
		"""

		choice = ''
		while choice != 'q':
			print('\n----------- Main Menù --------------')
			print('| <1> GREEDY                       |')
			print('| <2> GREEDY_BY_VALUE              |')
			print('| <3> DESTROY_AND_REPAIR           |')
			print('| <4> GREEDY_RANDOM                |')
			print('| <5> GRASP                        |')
			print('| <6> BEST_IMPROVEMENT_D_&_R       |')
			print('------------------------------------')
			choice = input('Select an option (q to exit): ')

			if choice in {'1', '2', '3', '4', '5', '6'}:
				if choice == '1':
					command = 'GREEDY'
				elif choice == '2':
					command = 'GREEDY_BY_VALUE'
				elif choice == '3':
					command = 'DESTROY_AND_REPAIR'
				elif choice == '4':
					command = 'GREEDY_RANDOM'
				elif choice == '5':
					command = 'GRASP'
				elif choice == '6':
					command = 'BEST_IMPROVEMENT_D_&_R'

				self.handler.serve(command)

			elif choice == 'q':
					break
			elif choice != 'q':
				print('Input code is wrong. Choose one action!\n')
