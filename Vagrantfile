# -*- mode: ruby -*-
# vi: set ft=ruby :

$machine_addr = "192.168.81.33"

$machine_cap  = "90"
$machine_cpus = "2"
$machine_name = "ubuntu-RobustMMLL"
$machine_ram  = "4096"


$provision_root = <<'SCRIPT_ROOT'

apt-get update
apt-get upgrade

apt-get install -y apt-transport-https ca-certificates curl coreutils libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libjpeg62 jq zip libtool

SCRIPT_ROOT


$provision_user = <<'SCRIPT_USER'

# Adds github.com to known hosts 
# Adds github.com to known hosts
if [ ! -n "$(grep "^github.com " ~/.ssh/known_hosts)" ]; then
    ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts;
fi
#echo "Adding local pip to the path"
#export PATH=${HOME}/.local/bin/:${PATH}

echo "Installing pyenv"
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
export PATH="~/.pyenv/bin:$PATH"
pyenv install 3.6.13
pyenv global 3.6.13
eval "$(pyenv init --path)"

echo "Upgrading pip, and creating virtualenv"
python -m pip install --upgrade pip

echo "Installing pip package dependencies"
pip install git+https://github.com/Musketeer-H2020/MMLL-Robust.git

#Set up some niceities in the shell
cat <<'EOF_BASHRC' > $HOME/.bashrc

# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT="[%F %T] "
export HISTFILE=/vagrant/bash_history
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"

export PATH=$HOME/.local/bin:$PATH
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init --path)"
fi

alias ls='ls --color=auto'
export PS1='\n\@ \w \e[0;32m $(__git_ps1 "(%s)") \e[m \n: \u@\h \j %; '
export PS1='\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n$ '

cd /vagrant

EOF_BASHRC

cat <<'EOF_VIM' > $HOME/.vimrc
set hlsearch
set showmode
set showmatch
set noautoindent
set esckeys

set scrolloff=3

" configure expanding of tabs for various file types
au BufRead,BufNewFile *.py set autoindent
au BufRead,BufNewFile *.py set expandtab
au BufRead,BufNewFile *.py set tabstop=4
au BufRead,BufNewFile *.py set softtabstop=4
au BufRead,BufNewFile *.py set shiftwidth=4

" configure expanding of tabs for various file types
au BufRead,BufNewFile *.yaml set autoindent
au BufRead,BufNewFile *.yaml set expandtab
au BufRead,BufNewFile *.yaml set shiftwidth=2
au BufRead,BufNewFile *.yaml set softtabstop=2
au BufRead,BufNewFile *.yaml set tabstop=2

EOF_VIM

SCRIPT_USER


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  #Use hosts git/ssh configs
  #if File.exists?(File.expand_path("~/.gitconfig"))
  #  config.vm.provision "file", source: "~/.gitconfig", destination: "~/.gitconfig"
  #end

  config.vm.provision :shell, inline: $provision_root
  config.vm.provision :shell, privileged: false, inline: $provision_user
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8888, host: 8881, auto_correct: true
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8001, host: 8001, auto_correct: true

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--name", $machine_name]
    vb.customize ["modifyvm", :id, "--cpus", $machine_cpus]
    vb.customize ["modifyvm", :id, "--cpuexecutioncap", $machine_cap]
    vb.customize ["modifyvm", :id, "--memory", $machine_ram]
  end

  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end

  if File.exists?(File.expand_path("~/.ssh/id_rsa"))
    config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"
  end

  if File.exists?(File.expand_path("~/.ssh/id_rsa.pub"))
    config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  end

  config.vm.hostname = $machine_name
  config.vm.network :private_network, ip: $machine_addr
end
