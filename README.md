This project helps the user to build an internal reporting tool that will use information 
from the database to discover what kind of articles the site's readers like.

The code helps in connecting  the database(news) and runs the the required
queries given in the project and print out the answers in command line.

Following are the questions which can be answered with the help of this code:
  1.What are the most popular three articles of all time? 
  2.Who are the most popular article authors of all time?
  3.On which days did more than 1% of requests lead to errors? 
  
REQUIRED:

Software installations:

1.Python
2.Install VirtualBox (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
3.Install Vagrant (https://www.vagrantup.com/downloads.html).
4.Download the VM configuration by using the github to fork and clone a repository
  (https://github.com/udacity/fullstack-nanodegree-vm).
5.Navigate to the above directory in terminal.
6.Run Vagrant up.
7.Run Vagrant ssh.
8.Download the newsdata.sql and keep this in vagrant directory shared by virtual machine.
  To load the data, change into vagrant directory and use the command (psql -d news -f newsdata.sql).
  
Steps to execute the program:

1.Download the loganalysis.py and keep this in the vagrant directory shared by virtual machine.
2.Navigate to the VM directory in your terminal.
3.Run vagrant up in terminal.(powers on the virtual machine)
4.Run vagrant ssh in terminal.(logs into the virtual machine)
5.Navigate to vagrant directory with the help of cd /vagrant command in terminal.
6.Run the application using python "loganalysis.py" in terminal.
7.you will be able to see the answers for the questions mentioned above.

  


