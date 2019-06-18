import os
import pymake

import configuration


class ClusterDeploy:
    def __init__(self):
        manager_token = None
        worker_token = None

    def deploy_cluster(self):
        pymake.main('install_requirments')