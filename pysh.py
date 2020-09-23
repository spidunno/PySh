#Code is v messy
#I bet yours is too
#coding is hard
#do whatever with the code
#if you can understand it

import subprocess,os,sys

info=False

showargs=False

print("Welcome to pyterm. It's just bash right now.\n")

class colors:

  reset='\033[0m'
  bold='\033[01m'
  disable='\033[02m'
  underline='\033[04m'
  reverse='\033[07m'
  strikethrough='\033[09m'
  invisible='\033[08m'
  class fg: 
      black='\033[30m'
      red='\033[31m'
      green='\033[32m'
      orange='\033[33m'
      blue='\033[34m'
      purple='\033[35m'
      cyan='\033[36m'
      lightgrey='\033[37m'
      darkgrey='\033[90m'
      lightred='\033[91m'
      lightgreen='\033[92m'
      yellow='\033[93m'
      lightblue='\033[94m'
      pink='\033[95m'
      lightcyan='\033[96m'
  class bg: 
      black='\033[40m'
      red='\033[41m'
      green='\033[42m'
      orange='\033[43m'
      blue='\033[44m'
      purple='\033[45m'
      cyan='\033[46m'
      lightgrey='\033[47m'
cmd=''
arg=''
cd=False
exit=False

while exit==False:
  cwd=os.getcwd().replace(os.environ['HOME'],'~')
  user=os.environ['USER']
  host=os.environ['HOSTNAME']
  delimiter='$ '

  thing=input(colors.bold + colors.fg.green + user + '@' + host + colors.fg.red + '-py' + colors.reset + colors.bold + ':' + colors.fg.blue + cwd + colors.reset + colors.bold + delimiter)

  thing_split=thing.split(' ')

  for x in thing_split[0:1]:
    exec=True
    if showargs==True:
      print('cmd: ' + x)
    cmd=x
    if cmd=='cd':
      cd=True
    if cmd=='exit':
      exit=True
      break;
    if cmd=='showargs':
      if showargs==False:
        showargs=True
        print('Showing arguments!')
        exec=False
        break;
      if showargs==True:
        showargs==False
        print('Hiding arguments!')
        exec=False
        break;
      exec=False
    if cmd=='pyinfo':
      info=True
      exec=False
      print('PyTerm info\n')
  for x in thing_split[1:]:
    if cd==False:
      if showargs==True:
        print('arg: ' + x)
      arg=arg + ' ' + x
    if cd==True:
      os.chdir(x)
      x=''
      cd=False
    if info==True:
      if x=='-py':
        print(colors.bg.blue + "This is just a proof of concept!" + colors.reset + "\n\nInstead of running the input string in its full, I'm instead splitting it up into different sections or 'cmd's and 'arg's. this is just me testing so that I can make an actual custom shell(-like) thing.")
      break;
  if showargs==True:
    print('\noutput:\n')
  if exec==True:
    subprocess.run(cmd + arg,shell=True,executable='/bin/bash') 
  cmd=''
  arg=''
