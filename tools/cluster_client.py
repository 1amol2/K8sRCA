from kubernetes import client, config


def get_kubernetes_client():

    config.load_kube_config()

    core_v1 = client.CoreV1Api()

    return core_v1


if __name__ == "__main__":
    v1 = get_kubernetes_client()

    nodes = v1.list_node()

    print("\nConnected to Kubernetes!")
    print(f"Total nodes: {len(nodes.items)}")

    for node in nodes.items:
        ready_condition = next(
            (
                condition
                for condition in (node.status.conditions or [])
                if condition.type == "Ready"
            ),
            None,
        )

        ready_status = ready_condition.status if ready_condition else "Unknown"

        print(f"Node: {node.metadata.name}")
        print(f"Ready: {ready_status}")