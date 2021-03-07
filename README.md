colab<br>
!/opt/bin/nvidia-smi<br>
!free -g<br>
!git clone https://chaowenguo:password@github.com/chaowenguo/tensorflow<br>
%cd tensorflow<br>
!python main.py<br>
!git add model<br>
!git config user.name dummy<br>
!git config user.email dummy<br>
!git commit --allow-empty-message -m ''<br>
!git push
