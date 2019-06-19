import pymake
import paramiko

from ELK import configuration


class ClusterDeploy:
    def __init__(self):
        self.manager_token = None
        self.worker_token = None
        self.connection = None

    def deploy_cluster(self):
        pymake.main('install_requirments')
        pymake.main('create_cluster')
        pymake.main('set_ram_usage')
        self.set_manager_and_workers(manager=configuration.MANAGER)
        pymake.main('apply_docker_compose')

    def set_manager_and_workers(self, manager):
        self.manager_token = self._get_manager_token(manager)
        self.worker_token = self._get_worker_token(manager)
        self._join_manager_to_cluster()
        self._join_workers_to_cluster()

    def _get_worker_token(self, manager):
        token = self._run_command(manager, 'docker swarm join-token worker -q')
        return token

    def _get_manager_token(self, manager):
        token = self._run_command(manager, 'docker swarm join-token manager -q')
        return token

    def _run_command(self, node, command):
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(node, configuration.USERNAME, configuration.PASSWORD)
        stdin, stdout, stderr = self.connection.exec_command(command)
        return stdout.read()

    def _join_manager_to_cluster(self):
        self._run_command(configuration.MANAGER, 'docker swarm join --token {}'.format(self.manager_token))

    def _join_workers_to_cluster(self):
        self._run_command(configuration.WORKER1, 'docker swarm join --token {}'.format(self.worker_token))
        self._run_command(configuration.WORKER2, 'docker swarm join --token {}'.format(self.worker_token))
        self._run_command(configuration.WORKER3, 'docker swarm join --token {}'.format(self.worker_token))
