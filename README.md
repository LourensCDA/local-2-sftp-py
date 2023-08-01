# LOCAL FOLDER TO SFTP

This process syncs a local folder to an SFTP.

## virtualenv

I use pipenv as virtual enviroment.

To install in Windows:

```powershell
pip install --user pipenv
```

To install in Ubuntu:

```bash
sudo apt install pipenv
```

You may have to add the Python Scripts folder to the path when running it:

Windows:

```powershell
$env:Path =  "C:\Users\~\AppData\Roaming\Python\Python39\Scripts;$env:Path"
```

You can run pipenv using the following commands in your project folder.

Windows:

```powershell
pipenv run python main.py
```

Generate requirements for pip install from pipenv

```powershell
pipenv lock -r > requirements.txt
```

Install those requirements

```powershell
pip install -r requirements.txt
```
