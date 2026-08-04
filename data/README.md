# Dataset setup

Raw images are not included in this repository. Download them from the original
Mendeley Data records and follow each record's CC BY 4.0 attribution terms.

## Sources

1. **Neem — AI-MedLeafX: A Large-Scale Computer Vision Dataset for Medicinal
   Plant Diagnosis**, version 1. DOI: `10.17632/zz7r5y4dc6.1`.
   Download: https://data.mendeley.com/datasets/zz7r5y4dc6/1
2. **Tulsi — Medicinal Plant Leaf Disease Dataset**, version 1. DOI:
   `10.17632/ncg7kk3gwx.1`.
   Download: https://data.mendeley.com/datasets/ncg7kk3gwx/1
3. **Jujube — Jujube Leaf Disease and Health Image Dataset: Anthracnose,
   Powdery Mildew, Insect Damage, Yellowing, and Healthy Classes**, version 4.
   The official v4 page contains **1,260 images**. DOI:
   `10.17632/yxmf3cd865.4`.
   Download: https://data.mendeley.com/datasets/yxmf3cd865/4

## Expected local layout

Only class folders referenced by the public manifests are required:

```text
data/
├─ neem/
│  ├─ Healthy Leaf/
│  ├─ Powdery Mildew/
│  ├─ Shot Hole Leaf/
│  └─ Yellow Leaf/
├─ tulsi/
│  ├─ Tulsi_Downy_Mildew/
│  ├─ Tulsi_Healthy/
│  ├─ Tulsi_Web_Blight/
│  └─ Tulsi_Yellow_Spot/
└─ jujube/
   ├─ Anthracnose/
   ├─ Healthy/
   ├─ Insect Damage/
   ├─ Powdery Mildew/
   └─ Yellow Leaf/
```

If the downloaded archive has additional wrapper directories, either move the
class folders into the layout above or pass the actual dataset directory to
`--data-root`.

## Integrity and experiment subsets

Files in `splits/<dataset>/` use `relative_path` and `image_sha256`; they do not
contain machine-specific absolute paths. The Mendeley page total describes the
downloaded source version, while `universe_manifest.csv` is the authoritative
list of images used by the released experiment protocol.

To verify one local image in PowerShell:

```powershell
Get-FileHash "data/neem/Healthy Leaf/<filename>.jpg" -Algorithm SHA256
```

Do not commit the downloaded images. The root `.gitignore` excludes common image
formats under `data/` and typical archive files.
