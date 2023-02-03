import yaml
import json
from pathlib import Path
content_dirs = ["_papers","_tasks","_datasets","_methods","_foundations"]
for content_dir in content_dirs:
    print(content_dir)
    content_dir = Path(content_dir)
    all_content= []
    for file in content_dir.glob("*.md"):
        content = file.read_text()
        yaml_content = content.split("---")[1]
        yaml_content = yaml.load(yaml_content, Loader=yaml.SafeLoader)
        all_content.append(yaml_content)
    out_name = content_dir.stem.replace("_","")
    print(out_name)
    with open(f"./data/{out_name}.json", "w") as f:
        json.dump(all_content, f, indent=4)