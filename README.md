colab
!/opt/bin/nvidia-smi
!free -g
!git clone https://chaowenguo:password@github.com/chaowenguo/tensorflow
%cd tensorflow
!python main.py
!git add model
!git config user.name dummy
!git config user.email dummy
!git commit --allow-empty-message -m ''
!git push
