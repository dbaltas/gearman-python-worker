import gearman
import simplejson

gm_worker = gearman.GearmanWorker(['localhost:4730'])

def task_listener_reverse(gearman_worker, gearman_job):
	data = simplejson.loads(gearman_job.data)

	return 'hi {0} from python worker'.format(data['name'])

# gm_worker.set_client_id is optional
gm_worker.set_client_id('your_worker_client_id_name')
gm_worker.register_task('python-hi', task_listener_reverse)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()