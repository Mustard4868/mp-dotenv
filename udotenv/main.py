import uos

class Dotenv:
    def __init__(
            self,
            path: str = '/',
    ):
        if '.env' in path:
            path = path.replace('.env', '')
        self.path = path
        self.envs = {}

    def load_dotenv(self) -> None:
        with open(self.path + '.env', 'r') as f:
            for line in f.readlines():
                key, value = line.strip().replace(' ', '').split('=')
                self.envs[key] = value

    def get_env(self, key: str) -> str:
        return self.envs[key]
        
env = Dotenv()
env.load_dotenv()
print(env.envs)