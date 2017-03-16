# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. source - activate changes made to .bash_profile in the current session
2. pwd - prints working director
3. which - prints location of binary referenced by command
4. chmod - change file modes (permissions)
5. env - return list of environment variables set
6. cp - copy files
7. mv - move files
8. rm - delete files
9. sort - alphabetically sort lines in a file
10. sed - stream editor sort of like find and replace for in-console text streams
---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls - lists files in current directory

ls -a - above, but all files, including hidden

ls -l - lists files in long formatting mode, with permissions and other file metadata

ls -lh - same as ls -l except filesizes have suffix abbreviations

ls -lah - same as ls -lh, except shows hidden files

ls -t - sorts by time modified

ls -Glp - G adds color, p adds trailing slash to directories, l adds long formatting

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-G colors, easier to read

-p clearly identifies directories

-R displays subdirectories as well

-m displays names as comma-separated list, might be useful for programming

-d displays only directories

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

Xargs allows passing arbitrary numbers of arguments to commands. Invoking xargs will issue a single command for each argument, so it can be useful for mass deleting of files returned by the find command.

