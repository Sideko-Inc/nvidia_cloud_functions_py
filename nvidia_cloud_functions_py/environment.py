import enum


class Environment(enum.Enum):
    ENVIRONMENT = "https://api.nvcf.nvidia.com"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/nvidia-cloud-functions/0.1.0"
