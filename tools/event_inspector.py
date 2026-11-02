from kubernetes import client, config


def inspect_events():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    events = v1.list_event_for_all_namespaces()

    print(f"\nTotal Events: {len(events.items)}")
    print("=" * 70)

    for event in events.items:
        print(f"Namespace: {event.metadata.namespace}")
        print(f"Reason: {event.reason}")
        print(f"Type: {event.type}")
        print(f"Message: {event.message}")
        print(f"Count: {event.count}")
        print(f"Object: {event.involved_object.name}")
        print("-" * 70)


if __name__ == "__main__":
    inspect_events()