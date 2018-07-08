echo "export $PATH:$HOME/bin" >> ~/.bashrc

mkdir -p ~/bin
python -m zipapp -p '/usr/bin/env python3' __main__.py --output ~/bin/sshas
