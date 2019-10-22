from multiprocessing import Process

from rest_api import start_healthcheck
from worker.emulate_worker import EmulateUserLiveWorker

if __name__ == "__main__":
    emulate_live_worker = EmulateUserLiveWorker()
    healthcheck_process = Process(target=start_healthcheck)
    healthcheck_process.start()
    matcher_process = Process(target=emulate_live_worker.start_async)
    matcher_process.start()
    healthcheck_process.join()
    matcher_process.join()
