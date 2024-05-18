# Smart Traffic Light
Projeto para a disciplina de Redes e Sistemas Autônomos que consiste em desenvolver um sistema de gestão de tráfego inteligente que utiliza câmeras em tempo real, para identificação do tráfego de veículos e peões, e comunicação entre nós, através de uma rede veicular implementada sobre [NAP-Vanetza](https://code.nap.av.it.pt/mobility-networks/vanetza).

## Setting up (Docker)
1. Install docker and docker-compose
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo bash -c 'echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker-ce.list'
sudo apt update
sudo apt install docker-ce docker-compose
```
2. Create the Docker network that the Vanetza containers will use to exchange ETSI C-ITS messages
```
docker network create vanetzalan0 --subnet 192.168.98.0/24
```
