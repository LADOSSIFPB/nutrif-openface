# nutrif-openface
Controle de acesso do Refeitório estudantil usando reconhecimento facial.

## Instalação e uso ##

### Docker ###

---

1) Clone Repo

```
git clone https://github.com/LADOSSIFPB/nutrif-openface.git
```

2) Pull imagem do docker

```
docker pull thayannevls/nutrif-openface
```

3) Rode a imagem docker na sua máquina e use os volumes para compartilhar arquivos da máquina hoster com o container do docker

```
docker run -v /Users/:/host -p 9000:9000 -p 8000:8000 -p 5000:5000 -t -i thayannevls/nutrif-openface /bin/bash
```

4) Se direcione para o diretório que você clonou anteriomente dentro do volume Docker

```
cd nutrif-openface
```

---

## Referências ##
OpenFace Project - https://cmusatyalab.github.io/openface/
Home Surveillance - https://github.com/BrandonJoffe/home_surveillance
