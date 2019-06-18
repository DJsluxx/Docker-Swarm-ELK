installing_requirements:
    @echo 'installing requirements ...'
    apt install docker
create_cluster:
    @echo 'creating cluster named elk ...'
    docker swarm init elk
set_ram_usage:
    @echo 'configuring ...'
    sysctl -w vm.max_map_count=262144
apply_docker_compose:
    @echo 'deploying elk on nodes ...'
    docker stack deploy -c docker-compose.yml elk