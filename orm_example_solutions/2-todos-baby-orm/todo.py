from orm_class import Model
import sys

class Todo(Model):
	def list_(self, args):
		for i in self.all():
			print(i.__dict__)

	def add(self, args):
		content = ' '.join(args)
		return self.create(thing=content)

	def delete(self, args):
		for i in args:
			super().delete(i)

	def complete(self, args):
		for i in args:
			finished_todo = self.get(id=i)
			finished_todo.is_completed = 1
			finished_todo.save()

if __name__ == "__main__":
	todo = Todo()
	command_dict = { 'list': todo.list_, 'add': todo.add,
			'delete': todo.delete, 'complete': todo.complete, }
	command = sys.argv[1]
	args = sys.argv[2:]
	if command in command_dict.keys():
		command_dict[command](args)
	else:
		print("invalid input jerkface")
