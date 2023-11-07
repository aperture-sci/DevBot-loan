# loan = SERVICE1
SERVICE1_COMMIT_MSGS = [
    "Fix issue with loan service failing to start on Kubernetes cluster",
    "Add error handling for loan service API requests",
    "Update loan service documentation with latest usage instructions",
    "Refactor loan service code for improved performance",
    "Fix bug in loan service causing data inconsistency in database",
    "Add support for custom logging configurations in loan service",
    "Implement API versioning in loan service for backward compatibility",
    "Update dependencies in loan service to latest versions",
    "Improve logging output in loan service for better debugging",
    "Fix security vulnerability in loan service's authentication logic",
    "Add unit tests for loan service to improve test coverage",
    "Refactor loan service's database queries for better efficiency",
    "Improve error handling for database connections in loan service",
    "Add support for Kubernetes Pod scaling in loan service deployment",
    "Fix issue with loan service's message processing logic",
    "Update loan service's Dockerfile for better containerization",
    "Add support for custom log formats in loan service",
    "Refactor loan service's configuration management for better scalability",
    "Fix bug in loan service's message validation logic",
]

# interest = SERVICE2
SERVICE2_COMMIT_MSGS = [
    "Fix issue with interest service failing to authenticate with external API",
    "Add error handling for interest service API requests",
    "Update interest service documentation with latest usage instructions",
    "Refactor interest service code for improved performance",
    "Fix bug in interest service causing incorrect data processing",
    "Add support for custom configurations in interest service",
    "Implement API versioning in interest service for backward compatibility",
    "Update dependencies in interest service to latest versions",
    "Improve logging output in interest service for better debugging",
    "Fix security vulnerability in interest service's authentication logic",
    "Add unit tests for interest service to improve test coverage",
    "Refactor interest service's database queries for better efficiency",
    "Improve error handling for external API connections in interest service",
    "Add support for Kubernetes Pod scaling in interest service deployment",
    "Fix issue with interest service's processing logic",
    "Update interest service's Dockerfile for better containerization",
    "Add support for custom log formats in interest service",
    "Refactor interest service's configuration management for better scalability",
    "Fix bug in interest service's validation logic",
]

# accounts = SERVICE3
SERVICE3_COMMIT_MSGS = [
    "Fix issue with accounts service failing to authenticate with external API",
    "Add error handling for accounts service API requests",
    "Update accounts service documentation with latest usage instructions",
    "Refactor accounts service code for improved performance",
    "Fix bug in accounts service causing incorrect data processing",
    "Add support for custom configurations in accounts service",
    "Implement API versioning in accounts service for backward compatibility",
    "Update dependencies in accounts service to latest versions",
    "Improve logging output in accounts service for better debugging",
    "Fix security vulnerability in accounts service's authentication logic",
    "Add unit tests for accounts service to improve test coverage",
    "Refactor accounts service's database queries for better efficiency",
    "Improve error handling for external API connections in accounts service",
    "Add support for Kubernetes Pod scaling in accounts service deployment",
    "Fix issue with accounts service's processing logic",
    "Update accounts service's Dockerfile for better containerization",
    "Add support for custom log formats in accounts service",
    "Refactor accounts service's configuration management for better scalability",
    "Fix bug in accounts service's validation logic",
]

# orders = SERVICE4
SERVICE4_COMMIT_MSGS = [
    "Fix issue with orders service failing to authenticate with external API",
    "Add error handling for orders service API requests",
    "Update orders service documentation with latest usage instructions",
    "Refactor orders service code for improved performance",
    "Fix bug in orders service causing incorrect data processing",
    "Add support for custom configurations in orders service",
    "Implement API versioning in orders service for backward compatibility",
    "Update dependencies in orders service to latest versions",
    "Improve logging output in orders service for better debugging",
    "Fix security vulnerability in orders service's authentication logic",
    "Add unit tests for orders service to improve test coverage",
    "Refactor orders service's database queries for better efficiency",
    "Improve error handling for external API connections in orders service",
    "Add support for Kubernetes Pod scaling in orders service deployment",
    "Fix issue with orders service's processing logic",
    "Update orders service's Dockerfile for better containerization",
    "Add support for custom log formats in orders service",
    "Refactor orders service's configuration management for better scalability",
    "Fix bug in orders service's validation logic",
]

# membership = SERVICE5
SERVICE5_COMMIT_MSGS = [
    "Fix issue with membership service failing to authenticate with external API",
    "Add error handling for membership service API requests",
    "Update membership service documentation with latest usage instructions",
    "Refactor membership service code for improved performance",
    "Fix bug in membership service causing incorrect data processing",
    "Add support for custom configurations in membership service",
    "Implement API versioning in membership service for backward compatibility",
    "Update dependencies in membership service to latest versions",
    "Improve logging output in membership service for better debugging",
    "Fix security vulnerability in membership service's authentication logic",
    "Add unit tests for membership service to improve test coverage",
    "Refactor membership service's database queries for better efficiency",
    "Improve error handling for external API connections in membership service",
    "Add support for Kubernetes Pod scaling in membership service deployment",
    "Fix issue with membership service's processing logic",
    "Update membership service's Dockerfile for better containerization",
    "Add support for custom log formats in membership service",
    "Refactor membership service's configuration management for better scalability",
    "Fix bug in membership service's validation logic",
]

SERVICE_COMMIT_MSGS = [
    "Fix bug in function xyz",
    "Refactor code for improved readability",
    "Add feature ABC",
    "Update documentation",
    "Optimize performance",
    "Merge branch feature/123",
    "Fix typo in file XYZ",
    "Implement new functionality",
    "Update dependencies",
    "Add test cases",
    "Fix formatting issues",
    "Remove unused code",
    "Fix security vulnerability",
    "Update error handling",
    "Revert previous commit",
    "Add logging statements",
    "Refactor variable naming",
    "Update UI layout",
    "Fix edge case in function ABC",
    "Improve error messages"
]

CODE_LINES_LIST = ['from kubernetes import client, config',
                   'config.load_kube_config()',
                   'v1 = client.CoreV1Api()',
                   'ret = v1.list_pod_for_all_namespaces(watch=False)',
                   'print("Total pods: %d" % len(ret.items))',
                   'ret = v1.list_node(watch=False)',
                   'print("Total nodes: %d" % len(ret.items))',
                   'v1_beta = client.ExtensionsV1beta1Api()',
                   'ret = v1_beta.list_deployment_for_all_namespaces(watch=False)',
                   'print("Total deployments: %d" % len(ret.items))',
                   'ret = v1_beta.list_ingress_for_all_namespaces(watch=False)',
                   'print("Total ingresses: %d" % len(ret.items))',
                   'ret = v1_beta.list_replica_set_for_all_namespaces(watch=False)',
                   'print("Total replica sets: %d" % len(ret.items))',
                   'v1_apps = client.AppsV1Api()',
                   'ret = v1_apps.list_stateful_set_for_all_namespaces(watch=False)',
                   'print("Total stateful sets: %d" % len(ret.items))',
                   'ret = v1_apps.list_daemon_set_for_all_namespaces(watch=False)',
                   'print("Total daemon sets: %d" % len(ret.items))']

PULL_REQUESTS_TOPICS = [
    "Fix issue with authentication flow",
    "Add support for multi-factor authentication",
    "Update documentation with new usage instructions",
    "Refactor code to improve performance",
    "Implement feature to support file uploads",
    "Fix bug causing incorrect calculation of prices",
    "Add unit tests for critical functionality",
    "Implement error handling for edge cases",
    "Add support for internationalization and localization",
    "Improve logging and error reporting",
    "Refactor database schema to optimize queries",
    "Implement caching to improve response times",
    "Fix UI rendering issue on mobile devices",
    "Add support for OAuth authentication",
    "Implement pagination for large datasets",
    "Add support for custom themes",
    "Improve error messaging for user-friendly feedback",
    "Refactor code to follow coding style guidelines",
    "Fix cross-site scripting (XSS) vulnerability",
    "Implement user authentication via social media accounts",
]
BRANCHES_NAMES_PREFIXES = [
    "feature/",
    "bugfix/",
    "hotfix/",
    "develop/",
    "refactor/",
    "chore/",
    "test/",
    "style/",
    "improvement/",
    "task/",
    "experimental/",
    "revert/",
    "support/",
    "temp/",
    "review/",
    "fix/",
    "vendor/",
    "maintenance/",
    "release-notes/",
    "demo/",
    "design/",
    "analysis/",
    "backlog/"
]

BRANCHES_NAMES = [
    "Containerization",
    "Microservices-refine",
    "K8s-deployment-opt",
    "IaC-refactoring",
    "CI-streamlining",
    "DevOps-automation",
    "Scalability-refactor",
    "Distributed-tracing",
    "Service-mesh-refactor",
    "Cloud-native-migra",
    "Immutable-infra",
    "Config-mgmt-refine",
    "Monitoring-refine",
    "Blue-green-deploy",
    "GitOps-adoption",
    "CICD-pipeline-opt",
    "Deployment-refactor",
    "Performance-refactor",
    "Error-handling-ref",
    "Security-refactor",
    "Logging-observability",
    "Secrets-mgmt-ref",
    "Auto-scaling-ref",
    "Infra-cost-optimize",
    "Backup-recovery-opt",
    "Compliance-audit",
    "Release-mgmt-opt",
    "Load-balancing-ref",
    "Pod-scheduling-error",
    "Svc-discovery-issue",
    "Ingress-conf-bug",
    "PVC-error",
    "Container-vuln",
    "Configmap-Secrets",
    "K8s-API-error",
    "Networking-issue",
    "Resource-quota",
    "RBAC-permission",
    "Pod-crash-loop",
    "Node-drain-failure",
    "K8s-upgrade-issue",
    "Pod-lifecycle-bug",
    "CronJob-scheduling",
    "DNS-resolution",
    "Svc-mesh-conf-bug",
    "K8s-operators-error",
    "CRD-issue",
    "Statefulset-bug",
    "K8s-volume-bug",
    "Pod-networking-bug",
    "Ingress-ctrl-bug",
    "K8s-namespace-error",
    "Sec-context-bug",
    "APIserver-conf-issue",
    "Pod-scaling-error",
    "K8s-autoscaling",
    "Admission-ctrl-error",
]

JIRA_TICKETS = [
    {
        "summary": "BUG: Pod CrashLoopBackOff error after deploying k8s application",
        "description": "The k8s application's pods are crashing with a 'CrashLoopBackOff' error in the logs, indicating a recurring issue. Investigation needed to identify and resolve the root cause of the problem.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for rolling updates in k8s application",
        "description": "Currently, the k8s application does not support rolling updates, resulting in downtime during deployments. Requesting to add support for rolling updates to ensure zero-downtime deployments and better availability.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Ingress not routing traffic to k8s application",
        "description": "Ingress configuration is not routing incoming traffic to the k8s application's services, resulting in 404 errors. Investigation needed to identify the misconfiguration and fix it to enable proper traffic routing.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement horizontal pod autoscaling for k8s application",
        "description": "Requesting to implement horizontal pod autoscaling for the k8s application to automatically scale up or down based on resource utilization and traffic patterns, ensuring optimal performance and resource utilization.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Container image pull failure in k8s application",
        "description": "The k8s application's pods are failing to pull container images from the container registry, resulting in failed deployments. Investigation needed to resolve the issue and ensure successful image pulling during deployments.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add logging and monitoring to k8s application",
        "description": "Requesting to add proper logging and monitoring to the k8s application to enable better observability and troubleshooting. This includes setting up centralized logging and monitoring solutions like ELK stack or Prometheus/Grafana.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: CrashLoopBackOff in init container of k8s application",
        "description": "The init containers in the k8s application's pods are encountering 'CrashLoopBackOff' error, preventing the pods from starting properly. Investigation needed to identify and fix the issue in the init container configuration.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement rolling restarts for k8s application",
        "description": "Requesting to implement rolling restarts for the k8s application to gracefully restart pods one by one, avoiding downtime and ensuring uninterrupted service availability during restarts.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: Incorrect resource limits set in k8s application",
        "description": "The resource limits set for the k8s application's pods are incorrect, resulting in resource exhaustion and performance issues. Investigation needed to review and adjust the resource limits for optimal performance and stability.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for canary deployments in k8s application",
        "description": "Requesting to add support for canary deployments in the k8s application to enable gradual rollouts and rollbacks, minimizing the impact of faulty deployments and ensuring better resilience and fault tolerance.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: accounts service returning 500 error on login",
        "description": "The accounts service is returning a 500 error when users attempt to log in, resulting in login failures. Investigation needed to identify and fix the issue to ensure successful user authentication and login functionality.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for multi-factor authentication in accounts service",
        "description": "Requesting to add support for multi-factor authentication (MFA) in the accounts service to provide an additional layer of security for user authentication. This will help in mitigating the risk of unauthorized access to the service and user accounts.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: accounts service not rendering UI components properly",
        "description": "The accounts service is not rendering UI components properly, resulting in broken or misaligned user interface elements. Investigation needed to identify and fix the issue to ensure proper rendering of UI components for improved user experience.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement API rate limiting in accounts service",
        "description": "Requesting to implement API rate limiting in the accounts service to prevent abuse and protect against potential DDoS attacks. This will help in ensuring fair usage of the service and maintaining service availability and performance.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: accounts service experiencing high memory utilization",
        "description": "The accounts service is experiencing high memory utilization, resulting in performance degradation and increased response times. Investigation needed to identify the memory-intensive processes and optimize resource utilization for improved performance and responsiveness.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for internationalization (i18n) in accounts service",
        "description": "Requesting to add support for internationalization (i18n) in the accounts service to enable localization of user interface components for different languages and regions. This will help in providing a better user experience for users from diverse language backgrounds.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: accounts service failing to handle concurrent user requests",
        "description": "The accounts service is failing to handle concurrent user requests, resulting in degraded performance and increased response times. Investigation needed to identify and fix the issue with request handling to ensure efficient handling of concurrent user requests.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Implement container image scanning in accounts service",
        "description": "Requesting to implement container image scanning in the accounts service to ensure the security and integrity of container images used in the service. This will help in identifying and addressing potential security vulnerabilities and ensuring secure container deployments.",
        "issuetype": "Idea"
    },
    {
        "summary": "BUG: accounts service not persisting user preferences properly",
        "description": "The accounts service is not persisting user preferences properly, resulting in loss of user settings and configurations. Investigation needed to identify and fix the issue with user preference storage to ensure reliable persistence of user preferences across sessions.",
        "issuetype": "Bug"
    },
    {
        "summary": "Enhancement Request: Add support for role-based access control (RBAC) in accounts service",
        "description": "Requesting to add support for role-based access control (RBAC) in the accounts service to provide granular control over user permissions and access to different functionalities and resources.",
        "issuetype": "Idea"
    }
]

PYTHON_COMMANDS = [
    "print('Hello, world!')",
    "input('Enter your name: ')",
    "len('Hello')",
    "range(1, 10)",
    "list('Python')",
    "tuple((1, 2, 3))",
    "set([1, 2, 3, 4])",
    "dict({'a': 1, 'b': 2})",
    "sorted([4, 2, 1, 3])",
    "str.upper('hello')",
    "int('42')",
    "float(3.14)",
    "bool(0)",
    "abs(-5)",
    "sum([1, 2, 3, 4])",
    "max([1, 2, 3, 4])",
    "min([1, 2, 3, 4])",
    "pow(2, 3)",
    "round(3.14159, 2)",
    "hex(255)",
    "bin(255)",
    "oct(255)",
    "ord('A')",
    "chr(65)",
    "type('hello')",
    "isinstance(42, int)",
    "dir('hello')",
    "help(print)"
]

PULL_REQUESTS_TITLES = [
    "Add Prometheus monitoring support for Loans microservices",
    "Refactor Loans loan microservice for better performance",
    "Implement authentication and authorization in Loans interest microservice",
    "Update accounts frontend for Loans with new UI design",
    "Integrate logging framework into Loans loan microservice",
    "Improve error handling in Loans interest microservice",
    "Add unit tests for Loans accounts frontend",
    "Optimize Loans loan microservice for scalability",
    "Implement CI/CD pipeline for Loans microservices",
    "Update dependencies for Loans loan, interest, and accounts",
    "Implement caching mechanism in Loans interest microservice",
    "Refactor Loans accounts for improved code maintainability",
    "Add API documentation for Loans loan, interest, and accounts",
    "Implement graceful shutdown handling in Loans microservices",
    "Update logging configuration in Loans loan microservice",
    "Enhance error handling in Loans accounts frontend",
    "Implement circuit breaker pattern in Loans interest microservice",
    "Add support for Kubernetes namespaces in Loans microservices",
    "Refactor Loans loan microservice to use async I/O",
    "Update UI components in Loans accounts for better usability",
    "Implement load balancing in Loans interest microservice",
    "Add Prometheus metrics endpoint to Loans microservices",
    "Implement API versioning in Loans loan, interest, and accounts",
    "Enhance security measures in Loans microservices",
    "Update logging format in Loans loan microservice",
    "Implement rate limiting in Loans interest microservice",
    "Refactor Loans accounts for improved performance",
    "Add custom exception handling in Loans microservices",
    "Update documentation for Loans loan, interest, and accounts",
    "Implement distributed tracing in Loans microservices"
]
