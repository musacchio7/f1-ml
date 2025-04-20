from kagglehub import dataset_download
from pathlib import Path
import shutil

def download_f1_dataset():
    kaggle_id = "rohanrao/formula-1-world-championship-1950-2020"
    folder_name = kaggle_id.replace("/", "_")  # rohanrao_formula-1-world-championship-1950-2020
    raw_dir = Path(f"data/raw/{folder_name}")

    if raw_dir.exists() and any(raw_dir.iterdir()):
        print(f"[✔] Dataset already present in {raw_dir}")
        return

    print("[⏳] Downloading dataset from Kaggle...")
    path = Path(dataset_download(kaggle_id))

    raw_dir.mkdir(parents=True, exist_ok=True)

    for item in path.iterdir():
        shutil.copy(item, raw_dir / item.name)

    print(f"[✔] Dataset copied to {raw_dir}")

if __name__ == "__main__":
    download_f1_dataset()
