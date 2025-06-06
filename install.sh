sudo apt install screen -y
## Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
#
## in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
#
## Download and install Node.js:
nvm install 22
#
## Verify the Node.js version:
node -v # Should print "v22.15.0".
nvm current # Should print "v22.15.0".
#
## Verify npm version:
npm -v # Should print "10.9.2".

sudo apt install python3.10-venv -y

#create venv
python3 -m venv venv

#activate venv
source venv/bin/activate

#download deps
pip install -r requirements.txt


