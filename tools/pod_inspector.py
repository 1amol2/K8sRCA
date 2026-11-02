from kubernetes import client, config


def get_kubernetes_client():
    config.load_kube_config()
    return client.CoreV1Api()


def inspect_pods():
    v1 = get_kubernetes_client()


    pods = v1.list_pod_for_all_namespaces()

    print(f"\nTotal Pods: {len(pods.items)}")
    print("-" * 60)

    for pod in pods.items:
        namespace = pod.metadata.namespace
        name = pod.metadata.name
        phase = pod.status.phase

        print(f"Pod: {name}")
        print(f"Namespace: {namespace}")
        print(f"Phase: {phase}")

        for container in pod.status.container_statuses or []:
            print(f"Container: {container.name}")
            print(f"Ready: {container.ready}")
            print(f"Restart Count: {container.restart_count}")

            if container.state.waiting:
                print(f"Waiting Reason: {container.state.waiting.reason}")

            if container.state.terminated:
                print(f"Termination Reason: {container.state.terminated.reason}")

        print("-" * 60)


if __name__ == "__main__":
    inspect_pods()