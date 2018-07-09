# echo "export $PATH:$HOME/bin" >> ~/.bashrc

mkdir -p ~/bin

if [ -e ~/bin/sshas ]; then
    rm ~/bin/sshas
fi

python -m zipapp -p '/usr/bin/env python3' __main__.py --output ~/bin/sshas
