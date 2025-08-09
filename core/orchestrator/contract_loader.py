import json
from pathlib import Path
import requests

class ContractLoader:
    def __init__(self, source="local", base_path="./schemas"):
        self.source = source
        self.base_path = Path(base_path)
        self.cache = {}

    def load(self, service_name):
        if self.source == "local":
            path = self.base_path / f"{service_name}_schema.json"
            with path.open() as f:
                schema = json.load(f)
            self.cache[service_name] = schema
            return schema
        elif self.source == "http":
            url = f"http://config-service/{service_name}/schema"
            resp = requests.get(url)
            resp.raise_for_status()
            schema = resp.json()
            self.cache[service_name] = schema
            return schema

    def get_cached(self, service_name):
        return self.cache.get(service_name)
