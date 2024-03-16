cd /root
mkdir douyin_analysis
tar -zxvf ./douyin_analysis.tar.gz -C ./douyin_analysis
cd ./douyin_analysis
docker rmi -f douyin_analysis-douyin_analysis:latest
docker compose down
docker compose up -d