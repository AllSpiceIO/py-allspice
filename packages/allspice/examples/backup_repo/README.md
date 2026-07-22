# Example: Back up a repository to an archive

This example shows how to back up a repository to an archive. It is presented as both a
[script](./backup_repo.py) and a [jupiter notebook](./backup_repo.ipynb). If you're using
this as a reference, the jupyter notebook is like a guided tour. Otherwise, you can
directly use the script with:

```bash
# Backs up test/test to my_backup.tar.gz
python backup_repo.py "test/test" --output "my_backup" --format "tar.gz"

# Backs up the develop branch of test/test to my_backup.zip
python backup_repo.py "test/test" --output "my_backup" --ref "develop"
```
