from wingnut import Wingnut
import yaml

if __name__ == "__main__":
    with open("/etc/wingnut/wingnut.yaml", "r") as yamlfile:
        config = yaml.safe_load(yamlfile)
    wingnut = Wingnut(config)
    wingnut.start_ui()
    wingnut.get_diagnostics()
