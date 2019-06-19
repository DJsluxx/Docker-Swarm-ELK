from ELK import elk_deploy


def start_deploy():
    elk = elk_deploy.ClusterDeploy
    elk.deploy_cluster()


if __name__ == '__main__':
    start_deploy()
