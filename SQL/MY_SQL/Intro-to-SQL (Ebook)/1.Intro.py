# ==============================================================================
"""
Install MySQL on Mac:
    brew install mysql
    brew services start mysql
    mysql_secure_installation 
    brew services stop mysql

Accessing MySQL via CLI:
    mysql -u root -p

Configuring .my.cnf: 
(By configuring the ~/.my.cnf file in your user's home directory, 
MySQL would allow you to log in without prompting you for a password.)
    
    touch ~/.my.cnf
    chmod 0600 ~/.my.cnf
    nano ~/.my.cnf
    
    Add below details:
        [client]
        user=YOUR_MYSQL_USERNAME
        password=YOUR_MYSQL_PASSWORD

To check all of your open SQL connections:
    mysqladmin proc

There are other GUI clients for MySQL, such as:
    MySQL Workbench
    Sequel Pro
    TablePlus etc.
"""