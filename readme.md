Related link:

http://www.categories.acsl.org/wiki/index.php?title=Main_Page


SSH Key:
1. ssh-keygen -t rsa -f ~/.ssh/my_rsa_key
2. eval "$(ssh-agent -s)"
3. ssh-add -l
4. ssh-add ~/.ssh/my_rsa_key
5. ssh-add -l
6. ssh -vT git@github.com


Git Account:
1. enter the root directory of the project
2. git config user.name "YourName"
3. git config user.email "YourEmail"