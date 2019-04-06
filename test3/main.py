from Scheduler import *

if __name__ == "__main__":

    input = [{'priority': 5, 'start_time': 10, 'duration': 20, 'type': 'audio', 'recorder': 'rec1'},
		 {'priority': 3, 'start_time': 15, 'duration': 10, 'type': 'video', 'recorder': 'rec2'}, 
		 {'priority': 1, 'start_time': 2, 'duration': 60, 'type': 'audio', 'recorder': 'rec3'},  
		 {'priority': 6, 'start_time': 13, 'duration': 33, 'type': 'audio', 'recorder': 'rec4'}, 
		 {'priority': 2, 'start_time': 8, 'duration': 48, 'type': 'video', 'recorder': 'rec5'},
		 {'priority': 4, 'start_time': 26, 'duration': 25, 'type': 'video', 'recorder': 'rec6'}]
    
    tasks = []

    for i in input:
        tasks.append(Task(i['priority'], i['start_time'], i['duration'], i['type'], i['recorder']))
    
    sorted_tasks = GetAllTasksSorted(tasks)
    
    for task in sorted_tasks:
        print(task)

    print("Get task:")
    print(GetNextTask(sorted_tasks))
    print(GetNextTask(sorted_tasks))
    print(GetNextTask(sorted_tasks))
    print(GetNextTask(sorted_tasks))
