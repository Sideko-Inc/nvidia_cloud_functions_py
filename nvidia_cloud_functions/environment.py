import enum


class Environment(enum.Enum):
    PRODUCTION = "https://api.nvcf.nvidia.com"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/nvidia-cloud-functions/0.1.0"
